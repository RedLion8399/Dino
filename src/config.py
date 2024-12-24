"""This module provides the global configuration for the game."""
# pylint: disable=missing-docstring

from enum import StrEnum


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
        self.display_scale: tuple[int, int] = (800, 600)
        self.caption: str = "Dino"
        self.object_speed: int = 5


# Initialize the global configuration
config: Config = Config()
