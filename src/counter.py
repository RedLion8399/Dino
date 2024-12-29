"""This module contains all about counters.
It's responsible for counting the players current score and sace and
load a highscore.

Classes:
    Counter: Containing the mian logic for counting the players score.
"""


class Counter:
    """Count the different game scores.

    The Counter class is responsible for counting the global score.
    From this scre many different subscores can be calculated.

    Attributes:
        frames: Counts the total frames passed in the game.
        highscore: The highscore from previous games. It's loaded from a file.
    """

    def __init__(self) -> None:
        """Initialize the Counter class and load the highscore from a file."""
        self.frames: int = 0
        self.highscore: int = self.__load_highscore()

    def save_highscore(self) -> None:
        """This method saves the current highscore to a file.

        The higscore is only saved if the current score is higher
        than the previous highscore.
        """
        if self.score > self.highscore:
            self.highscore = self.score
        with open("highscore.txt", "w", encoding="utf-8") as file:
            file.write(str(self.highscore))

    def __load_highscore(self) -> int:
        """This method loads the highscore from a file.
        If the file does not exist, it returns 0.

        Returns:
            int: The highscore feom previous games.
        """
        try:
            with open("highscore.txt", "r", encoding="utf-8") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def tick(self) -> None:
        """Increase the frame counter by one every time this method is called."""
        self.frames += 1

    @property
    def score(self) -> int:
        """This method returns the current score of the player."""
        return self.frames // 3

    @property
    def dino_running_status(self) -> bool:
        """Returns the animation status of the dino.

        While the Dino is running or sneaking it has to different immages
        to change between in order to create a running animation.
        The animation state changes every 20 frames.

        Returns:
            bool: The aimaton has only two states so it can be displayed
            as a boolean. It is irrelevant wich state belongs to wich image
            and can be difined by the user.
        """
        return self.frames % 20 < 10
