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
        highscore: The highscore from previous games. It's loaded from a file.

    Methods:
        count: Increases the score by one every 3 frames.
        save_highscore: Saves the current highscore to a file.
        __int__: Returns the current score of the player.
    """

    def __init__(self) -> None:
        """Initialize the Counter class and load the highscore from a file."""
        self.frames: int = 0
        self.highscore: int = self.__load_highscore()

    def save_highscore(self) -> None:
        """This method saves the current highscore to a file."""
        if self.score > self.highscore:
            self.highscore = self.score
        with open("highscore.txt", "w", encoding="utf-8") as file:
            file.write(str(self.highscore))

    def __load_highscore(self) -> int:
        """This method loads the highscore from a file.
        If the file does not exist, it returns 0.

        Raises:
            FileNotFoundError: If the file does not exist.

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
