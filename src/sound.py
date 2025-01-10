"""
sound.py

This module defines the `Sound` class for managing and playing various sound effects 
in the Chrome Dino game. It encapsulates methods to load and play sound files 
associated with different game events.
"""

# pylint: disable=invalid-name

from typing import Final
import pygame as pg
from recourses import load_sound


class Sound:
    """The sound class loads and plays sound effects."""

    def __init__(self):
        pg.mixer.init()

        self.CHECK_POINT: Final[pg.mixer.Sound] = load_sound("checkPoint.wav")
        self.DIE: Final[pg.mixer.Sound] = load_sound("die.wav")
        self.JUMP: Final[pg.mixer.Sound] = load_sound("jump.wav")

    def play_check_point(self) -> None:
        """Plays the check point sound effect."""
        self.CHECK_POINT.play()

    def play_die(self) -> None:
        """Plays the die sound effect."""
        self.DIE.play()

    def play_jump(self) -> None:
        """Plays the jump sound effect."""
        self.JUMP.play()
