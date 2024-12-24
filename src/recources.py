"""This module manages the external resources of the game.
It is responsible for loading and storing the images and sounds from their files and preparing
them for use in the game.
"""

import pygame as pg


def load_image(file_name:str) -> pg.Surface:
    """Load an image from a file and return it as a pygame.Surface object.

    Args:
        file_name (str): The name of the file to load.
    
    Returns:
        image (pg.Surface): The loaded image as a pygame.Surface object.
    """
    file_path: str = f"src/images/light_gray/{file_name}"
    try:
        image: pg.Surface = pg.image.load(file_path).convert_alpha()
    except FileNotFoundError as error:
        raise SystemExit(f"Could not load image '{file_path}' : {str(error)}") from error

    # Makes the background of the image transparent
    image.set_colorkey(image.get_at((0, 0)))
    return image

def load_sound(file_name:str) -> pg.mixer.Sound:
    """Load a sound from a file and return it as a pygame.mixer.Sound object.

    Args:
        file_name (str): The name of the file to load.
    
    Returns:
        sound (pg.mixer.Sound): The loaded sound as a pygame.mixer.Sound object.
    """
    file_path: str = f"src/sounds/{file_name}"
    try:
        sound: pg.mixer.Sound = pg.mixer.Sound(file_path)
    except FileNotFoundError as error:
        raise SystemExit(f"Could not load sound '{file_path}' : {str(error)}") from error
    return sound

def seperate_images(image: pg.Surface, size: tuple[int, int]) -> list[pg.Surface]:
    """Seperate an image into smaller images of a given size.
    All of them must have the same size and must be ordered in a grid.

    Args:
        image (pg.Surface): The image to seperate.
        size (tuple[int, int]): The amount of the image to seperate. (width, height)
    
    Returns:
        list[pg.Surface]: A list of seperated images.
    """
    width: float = image.get_width() / size[0]
    height: float = image.get_height() / size[1]
    immages: list[pg.Surface] = []

    for i in range(size[1]):
        for j in range(size[0]):
            immages.append(image.subsurface((j * width, i * height, width, height)))
    return immages
