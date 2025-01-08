# type: ignore
# pylint: disable=missing-docstring, no-member
import unittest
import pygame as pg
from score import Score
from unittest.mock import Mock, patch


class TestScore(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.score = Score()
        self.score.counter = Mock()

    def test_split_number(self):
        test_cases: list[tuple[int, list[int]]]
        test_cases = [
            (0, [0, 0, 0, 0, 0]),
            (1, [0, 0, 0, 0, 1]),
            (123, [0, 0, 1, 2, 3]),
            (12345, [1, 2, 3, 4, 5]),
        ]

        for input_num, expected in test_cases:
            with self.subTest(input_num=input_num):
                result = self.score.split_number(input_num)
                self.assertEqual(result, expected)

    @patch("score.config")
    def test_display_highscore(self, mock_config):
        self.score.counter.highscore = 12345
        self.score.display_highscore()
        self.assertEqual(mock_config.window.blit.call_count, 7)

    @patch("score.config")
    def test_update(self, mock_config):
        self.score.counter.score = 12345
        self.score.update()
        self.assertEqual(mock_config.window.blit.call_count, 5)


if __name__ == "__main__":
    unittest.main()
