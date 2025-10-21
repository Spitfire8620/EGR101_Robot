"""Audio helpers for letting the robot talk."""

from __future__ import annotations

import importlib.util
from typing import Optional


class SpeechSynthesizer:
    """Simple text-to-speech helper.

    Attempts to use ``pyttsx3`` when available. When the dependency is not
    installed, messages are printed to the console so the flow can be verified
    during development without hardware.
    """

    def __init__(self) -> None:
        self._engine = self._create_engine()

    @staticmethod
    def _create_engine():
        spec = importlib.util.find_spec("pyttsx3")
        if spec is None:
            return None
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None  # for type checkers
        spec.loader.exec_module(module)
        return module.init()

    def speak(self, message: str, *, blocking: bool = True) -> None:
        """Speak *message* using the available output device."""

        if not message:
            return
        if self._engine is None:
            print(f"[Robot] {message}")
            return
        self._engine.say(message)
        if blocking:
            self._engine.runAndWait()


DEFAULT_SYNTHESIZER = SpeechSynthesizer()
