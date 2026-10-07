"""Vendor-neutral tour-navigation and safety-layer reference implementation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple


@dataclass(frozen=True)
class Goal:
    name: str
    x_m: float
    y_m: float


@dataclass(frozen=True)
class Velocity:
    linear_mps: float = 0.0
    angular_rps: float = 0.0


@dataclass
class SafetyGuard:
    max_linear_mps: float = 0.35
    max_angular_rps: float = 0.60
    paused: bool = False
    sensor_healthy: bool = True

    def command(self, requested: Velocity) -> Velocity:
        """Limit commands and fail closed when the perception path is unhealthy."""
        if self.paused or not self.sensor_healthy:
            return Velocity()
        return Velocity(
            linear_mps=max(-self.max_linear_mps, min(self.max_linear_mps, requested.linear_mps)),
            angular_rps=max(-self.max_angular_rps, min(self.max_angular_rps, requested.angular_rps)),
        )


class TourRoute:
    def __init__(self, goals: Iterable[Goal], guard: Optional[SafetyGuard] = None) -> None:
        self.goals: List[Goal] = list(goals)
        self.guard = guard or SafetyGuard()
        self.index = 0
        self.arrivals: List[str] = []

    @property
    def active_goal(self) -> Optional[Goal]:
        return self.goals[self.index] if self.index < len(self.goals) else None

    def pause(self) -> None:
        self.guard.paused = True

    def resume(self) -> None:
        self.guard.paused = False

    def cancel(self) -> Velocity:
        self.index = len(self.goals)
        return self.guard.command(Velocity())

    def update(self, requested: Velocity, at_goal: bool = False) -> Tuple[Velocity, Optional[str]]:
        """Return a guarded command and emit one arrival event when appropriate."""
        arrival = None
        if at_goal and self.active_goal is not None:
            arrival = self.active_goal.name
            self.arrivals.append(arrival)
            self.index += 1
        return self.guard.command(requested), arrival

