"""This modules contains the central GameElement class of the game.
It provides the functionality to create and manage
the basic elements of the game.
"""

# pylint: disable=invalid-name

import random as rd

import pygame as pg

from config import config
from counter import Counter
from recourses import load_image, seperate_images


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
        self.counter: Counter = Counter()
        self.OBJECT_SPEED: float = config.object_speed

    def update(self) -> None:
        """Update the position of the element in the game."""
        self.move()
        self.rect.update((self.x_position, self.y_position), self.rect.size)
        config.window.blit(self.current_image, self.rect)

        if self.rect.right <= 0:
            self.kill()

    def move(self) -> None:
        """Move the element in the game."""
        self.x_position -= self.OBJECT_SPEED


class Cactus(GameElement):
    """This class represents a Cactus element in the game.
    It is a subclass of the GameElement class.
    It has a rect attribute that represents its position and size.
    """

    def __init__(self) -> None:
        super().__init__(config.display_scale[0], 200)
        self.image_1: tuple[list[pg.Surface], pg.Rect]
        self.image_2: tuple[list[pg.Surface], pg.Rect]
        self.image_1 = seperate_images(load_image("cactus-big.png")[0], (3, 1))
        self.image_2 = seperate_images(load_image("cactus-small.png")[0], (3, 1))

        self.random_image()

    def random_image(self) -> None:
        """Randomly select an image for the Cactus element.

        Cactus has two different sprite sheets with 3 different sprites each.
        On every spawn of a new Cactus element, a random image is selected
        and the rect attribute is updated accordingly.
        """
        temp_image: tuple[list[pg.Surface], pg.Rect] = rd.choice(
            [self.image_1, self.image_2]
        )
        self.rect = temp_image[1]
        self.current_image = rd.choice(temp_image[0])


class Bird(GameElement):
    """This class represents a Bird element in the game.
    It is a subclass of the GameElement class.
    It has a rect attribute that represents its position and size.
    """

    def __init__(self) -> None:
        super().__init__(config.display_scale[0], rd.choice([75, 200]))
        self.image: tuple[list[pg.Surface], pg.Rect]
        self.image = seperate_images(load_image("birds.png")[0], (2, 1))
        self.rect = self.image[1]

    def update(self) -> None:
        """Updates the whole Bird element in the game.

        Bird has two different immages to change between in order to create
        a flying animation. The animation state changes every 40 frames.
        """
        if self.counter.bird_animation_status:
            self.current_image = self.image[0][0]
        else:
            self.current_image = self.image[0][1]
        super().update()


class Cloud(GameElement):
    """This class represents a Cloud element in the game.
    It is a subclass of the GameElement class.
    It has a rect attribute that represents its position and size.
    """

    def __init__(self) -> None:
        super().__init__(config.display_scale[0], rd.randint(50, 100))
        self.current_image, self.rect = load_image("cloud.png")
        self.OBJECT_SPEED = 1


class Ground(GameElement):
    """This class represents a Ground element in the game.
    It is a subclass of the GameElement class.
    It has a rect attribute that represents its position and size.
    """

    def __init__(self) -> None:
        super().__init__(config.display_scale[0], config.display_scale[1])
        self.immage_1: pg.Surface
        self.immage_2: pg.Surface
        self.rect_1: pg.Rect
        self.rect_2: pg.Rect

        self.immage_1, self.rect_1 = load_image("ground.png", (1, 1))
        self.immage_2, self.rect_2 = load_image("ground.png", (1, 1))

        self.rect_1.bottomleft = (0, config.display_scale[1])
        self.rect_2.bottomleft = (self.rect_1.right, config.display_scale[1])

    def update(self) -> None:
        """Move the ground in the game.

        The ground moves as every other element in the game.
        Different from the other elements, the ground exists
        at every time of the game.
        That means two different ground images are needed wich are
        swiched every time one reaches the end.
        If the right end of on of them cross the window border,
        the other image is atteched at it's right side.
        """
        if self.rect_1.right <= 0:
            self.rect_1.left = self.rect_2.right

        if self.rect_2.right <= 0:
            self.rect_2.left = self.rect_1.right

        self.rect_1.move_ip(-self.OBJECT_SPEED, 0)
        self.rect_2.move_ip(-self.OBJECT_SPEED, 0)

        config.window.blit(self.immage_1, self.rect_1)
        config.window.blit(self.immage_2, self.rect_2)
