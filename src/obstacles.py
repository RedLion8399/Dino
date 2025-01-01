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
        self.position_rect: pg.Rect
        self.hitbox: pg.Rect
        self.current_image: pg.Surface
        self.counter: Counter = Counter()
        self.OBJECT_SPEED: float = config.object_speed

    def update(self) -> None:
        """Update the position of the element and it's hitbox in the game."""
        self.move()
        self.position_rect.bottomleft = (int(self.x_position), int(self.y_position))
        self.hitbox.center = self.position_rect.center
        config.window.blit(self.current_image, self.position_rect)

        if self.position_rect.right <= 0:
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
        super().__init__(config.display_scale[0], config.display_scale[1])
        self.image_1: tuple[list[pg.Surface], pg.Rect, pg.Rect]
        self.image_2: tuple[list[pg.Surface], pg.Rect, pg.Rect]
        self.image_1 = seperate_images(load_image("cactus-big.png")[0], (3, 1))
        self.image_2 = seperate_images(load_image("cactus-small.png")[0], (3, 1))

        self.counter.reset_obstacle_counter()
        self.random_image()

    def random_image(self) -> None:
        """Randomly select an image for the Cactus element.

        Cactus has two different sprite sheets with 3 different sprites each.
        On every spawn of a new Cactus element, a random image is selected
        and the rect attribute is updated accordingly.
        """
        temp_image: tuple[list[pg.Surface], pg.Rect, pg.Rect] = rd.choice(
            [self.image_1, self.image_2]
        )

        self.current_image = rd.choice(temp_image[0])
        self.position_rect = temp_image[1]
        self.hitbox = temp_image[2]


class Bird(GameElement):
    """This class represents a Bird element in the game.
    It is a subclass of the GameElement class.
    It has a rect attribute that represents its position and size.
    """

    def __init__(self) -> None:
        super().__init__(config.display_scale[0], rd.choice([150, 300]))
        self.image: tuple[list[pg.Surface], pg.Rect, pg.Rect]
        self.image = seperate_images(load_image("birds.png")[0], (2, 1))
        self.position_rect = self.image[1]
        self.hitbox = self.image[2]

        self.counter.reset_obstacle_counter()

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
        super().__init__(config.display_scale[0], rd.randint(120, 250))
        self.current_image, self.position_rect, self.hitbox = load_image("cloud.png")
        self.OBJECT_SPEED = 1

        self.counter.reset_cloud_counter()


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

        self.immage_1, self.rect_1, *_ = load_image("ground.png")
        self.immage_2, self.rect_2, *_ = load_image("ground.png")

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
