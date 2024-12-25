"""This module contains the tests for the obstacles module."""
# pylint: disable=missing-docstring
import unittest
from obstacles import GameElement

class TestGameElement(unittest.TestCase):
    def test_init(self):
        game_element = GameElement(0, 0)
        self.assertEqual(game_element.x_position, 0)
        self.assertEqual(game_element.y_position, 0)
