"""Placeholder distance sensor driver."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class DistanceSensorReading:
    """Represents a single distance sensor reading."""

    distance_cm: float
    raw_value: Optional[int] = None


class DistanceSensor:
    """Base class for an obstacle detection sensor."""

    def __init__(self) -> None:
        self._last_reading: Optional[DistanceSensorReading] = None

    @property
    def last_reading(self) -> Optional[DistanceSensorReading]:
        """Return the most recent reading."""

        return self._last_reading

    def read(self) -> DistanceSensorReading:
        """Return a simulated reading.

        Replace this method with hardware specific logic.
        """

        reading = DistanceSensorReading(distance_cm=100.0, raw_value=None)
        self._last_reading = reading
        print(f"[DistanceSensor] distance={reading.distance_cm:.1f}cm")
        return reading
