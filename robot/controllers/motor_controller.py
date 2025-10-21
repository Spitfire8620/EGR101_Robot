"""Base motor controller abstraction."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class MotorCommand:
    """Represents a command issued to the drivetrain."""

    action: str
    speed: float
    duration: Optional[float] = None


class MotorController:
    """Placeholder motor controller to be adapted to the team's hardware."""

    def __init__(self) -> None:
        self._last_command: Optional[MotorCommand] = None

    @property
    def last_command(self) -> Optional[MotorCommand]:
        """Return the last command that was issued."""

        return self._last_command

    def move(self, speed: float, duration: Optional[float] = None) -> MotorCommand:
        """Move forward or backward depending on the sign of *speed*."""

        command = MotorCommand("move", speed, duration)
        self._apply(command)
        return command

    def turn(self, speed: float, duration: Optional[float] = None) -> MotorCommand:
        """Turn in place using the differential drivetrain."""

        command = MotorCommand("turn", speed, duration)
        self._apply(command)
        return command

    def stop(self) -> MotorCommand:
        """Stop all motion immediately."""

        command = MotorCommand("stop", 0.0, None)
        self._apply(command)
        return command

    def _apply(self, command: MotorCommand) -> None:
        """Send the *command* to hardware.

        Replace this placeholder with GPIO, serial, or microcontroller code.
        """

        self._last_command = command
        print(
            f"[MotorController] action={command.action} speed={command.speed:.2f}"
            + (f" duration={command.duration:.2f}s" if command.duration else "")
        )
