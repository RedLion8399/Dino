"""This modules contains the central GameElement class of the game.
It provides the functionality to create and manage
the basic elements of the game.
"""

import pygame as pg

class GameElement(pg.sprite.Sprite):
    """This class represents any element in the game.
    It is a subclass of the pygame.sprite.Sprite class.
    It has a rect attribute that represents its position and size.
    """
    def __init__(self, x_position:float, y_position:float) -> None:
        super().__init__()
        self.x_position: float = x_position
        self.y_position: float = y_position
