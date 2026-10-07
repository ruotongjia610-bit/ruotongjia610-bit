"""Waypoint sequencing and arrival-event generation."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, List, Optional


@dataclass(frozen=True)
class Waypoint:
    name: str
    x_m: float
    y_m: float
    tolerance_m: float = 0.35


class RouteState(str, Enum):
    READY = "ready"
    ACTIVE = "active"
    COMPLETE = "complete"
    CANCELLED = "cancelled"


class RouteManager:
    def __init__(self, waypoints: Iterable[Waypoint]) -> None:
        self.waypoints: List[Waypoint] = list(waypoints)
        if not self.waypoints:
            raise ValueError("route requires at least one waypoint")
        self.index = 0
        self.state = RouteState.READY

    @property
    def active_waypoint(self) -> Optional[Waypoint]:
        return self.waypoints[self.index] if self.index < len(self.waypoints) else None

    def start(self) -> None:
        if self.state == RouteState.READY:
            self.state = RouteState.ACTIVE

    def update(self, distance_to_goal_m: float) -> Optional[str]:
        if distance_to_goal_m < 0.0:
            raise ValueError("distance_to_goal_m must be non-negative")
        if self.state != RouteState.ACTIVE or self.active_waypoint is None:
            return None
        if distance_to_goal_m <= self.active_waypoint.tolerance_m:
            name = self.active_waypoint.name
            self.index += 1
            if self.active_waypoint is None:
                self.state = RouteState.COMPLETE
            return name
        return None

    def cancel(self) -> None:
        self.state = RouteState.CANCELLED

