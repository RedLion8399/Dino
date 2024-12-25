""" This module contains the behaviour of the dino.
The dino is the main character of the game and is controlled by the player.
It can run, jump and sneak.
classes:
    Dino: This class contains the behaviour of the dino.
    Status: This class contains the status of the dino as an enum.
"""
# pylint: disable=no-member
# pylint: disable=unused-private-member

from enum import Enum
from typing import Final
import pygame as pg
from recourses import load_image, seperate_images
from obstacles import GameElement

class Status(Enum):
    """This class contains the status of the dino.
    The status displays the current state of the dino.
    Atributes:
        RUNNING: The dino is running.
        JUMPING: The dino is jumping.
        SNEAKING: The dino is sneaking.
    """
    RUNNING = 1
    JUMPING = 2
    SNEAKING = 3


class Dino(GameElement):
    """This class contains the behaviour of the dino.
    The dino is the main character of the game and is controlled by the player.
    It can run, jump and sneak.
    Atributes:
        position: The vertical position of the dino.
        status: The status of the dino as an enum of the Status class.
        color_theme: The color theme of the dino as a string.

    Methods:
        update: calls the specific method for the current state of the dino.
        check_collision: checks if the dino collides with an object.
    """
    def __init__(self) -> None:
        super().__init__(20, 100)
        self.status: Status = Status.RUNNING

        self.running_image: tuple[list[pg.Surface], pg.Rect]
        self.sneaking_image: tuple[list[pg.Surface], pg.Rect]
        self.load_images()

    def process_input(self, event: pg.event.Event) -> None:
        """This function gets the input from the user.
        It gets all inputs from the previous frame and
        looks for keys they are relevant for the dino movement.
        In case of those keys being pressed, it is checked if it's
        possible to change the state of the dino to the desired one.

        Args:
            event: The event that was triggered by the user
        
        Variables:
            JUMP_KEYS: list of integers that represent the keys that make the dino jump.
            SNEAK_KEYS: list of integers that represent the keys that make the dino sneak.

        Examples:
            >>> dino: Dino = Dino()
            >>> for event in pg.event.get():
            >>>     dino.process_input(event)
        """
        JUMP_KEYS: Final[list[int]] = [pg.K_UP, pg.K_SPACE]  # pylint: disable=invalid-name
        SNEAK_KEYS: Final[list[int]] = [pg.K_DOWN]  # pylint: disable=invalid-name

        if event.type == pg.KEYDOWN:
            if event.key in JUMP_KEYS and self.status == Status.RUNNING:
                self.status = Status.JUMPING
            if event.key in SNEAK_KEYS and self.status == Status.RUNNING:
                self.status = Status.SNEAKING
        if event.type == pg.KEYUP:
            if event.key in SNEAK_KEYS and self.status == Status.SNEAKING:
                self.status = Status.RUNNING

    def __run(self) -> None:
        raise NotImplementedError("Subclasses must implement the run method.")

    def __jump(self) -> None:
        raise NotImplementedError("Subclasses must implement the jump method.")

    def __sneak(self) -> None:
        raise NotImplementedError("Subclasses must implement the sneak method.")

    def update(self) -> None:
        raise NotImplementedError("Subclasses must implement the update method.")

    def check_collision(self) -> bool:
        raise NotImplementedError("Subclasses must implement the check_collision method.")

    def load_images(self) -> None:
        """This function loads the images for the dino."""
        self.running_image = seperate_images(
            load_image("dino_running.png")[0], (5, 1))
        self.sneaking_image = seperate_images(
            load_image("dino_sneaking.png")[0], (2, 1))
