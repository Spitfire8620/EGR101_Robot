"""Entry point for running the EGR 101 robot demo."""

from __future__ import annotations

from robot import Robot, RobotConfig


def main() -> None:
    """Run a short demonstration for the robot."""

    config = RobotConfig()
    robot = Robot(config)
    robot.perform_intro_sequence()


if __name__ == "__main__":
    main()
