"""This module contains all about counters.
It's responsible for counting the players current score and sace and
load a highscore.

Classes:
    Counter: Containing the mian logic for counting the players score.
"""


class Counter:
    """The Counter class is responsible for counting the players score.
    It's needed because the score should be increased only every 3 frames.

    Attributes:
        score: The current score of the player.
        frame_counter: Counts the frames passing. It is set to 0 every 3 frames.
    """

    def __init__(self) -> None:
        self.score: int = 0
        self.frame_counter: int = 0

    def count(self) -> int:
        """This method is responsible for counting the players score.
        It increases the score by one every 3 frames.

        Returns:
            int: The current score of the player.
        """
        self.frame_counter += 1
        if self.frame_counter == 3:
            self.score += 1
            self.frame_counter = 0
        return self.score

    def __int__(self) -> int:
        """This method returns the current score of the player."""
        return self.score
