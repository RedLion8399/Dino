from enum import Enum

class Status(Enum):
    """This class contains the status of the dino.
    The status displays the current state of the dino.
    """
    RUNNING = 1
    JUMPING = 2
    SNEAKING = 3


class Dino:
    """This class contains the behaviour of the dino."""
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
