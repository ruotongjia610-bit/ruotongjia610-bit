"""Bounded joint-space trajectory generation."""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Dict, Mapping

Pose = Dict[str, float]


def smoothstep(progress: float) -> float:
    """Cubic easing with zero slope at both endpoints."""
    p = max(0.0, min(1.0, progress))
    return p * p * (3.0 - 2.0 * p)


@dataclass(frozen=True)
class TrajectoryConfig:
    duration_s: float = 2.0
    max_joint_speed: float = 2.0

    def __post_init__(self) -> None:
        if self.duration_s <= 0.0:
            raise ValueError("duration_s must be positive")
        if self.max_joint_speed <= 0.0:
            raise ValueError("max_joint_speed must be positive")


class PoseTrajectory:
    """Interpolates a named-joint pose while enforcing finite inputs."""

    def __init__(
        self,
        start: Mapping[str, float],
        target: Mapping[str, float],
        config: TrajectoryConfig | None = None,
    ) -> None:
        self.start = dict(start)
        self.target = dict(target)
        self.config = config or TrajectoryConfig()
        self._validate(self.start)
        self._validate(self.target)

    @staticmethod
    def _validate(pose: Mapping[str, float]) -> None:
        if not pose:
            raise ValueError("pose cannot be empty")
        if not all(isfinite(value) for value in pose.values()):
            raise ValueError("pose values must be finite")

    def sample(self, elapsed_s: float) -> Pose:
        progress = elapsed_s / self.config.duration_s
        alpha = smoothstep(progress)
        names = set(self.start) | set(self.target)
        return {
            name: self.start.get(name, 0.0)
            + alpha * (self.target.get(name, 0.0) - self.start.get(name, 0.0))
            for name in sorted(names)
        }

    def completed(self, elapsed_s: float) -> bool:
        return elapsed_s >= self.config.duration_s - 1e-9

