"""This modules contains the central GameElement class of the game.
It provides the functionality to create and manage
the basic elements of the game.
"""

import pygame as pg
from recourses import load_image, seperate_images
from config import config


class GameElement(pg.sprite.Sprite):
    """This class represents any element in the game.
    It is a subclass of the pygame.sprite.Sprite class.
    It has a rect attribute that represents its position and size.
    """

    def __init__(self, x_position: float, y_position: float) -> None:
        super().__init__()
        self.x_position: float = x_position
        self.y_position: float = y_position
        self.rect: pg.Rect
        self.current_image: pg.Surface

    def update(self, speed: float = config.object_speed) -> None:
        """Update the position of the element in the game."""
        self.move(speed)
        self.rect.update((self.x_position, self.y_position), self.rect.size)
        config.window.blit(self.current_image, self.rect)

    def move(self, speed: float) -> None:
        """Move the element in the game."""
        self.x_position -= speed


class Cactus(GameElement):
    """This class represents a Cactus element in the game.
    It is a subclass of the GameElement class.
    It has a rect attribute that represents its position and size.
    """

    def __init__(self, x_position: float, y_position: float) -> None:
        super().__init__(x_position, y_position)
        self.image_1: tuple[list[pg.Surface], pg.Rect]
        self.image_2: tuple[list[pg.Surface], pg.Rect]
        self.image_1 = seperate_images(load_image("cactus-big.png")[0], (3, 1))
        self.image_2 = seperate_images(load_image("cactus-small.png")[0], (3, 1))


class Bird(GameElement):
    """This class represents a Bird element in the game.
    It is a subclass of the GameElement class.
    It has a rect attribute that represents its position and size.
    """

    def __init__(self, x_position: float, y_position: float) -> None:
        super().__init__(x_position, y_position)
        self.image: tuple[list[pg.Surface], pg.Rect]
        self.image = seperate_images(load_image("birds.png")[0], (2, 1))
        self.rect = self.image[1]


class Cloud(GameElement):
    """This class represents a Cloud element in the game.
    It is a subclass of the GameElement class.
    It has a rect attribute that represents its position and size.
    """

    def __init__(self, x_position: float, y_position: float) -> None:
        super().__init__(x_position, y_position)
        self.current_image, self.rect = load_image("cloud.png")


class Ground(GameElement):
    """This class represents a Ground element in the game.
    It is a subclass of the GameElement class.
    It has a rect attribute that represents its position and size.
    """

    def __init__(self, x_position: float, y_position: float) -> None:
        super().__init__(x_position, y_position)
        self.immage_1: pg.Surface
        self.immage_2: pg.Surface
        self.rect_1: pg.Rect
        self.rect_2: pg.Rect

        self.immage_1, self.rect_1 = load_image("ground.png")
        self.immage_2, self.rect_2 = load_image("ground.png")
