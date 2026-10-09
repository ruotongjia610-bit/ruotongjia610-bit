"""Mission-level coordination for route, sensors, and velocity safety."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from .route_manager import RouteManager, RouteState
from .sensor_monitor import SensorMonitor
from .velocity_guard import VelocityCommand, VelocityGuard


class MissionState(str, Enum):
    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETE = "complete"
    CANCELLED = "cancelled"
    FAULT = "fault"


@dataclass(frozen=True)
class MissionEvent:
    state: MissionState
    waypoint: Optional[str] = None
    message: str = ""


class MissionManager:
    def __init__(self, route: RouteManager, sensors: SensorMonitor, guard: VelocityGuard) -> None:
        self.route = route
        self.sensors = sensors
        self.guard = guard
        self.state = MissionState.IDLE
        self.last_command = VelocityCommand()

    def start(self) -> None:
        self.route.start()
        self.state = MissionState.RUNNING

    def pause(self) -> VelocityCommand:
        self.state = MissionState.PAUSED
        self.guard.stop()
        self.last_command = VelocityCommand()
        return self.last_command

    def resume(self) -> None:
        if self.state == MissionState.PAUSED:
            self.guard.resume()
            self.state = MissionState.RUNNING

    def cancel(self) -> VelocityCommand:
        self.route.cancel()
        self.state = MissionState.CANCELLED
        self.guard.stop()
        self.last_command = VelocityCommand()
        return self.last_command

    def tick(self, requested: VelocityCommand, distance_to_goal_m: float, now_s: float) -> MissionEvent:
        if self.state != MissionState.RUNNING:
            return MissionEvent(self.state, message="mission is not running")
        self.sensors.evaluate(now_s)
        if not self.sensors.safe_to_move:
            self.state = MissionState.FAULT
            self.guard.stop()
            self.last_command = VelocityCommand()
            return MissionEvent(self.state, message="sensor data is stale")
        arrival = self.route.update(distance_to_goal_m)
        if self.route.state == RouteState.COMPLETE:
            self.state = MissionState.COMPLETE
            self.guard.stop()
            self.last_command = VelocityCommand()
            return MissionEvent(self.state, waypoint=arrival, message="route complete")
        self.last_command = self.guard.apply(requested)
        return MissionEvent(self.state, waypoint=arrival)

