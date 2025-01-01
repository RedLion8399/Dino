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
    It is implemented as a singleton meaning that every reference
    to the Counter class returns the same instance. Consequently changing
    the attributes of one instance will change the attributes of all others as well.

    Attributes:
        frames: Counts the total frames passed in the game.
        highscore: The highscore from previous games. It's loaded from a file.
    """

    _innitialized: bool = False

    def __new__(cls):
        """Ensure that only one instance of the Counter class exists.

        Returns:
            Counter: In any casee an inctance of the Counter class is returned.
            If there is already an instance only the reference to this instance
            is returned. Otherwise a new instance is created and returned.
        """
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Initialize the Counter class and load the highscore from a file."""
        if self._innitialized:
            return
        self.frames: int = 0
        self.highscore: int = self.__load_highscore()

        self._cactus_counter: int = 0
        self._cloud_counter: int = 0

        self._innitialized = True

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

    def reset_obstacle_counter(self) -> None:
        """Set the current frame number when a new cactus is generated."""
        self._cactus_counter = self.frames

    def reset_cloud_counter(self) -> None:
        """Set the current frame number when a new cloud is generated."""
        self._cloud_counter = self.frames

    @property
    def cloud_counter(self) -> int:
        """Return the current frame number when a new cloud is generated."""
        return self.frames - self._cloud_counter

    @property
    def cactus_counter(self) -> int:
        """Return the current frame number when a new cactus is generated."""
        return self.frames - self._cactus_counter

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

    @property
    def bird_animation_status(self) -> bool:
        """Returns the animation status of the bird.

        While the bird is flying it has to different immages
        to change between in order to create a flying animation.
        The animation state changes every 40 frames.

        Returns:
            bool: The aimaton has only two states so it can be displayed
        """
        return self.frames % 40 < 20
