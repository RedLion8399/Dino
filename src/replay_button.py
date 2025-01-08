"""This module contains the ReplayButton class.

The ReplayButton class is a button that allows
the player to replay the game after losing.
"""

# pylint: disable=no-member

from typing import Callable
import sys
import pygame as pg
from obstacles import GameElement
from config import config
from recourses import load_image


class ReplayButton(GameElement):
    """The ReplayButton class is a button that allows
    the player to replay the game after losing.
    """

    def __init__(self) -> None:
        super().__init__(config.display_scale[0] / 2, config.display_scale[1] / 2)
        self.current_image, self.position_rect, self.hitbox = load_image(
            "replay_button.png"
        )
        self.position_rect.center = (
            config.display_scale[0] // 2,
            config.display_scale[1] // 2,
        )
        self.OBJECT_SPEED = 0

    def update(self) -> None:
        config.window.blit(self.current_image, self.position_rect)
        pg.display.flip()

    def replay(self, main: Callable[[], None]) -> None:
        """Handle replay button clicks and restart the game.

        Args:
            main: The main game function to call when replay is clicked
            To rerun the game the main func is called recursively.
        """
        self.update()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.position_rect.collidepoint(event.pos):
                        main()
