"""Configuration objects for the robot."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass(slots=True)
class RobotConfig:
    """Configuration used to initialize a :class:`robot.robot.Robot`."""

    name: str = "EGR101 Robot"
    voice_enabled: bool = True
    default_speed: float = 0.5
    turn_speed: float = 0.4
    say_hello_on_start: bool = True
    greeting_message: str = "Hello! I'm ready for the EGR 101 competition."
    extra: dict[str, object] = field(default_factory=dict)

    def get(self, key: str, default: Optional[object] = None) -> Optional[object]:
        """Retrieve an extra configuration value."""

        return self.extra.get(key, default)
