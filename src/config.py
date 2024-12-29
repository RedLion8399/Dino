"""This module provides the global configuration for the game."""

# pylint: disable=no-member

from enum import StrEnum

import pygame as pg


class ColorTheme(StrEnum):
    """This class represents the color themes of the game as enums."""

    LIGHT_GRAY = "light_gray"


class Config:
    """This class provides the global configuration for the game.
    From any the same instance of the class is accessible so that
    the configuration is the same throughout all parts of the game.
    """

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.color_theme: ColorTheme = ColorTheme.LIGHT_GRAY
        self.display_scale: tuple[int, int]
        self.caption: str
        self.object_speed: int = 0
        self.window: pg.Surface
        self.background_color: pg.Color

    def init_screen(self) -> None:
        """Initialize the game screen globally."""
        pg.init()
        self.window = pg.display.set_mode(self.display_scale)
        pg.display.set_caption(self.caption)
        self.window.fill(self.background_color)


# Initialize the global configuration
config: Config = Config()
