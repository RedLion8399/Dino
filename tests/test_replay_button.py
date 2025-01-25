# pylint: disable=missing-docstring, no-member

import unittest

import pygame as pg

from config import config
from game_elements.replay_button import ReplayButton


class TestReplayButton(unittest.TestCase):
    def setUp(self):
        config.display_scale = (800, 600)
        config.caption = "Dino"
        config.background_color = pg.Color(255, 255, 255)
        config.object_speed = 10
        config.init_game()
        self.replay_button = ReplayButton()

    def test_init(self):
        self.assertEqual(self.replay_button.OBJECT_SPEED, 0)
        self.assertEqual(
            self.replay_button.position_rect.center,
            (config.display_scale[0] // 2, config.display_scale[1] // 2),
        )

    def test_update(self):
        """Just verify update runs without errors"""
        self.replay_button.update()

    def test_replay_without_click(self):
        # Mock event queue with no clicks
        pg.event.get = lambda: [pg.event.Event(pg.QUIT)]
        with self.assertRaises(SystemExit):
            self.replay_button.replay(lambda: None)
