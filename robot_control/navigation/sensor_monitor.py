"""Sensor-health gating for navigation commands."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class SensorStatus(str, Enum):
    HEALTHY = "healthy"
    STALE = "stale"
    FAULT = "fault"


@dataclass
class SensorMonitor:
    timeout_s: float = 0.5
    last_update_s: float | None = None
    status: SensorStatus = SensorStatus.STALE

    def update(self, timestamp_s: float) -> None:
        if timestamp_s < 0.0:
            raise ValueError("timestamp_s must be non-negative")
        self.last_update_s = timestamp_s
        self.status = SensorStatus.HEALTHY

    def evaluate(self, now_s: float) -> SensorStatus:
        if now_s < 0.0:
            raise ValueError("now_s must be non-negative")
        if self.last_update_s is None or now_s - self.last_update_s > self.timeout_s:
            self.status = SensorStatus.STALE
        return self.status

    @property
    def safe_to_move(self) -> bool:
        return self.status == SensorStatus.HEALTHY

