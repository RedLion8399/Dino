"""This module contains the tests for the dino module."""

import unittest
from dino import Dino, Status

class TestDino(unittest.TestCase):
    """This class contains the tests for the Dino class."""

    def test_init(self) -> None:
        """This function tests the initialization of the Dino class."""
        dino: Dino = Dino()
        self.assertEqual(dino.position, 20)
        self.assertEqual(dino.status, Status.RUNNING)


class TestStatus(unittest.TestCase):
    """This class contains the tests for the Status class."""

    def test_values(self) -> None:
        """This function tests the initialization of the Status class."""
        self.assertEqual(Status.RUNNING, 1)
        self.assertEqual(Status.JUMPING, 2)
        self.assertEqual(Status.SNEAKING, 3)
