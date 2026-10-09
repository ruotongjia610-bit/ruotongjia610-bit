"""Action lifecycle and safety-aware execution state machine."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Callable, Dict, Mapping

from .safety import SafetyMonitor
from .trajectory import Pose, PoseTrajectory, TrajectoryConfig


class ActionState(str, Enum):
    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETE = "complete"
    STOPPED = "stopped"
    FAULT = "fault"


@dataclass(frozen=True)
class ActionEvent:
    state: ActionState
    elapsed_s: float
    message: str = ""


class ActionController:
    """Executes a bounded pose trajectory and emits lifecycle events."""

    def __init__(self, safety: SafetyMonitor, on_event: Callable[[ActionEvent], None] | None = None) -> None:
        self.safety = safety
        self.on_event = on_event
        self.state = ActionState.IDLE
        self.elapsed_s = 0.0
        self.current_pose: Pose = {}
        self._trajectory: PoseTrajectory | None = None

    def _emit(self, message: str = "") -> None:
        if self.on_event:
            self.on_event(ActionEvent(self.state, self.elapsed_s, message))

    def start(self, current_pose: Mapping[str, float], target_pose: Mapping[str, float], config: TrajectoryConfig | None = None) -> None:
        try:
            self.safety.validate_pose(current_pose)
            self.safety.validate_pose(target_pose)
        except ValueError as exc:
            self.state = ActionState.FAULT
            self._emit(str(exc))
            return
        self.current_pose = dict(current_pose)
        self._trajectory = PoseTrajectory(current_pose, target_pose, config)
        self.elapsed_s = 0.0
        self.state = ActionState.RUNNING
        self._emit("action started")

    def pause(self) -> None:
        if self.state == ActionState.RUNNING:
            self.state = ActionState.PAUSED
            self._emit("action paused")

    def resume(self) -> None:
        if self.state == ActionState.PAUSED:
            self.state = ActionState.RUNNING
            self._emit("action resumed")

    def stop(self, reason: str = "stopped by operator") -> None:
        self.state = ActionState.STOPPED
        self._emit(reason)

    def fault(self, reason: str) -> None:
        self.state = ActionState.FAULT
        self._emit(reason)

    def step(self, dt_s: float) -> Pose:
        if dt_s < 0.0:
            raise ValueError("dt_s must be non-negative")
        if self.state != ActionState.RUNNING or self._trajectory is None:
            return dict(self.current_pose)
        next_elapsed = min(self._trajectory.config.duration_s, self.elapsed_s + dt_s)
        next_pose = self._trajectory.sample(next_elapsed)
        try:
            self.safety.validate_step(self.current_pose, next_pose)
        except ValueError as exc:
            self.fault(str(exc))
            return dict(self.current_pose)
        self.elapsed_s = next_elapsed
        self.current_pose = next_pose
        if self._trajectory.completed(self.elapsed_s):
            self.state = ActionState.COMPLETE
            self._emit("action complete")
        return dict(self.current_pose)

