# pylint: disable=protected-access, missing-docstring

import unittest
from random import randint

from counter import Counter

# Some of the tests are testing private methods, which is not recommended.
# However, the tests are necessary to ensure the correct functionality of the
# class. This results in the hard readable syntax of some tests, like:
# counter._Counter__load_highscore()


class TestCounter(unittest.TestCase):
    def test_init(self) -> None:
        """This function tests the initialization of the Counter class."""
        counter: Counter = Counter()
        self.assertEqual(counter.frames, 0)

    def test_singleton(self) -> None:
        """This function tests the singleton property of the Counter class."""
        counter1: Counter = Counter()
        counter2: Counter = Counter()
        self.assertEqual(counter1, counter2)

    def test_count_simple(self) -> None:
        """This function tests the count method of the Counter class."""
        counter: Counter = Counter()
        for _ in range(3):
            counter.tick()
        self.assertEqual(counter.score, 1)
        self.assertEqual(counter.frames, 3)

    def test_count_multiple(self) -> None:
        """This function tests the count method of the Counter class."""
        for _ in range(20):
            counter: Counter = Counter()
            random_number: int = randint(1, 100)
            for _ in range(random_number):
                counter.tick()
            self.assertEqual(counter.score, random_number // 3)

    def test_save_highscore(self) -> None:
        """This function tests the save_highscore method of the Counter class."""
        with open("highscore.txt", "w", encoding="utf-8") as file:
            file.write("0")
        counter: Counter = Counter()
        counter.save_highscore()
        with open("highscore.txt", "r", encoding="utf-8") as file:
            self.assertEqual(int(file.read()), counter.highscore)

    def test_load_random_highscore(self) -> None:
        """This function tests the load_highscore method of the Counter class."""
        with open("highscore.txt", "w", encoding="utf-8") as file:
            file.write("0")
        counter: Counter = Counter()
        random_score: int = randint(1, 100)
        counter.highscore = random_score
        counter.save_highscore()
        counter._Counter__load_highscore()  # type: ignore
        counter._Counter__load_highscore()  # type: ignore
        self.assertEqual(counter.highscore, random_score)

    def test_load_highscore(self) -> None:
        """This function tests the load_highscore method of the Counter class."""
        with open("highscore.txt", "w", encoding="utf-8") as file:
            file.write("0")
        counter: Counter = Counter()
        self.assertEqual(counter.highscore, 0)
        counter.highscore = 100
        counter.save_highscore()
        counter._Counter__load_highscore()  # type: ignore
        counter._Counter__load_highscore()  # type: ignore
        self.assertEqual(counter.highscore, 100)

    def test_save_highscore_if_higher(self) -> None:
        """This function tests the save_highscore method of the Counter class."""
        with open("highscore.txt", "w", encoding="utf-8") as file:
            file.write("0")
        counter: Counter = Counter()
        for _ in range(300):
            counter.tick()
        counter.save_highscore()
        with open("highscore.txt", "r", encoding="utf-8") as file:
            self.assertEqual(int(file.read()), 100)

    def test_save_highscore_if_lower(self) -> None:
        """This function tests the save_highscore method of the Counter class."""
        with open("highscore.txt", "w", encoding="utf-8") as file:
            file.write("55")
        counter: Counter = Counter()
        for _ in range(99):
            counter.tick()
        counter.save_highscore()
        with open("highscore.txt", "r", encoding="utf-8") as file:
            self.assertEqual(int(file.read()), 55)

    def test_dino_running_status(self):
        counter: Counter = Counter()
        self.assertTrue(counter.dino_running_status)
        for _ in range(12):
            counter.tick()
        self.assertFalse(counter.dino_running_status)
