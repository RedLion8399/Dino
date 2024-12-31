"""This module manages the external resources of the game.
It is responsible for loading and storing the images and sounds from
their files and preparing them for use in the game.
"""

import os

import pygame as pg

from config import config


def full_path(file_name: str, image: bool = False) -> str:
    """Return the full path of a file in the recources directory.

    Args:
        file_name (str): The name of the file.
        image (bool): True if the file is an image, False if it is a sound.

    Returns:
        str: The full path of the file.
    """
    if not image:
        # Only executed if it is a sound file
        return os.path.abspath(
            os.path.join(os.path.dirname(__file__), "sounds", file_name)
        )
    color_theme = config.color_theme
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "images", color_theme, file_name)
    )


def load_image(
    file_name: str, size: tuple[float, float] = (0.6, 0.6)
) -> tuple[pg.Surface, pg.Rect]:
    """Load an image from a file and return it as a pygame.Surface object.

    Args:
        file_name (str): The name of the file to load.
        size (tuple[float, float]): Factor to scale the image by.

    Returns:
        tuple[pg.Surface, pg.Rect]: The loaded image as a pygame.Surface object
        and its rect representation.
    """
    path: str = full_path(file_name, True)
    try:
        image: pg.Surface = pg.image.load(path).convert_alpha()
    except FileNotFoundError as error:
        raise SystemExit(f"Could not load image '{path}' : {str(error)}") from error

    # Makes the background of the image transparent
    image.set_colorkey(image.get_at((0, 0)))

    rect: pg.Rect = image.get_rect()
    rect.scale_by_ip(size[0], size[1])
    return (image, rect)


def load_sound(file_name: str) -> pg.mixer.Sound:
    """Load a sound from a file and return it as a pygame.mixer.Sound object.

    Args:
        file_name (str): The name of the file to load.

    Returns:
        sound (pg.mixer.Sound): The loaded sound as a pygame.mixer.Sound object.
    """
    path: str = full_path(file_name)
    try:
        sound: pg.mixer.Sound = pg.mixer.Sound(path)
    except FileNotFoundError as error:
        raise SystemExit(f"Could not load sound '{path}' : {str(error)}") from error
    return sound


def seperate_images(
    image: pg.Surface,
    image_count: tuple[int, int],
    size: tuple[float, float] = (0.6, 0.6),
) -> tuple[list[pg.Surface], pg.Rect]:
    """Seperate an image into smaller images of a given size.
    All of them must have the same size and must be ordered in a grid.

    Args:
        image (pg.Surface): The image to seperate.
        image_count (tuple[int, int]): The amount of the image to seperate. (width, height)
        size (tuple[float, float]): Factor to scale the image by.

    Returns:
        touple[List[pg.Surface], Rect]: List of the seperated images
        and their regt representation.
    """
    width: float = image.get_width() / image_count[0]
    height: float = image.get_height() / image_count[1]
    immages: list[pg.Surface] = []

    for i in range(image_count[1]):
        for j in range(image_count[0]):
            immages.append(image.subsurface((j * width, i * height, width, height)))

    rect = immages[0].get_rect()
    rect.scale_by_ip(size[0], size[1])
    return (immages, rect)
