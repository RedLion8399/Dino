# type: ignore
# pylint: disable=missing-docstring, no-member, disable=protected-access
import unittest
from unittest.mock import Mock, patch

import pygame as pg

from config import config
from score import Score


class TestScore(unittest.TestCase):
    def setUp(self):
        config.display_scale = (800, 600)
        config.caption = "Dino"
        config.background_color = pg.Color(255, 255, 255)
        config.init_game()

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
        self.score._display_highscore()
        self.assertEqual(mock_config.window.blit.call_count, 7)

    @patch("score.config")
    def test_update(self, mock_config):
        self.score.counter.highscore = 23456
        self.score.counter.score = 12345
        self.score.update()
        self.assertEqual(mock_config.window.blit.call_count, 12)

    @patch("score.config")
    def test_display_characters(self, mock_config):
        mock_config.display_scale = (800, 600)
        test_characters = [1, 2, 3]
        test_position = 100

        self.score._display_characters(test_position, test_characters)

        self.assertEqual(mock_config.window.blit.call_count, 3)
