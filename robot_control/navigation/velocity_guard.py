"""Velocity limiting and fail-closed command handling."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VelocityCommand:
    linear_mps: float = 0.0
    angular_rps: float = 0.0


@dataclass(frozen=True)
class VelocityLimits:
    max_linear_mps: float = 0.35
    max_angular_rps: float = 0.60


class VelocityGuard:
    def __init__(self, limits: VelocityLimits | None = None) -> None:
        self.limits = limits or VelocityLimits()
        self.enabled = True

    def stop(self) -> None:
        self.enabled = False

    def resume(self) -> None:
        self.enabled = True

    def apply(self, requested: VelocityCommand) -> VelocityCommand:
        if not self.enabled:
            return VelocityCommand()
        return VelocityCommand(
            linear_mps=max(-self.limits.max_linear_mps, min(self.limits.max_linear_mps, requested.linear_mps)),
            angular_rps=max(-self.limits.max_angular_rps, min(self.limits.max_angular_rps, requested.angular_rps)),
        )

