"""This module contains the tests for the counter module"""

import unittest
from math import floor
from random import randint
from counter import Counter

class TestCounter(unittest.TestCase):
    """This class contains the tests for the Counter class."""

    def test_init(self) -> None:
        """This function tests the initialization of the Counter class."""
        counter: Counter = Counter()
        self.assertEqual(counter.score, 0)
        self.assertEqual(counter.frame_counter, 0)
    
    def test_count_simple(self) -> None:
        """This function tests the count method of the Counter class."""
        counter: Counter = Counter()
        for _ in range(3):
            counter.count()
        self.assertEqual(counter.score, 1)
        self.assertEqual(counter.frame_counter, 0)

    def test_count_multiple(self) -> None:
        """This function tests the count method of the Counter class."""
        for _ in range(20):
            counter: Counter = Counter()
            random_number: int = randint(1, 100)
            for _ in range(random_number):
                counter.count()
            self.assertEqual(counter.score, floor(random_number / 3))
