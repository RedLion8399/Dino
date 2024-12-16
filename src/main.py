"""The main module contains the main functionality of the programm.
It is the file, meant to be called directly to playthe game.
It initializes the grafics as well as controlls the main game functionalitys
defined in other modules.
"""

from random import randint  # pylint: disable=unused-import
import time as t  # pylint: disable=unused-import
import sys
import pygame as pg

pg.init()  # pylint: disable=no-member


# Initializes the window
window_scale: list[int] = [800, 600]
window: pg.Surface = pg.display.set_mode((window_scale[0], window_scale[1]))  # pylint: disable=no-member
pg.display.set_caption("Dino")

# Initializes the colors
black: pg.Color = pg.Color(0, 0, 0)
white: pg.Color = pg.Color(255, 255, 255)
gray: pg.Color = pg.Color(190, 190, 190)

object_speed: int
score: int = 0


def game_over() -> None:
    """This function is called when the game is over."""

    sys.exit()
    pg.quit()  # pylint: disable=no-member


def main() -> None:
    """This is the main function of the programm.
    It is the place were every functionality is stticked together.
    It initializes the game, runs it displays changes and checks for kollisiions.
    """

    while True:
        #get imput 
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP or pg.K_SPACE:
                    if not Sneak
                        Jump = True
                if event.key == pg.K_DOWN and not Jump:
                    Sneak = True

        move_objects()
        update_display()

        if kollision():
            break
        count_score()

    game_over()


if __name__ == "__main__":
    main()
