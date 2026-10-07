"""Humanoid action controller with bounded interpolation and fail-safe state transitions."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Mapping


def _clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def interpolate_pose(
    start: Mapping[str, float], target: Mapping[str, float], alpha: float
) -> Dict[str, float]:
    """Interpolate a named-joint pose with a bounded progress value."""
    progress = _clamp(alpha, 0.0, 1.0)
    names = set(start) | set(target)
    return {
        name: start.get(name, 0.0)
        + progress * (target.get(name, 0.0) - start.get(name, 0.0))
        for name in sorted(names)
    }


class ActionStatus(str, Enum):
    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETE = "complete"
    SAFE_STOP = "safe_stop"


@dataclass
class GestureController:
    """Deterministic state machine for a bounded upper-body gesture."""

    target_pose: Mapping[str, float]
    duration_s: float = 2.0
    ramp_s: float = 0.25
    status: ActionStatus = ActionStatus.IDLE
    elapsed_s: float = 0.0
    current_pose: Dict[str, float] = field(default_factory=dict)
    start_pose: Dict[str, float] = field(default_factory=dict)

    def start(self, current_pose: Mapping[str, float]) -> None:
        self.current_pose = dict(current_pose)
        self.start_pose = dict(current_pose)
        self.elapsed_s = 0.0
        self.status = ActionStatus.RUNNING

    def pause(self) -> None:
        if self.status == ActionStatus.RUNNING:
            self.status = ActionStatus.PAUSED

    def resume(self) -> None:
        if self.status == ActionStatus.PAUSED:
            self.status = ActionStatus.RUNNING

    def safe_stop(self) -> None:
        self.status = ActionStatus.SAFE_STOP

    def step(self, dt_s: float) -> Dict[str, float]:
        """Advance one control step and return the bounded pose command."""
        if self.status in {ActionStatus.IDLE, ActionStatus.COMPLETE, ActionStatus.SAFE_STOP}:
            return dict(self.current_pose)
        if self.status == ActionStatus.PAUSED:
            return dict(self.current_pose)

        self.elapsed_s = min(self.duration_s, self.elapsed_s + max(0.0, dt_s))
        progress = self.elapsed_s / max(self.duration_s, 1e-6)
        eased = progress * progress * (3.0 - 2.0 * progress)
        self.current_pose = interpolate_pose(self.start_pose, self.target_pose, eased)
        if self.elapsed_s >= self.duration_s - 1e-9:
            self.status = ActionStatus.COMPLETE
        return dict(self.current_pose)
