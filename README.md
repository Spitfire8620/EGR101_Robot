# EGR101 Robot

This repository contains starter code for the EGR 101 competition robot. The
project includes a high-level `Robot` class that orchestrates motor control,
sensor readings, and speech output so the team can focus on adapting the code
to their specific hardware.

## Features

- Text-to-speech support using `pyttsx3` when available (falls back to console
  output when not installed).
- Placeholder motor controller and distance sensor classes that can be
  extended with GPIO, serial, or microcontroller logic.
- Demonstration sequence showing how to make the robot move, speak, and respond
  to obstacle detection.

## Requirements

Python 3.10 or higher is recommended. Install optional dependencies with:

```bash
pip install pyttsx3
```

## Running the demo

```bash
python Main.py
```

The demo will run an introductory sequence, commanding the robot to move,
turn, check for obstacles, and speak status updates.
