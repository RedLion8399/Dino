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
        if not hasattr(cls, "instance"):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        self.__color_theme: ColorTheme = ColorTheme.LIGHT_GRAY
        self.object_speed: int = 5

    @property
    def get_color_theme(self) -> ColorTheme:
        return self.__color_theme

    @get_color_theme.setter
    def set_color_theme(self, color_theme: ColorTheme) -> None:
        self.__color_theme = color_theme

    @property
    def get_object_speed(self) -> int:
        return self.object_speed

    @get_object_speed.setter
    def set_object_speed(self, object_speed: int) -> None:
        self.object_speed = object_speed


# Initialize the global configuration
Config()
