"""The main module contains the main functionality of the programm.
It is the file, meant to be called directly to playthe game.
It initializes the grafics as well as controlls the main game functionalitys
defined in other modules.
"""

# pylint: disable=no-member

import sys
from typing import Final

import pygame as pg

from config import ColorTheme, config
from counter import Counter
from dino import Dino

config.color_theme = ColorTheme.LIGHT_GRAY
config.display_scale = (800, 600)
config.caption = "Dino"
config.background_color = pg.Color(255, 255, 255)
config.init_screen()

counter: Counter = Counter()
dino: Dino = Dino()

# Initializes the colors
BLACK: Final[pg.Color] = pg.Color(0, 0, 0)
WHITE: Final[pg.Color] = pg.Color(255, 255, 255)
GRAY: Final[pg.Color] = pg.Color(190, 190, 190)


def get_input() -> None:
    """This function gets the input from the user.
    It collects all inputs from the previous frame and
    processes them by modyfying the game according to the player wishes.
    """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        dino.process_input(event)


def game_over() -> None:
    """This function is called when the game is over."""
    counter.save_highscore()
    pg.quit()
    sys.exit()


def main() -> None:
    """This is the main function of the programm.
    It is the place were every functionality is stticked together.
    It initializes the game, runs it displays changes and checks for kollisiions.
    """
    while True:
        get_input()
        counter.count()
        pg.display.flip()
    game_over()


if __name__ == "__main__":
    main()
