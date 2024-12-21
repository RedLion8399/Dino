""" This module contains the behaviour of the dino.
The dino is the main character of the game and is controlled by the player.
It can run, jump and sneak.
classes:
    Dino: This class contains the behaviour of the dino.
    Status: This class contains the status of the dino as an enum.
"""
from enum import Enum

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


class Dino:
    """This class contains the behaviour of the dino.
    The dino is the main character of the game and is controlled by the player.
    It can run, jump and sneak.
    Atributes:
        position: The vertical position of the dino.
        status: The status of the dino as an enum of the Status class.

    Methods:
        run: sets the dino parameters to running state.
        jump: sets the dino parameters to jumping state.
        sneak: sets the dino parameters to sneaking state.
        update: calls the specific method for the current state of the dino.
        check_collision: checks if the dino collides with an object.
    """
    def __init__(self) -> None:
        self.position: int = 20
        self.status: Status = Status.RUNNING


    def run(self) -> None:
        raise NotImplementedError("Subclasses must implement the run method.")

    def jump(self) -> None:
        raise NotImplementedError("Subclasses must implement the jump method.")

    def sneak(self) -> None:
        raise NotImplementedError("Subclasses must implement the sneak method.")

    def update(self) -> None:
        raise NotImplementedError("Subclasses must implement the update method.")

    def check_collision(self) -> bool:
        raise NotImplementedError("Subclasses must implement the check_collision method.")
