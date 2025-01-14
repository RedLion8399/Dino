"""The score the player recieves is displayed heren

As long as the player survives in the game he recieves
score points. The score is displayed on the screen.
"""

import pygame as pg

from config import config
from obstacles import GameElement
from recourses import load_image, seperate_images


class Score(GameElement):
    """The score management and display is implemented here."""

    def __init__(self) -> None:
        super().__init__(config.display_scale[0], 0)
        self.OBJECT_SPEED = 0

        self.immages: tuple[list[pg.Surface], pg.Rect, pg.Rect]
        self.immages = seperate_images(load_image("numbers.png")[0], (12, 1))
        self.immage, self.position_rect, self.hitbox = self.immages

    def split_number(self, number: int) -> list[int]:
        """Split an int into a list of digits of a length of five

        Args:
            number (int): The number to be split

        Returns:
            list[int]: The list of split digits
        """
        digits: list[int] = [int(digit) for digit in str(number)]
        digits.reverse()
        while len(digits) < 5:
            digits.append(0)
        digits.reverse()
        return digits

    def _display_characters(self, position: int, characters: list[int]) -> None:
        """Display a list of characters on the screen

        Args:
            position (int): The position on the screen
            The position is counted from the right of the leftmost character
            to the right side of the screen
            characters (list[int]): The list of characters to be displayed
            It refers to the immage list of the Score class
        """

        for i, character in enumerate(characters):
            self.current_image = self.immage[character]
            self.position_rect.x = config.display_scale[0] - position + i * 25
            config.window.blit(self.current_image, self.position_rect)

    def display_highscore(self) -> None:
        """Display the highscore on the screen"""
        highscore: int = self.counter.highscore
        digits: list[int] = self.split_number(highscore)

        self._display_characters(300, digits)

        digits = [10, 11]

        self._display_characters(365, digits)

    def update(self) -> None:
        # At first the singulat chars are seperated and
        # filled up to a total of five using zeros
        sore: int = self.counter.score
        digits: list[int] = self.split_number(sore)

        self._display_characters(125, digits)
