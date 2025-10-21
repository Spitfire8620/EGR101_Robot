"""High level robot orchestration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .audio import DEFAULT_SYNTHESIZER, SpeechSynthesizer
from .config import RobotConfig
from .controllers import MotorController
from .sensors import DistanceSensor


@dataclass(slots=True)
class RobotState:
    """In-memory snapshot of the robot state."""

    is_moving: bool = False
    last_message: Optional[str] = None


class Robot:
    """High-level interface for the EGR 101 robot.

    The class coordinates speech, movement, and sensor readings. Hardware
    specific logic can be provided by extending the placeholder controllers and
    sensors inside the :mod:`robot` package.
    """

    def __init__(
        self,
        config: Optional[RobotConfig] = None,
        *,
        motor_controller: Optional[MotorController] = None,
        distance_sensor: Optional[DistanceSensor] = None,
        synthesizer: Optional[SpeechSynthesizer] = None,
    ) -> None:
        self.config = config or RobotConfig()
        self.motor_controller = motor_controller or MotorController()
        self.distance_sensor = distance_sensor or DistanceSensor()
        self.synthesizer = synthesizer or DEFAULT_SYNTHESIZER
        self.state = RobotState()

        if self.config.say_hello_on_start:
            self.say(self.config.greeting_message)

    def say(self, message: str) -> None:
        """Make the robot speak *message*."""

        if not message:
            return
        self.state.last_message = message
        if self.config.voice_enabled:
            self.synthesizer.speak(message)
        else:
            print(f"[Robot muted] {message}")

    def move_forward(self, duration: Optional[float] = None, speed: Optional[float] = None) -> None:
        """Move forward at *speed* for *duration* seconds."""

        actual_speed = speed if speed is not None else self.config.default_speed
        self.state.is_moving = True
        self.motor_controller.move(abs(actual_speed), duration)

    def move_backward(self, duration: Optional[float] = None, speed: Optional[float] = None) -> None:
        """Move backward at *speed* for *duration* seconds."""

        actual_speed = speed if speed is not None else self.config.default_speed
        self.state.is_moving = True
        self.motor_controller.move(-abs(actual_speed), duration)

    def turn(self, angle_degrees: float, speed: Optional[float] = None) -> None:
        """Turn the robot by ``angle_degrees``."""

        actual_speed = speed if speed is not None else self.config.turn_speed
        direction = 1.0 if angle_degrees >= 0 else -1.0
        self.state.is_moving = True
        self.motor_controller.turn(direction * abs(actual_speed))
        self.say(f"Turning {'left' if direction > 0 else 'right'} {abs(angle_degrees):.0f} degrees.")

    def stop(self) -> None:
        """Stop all motion."""

        self.motor_controller.stop()
        self.state.is_moving = False

    def check_obstacles(self) -> float:
        """Return the distance to the nearest obstacle in centimeters."""

        reading = self.distance_sensor.read()
        if reading.distance_cm < 30:
            self.say("Obstacle detected! Stopping to avoid a collision.")
            self.stop()
        return reading.distance_cm

    def perform_intro_sequence(self) -> None:
        """Example sequence showcasing speech and movement."""

        self.say("Starting intro sequence.")
        self.move_forward(duration=1.5)
        self.turn(angle_degrees=90)
        self.move_forward(duration=1.0)
        self.stop()
        distance = self.check_obstacles()
        self.say(f"Obstacle distance: {distance:.1f} centimeters.")
        self.say("Intro sequence complete.")
