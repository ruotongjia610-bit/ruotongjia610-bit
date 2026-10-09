"""Joint-limit and command-sanity checks for action execution."""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Mapping


@dataclass(frozen=True)
class JointLimit:
    lower: float
    upper: float

    def contains(self, value: float) -> bool:
        return self.lower <= value <= self.upper


@dataclass(frozen=True)
class SafetyConfig:
    joint_limits: Mapping[str, JointLimit]
    max_pose_step: float = 0.25


class SafetyMonitor:
    """Validates poses before they reach a controller interface."""

    def __init__(self, config: SafetyConfig) -> None:
        if config.max_pose_step <= 0.0:
            raise ValueError("max_pose_step must be positive")
        self.config = config

    def validate_pose(self, pose: Mapping[str, float]) -> None:
        for joint, value in pose.items():
            if not isfinite(value):
                raise ValueError(f"non-finite command for {joint}")
            limit = self.config.joint_limits.get(joint)
            if limit is not None and not limit.contains(value):
                raise ValueError(f"joint limit exceeded for {joint}")

    def validate_step(self, previous: Mapping[str, float], current: Mapping[str, float]) -> None:
        self.validate_pose(current)
        for joint in set(previous) | set(current):
            delta = abs(current.get(joint, 0.0) - previous.get(joint, 0.0))
            if delta > self.config.max_pose_step:
                raise ValueError(f"pose step too large for {joint}")

