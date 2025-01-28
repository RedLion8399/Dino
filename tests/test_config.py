# pylint: disable=missing-docstring, unused-argument

"""This module contains the tests for the config module."""


import unittest
from unittest.mock import MagicMock, patch

from config import ColorTheme, Config, config


class TestConfig(unittest.TestCase):

    @patch("config.pg")
    def test_values(self, mock_pg: MagicMock):
        config.display_scale = (800, 600)
        config.caption = "Dino"
        self.assertEqual(config.color_theme, ColorTheme.LIGHT_GRAY)
        self.assertEqual(config.display_scale, (800, 600))
        self.assertEqual(config.caption, "Dino")
        self.assertEqual(config.object_speed, 0)

    @patch("config.pg")
    def test_singleton(self, mock_pg: MagicMock):
        new_config: Config = Config()
        self.assertEqual(config, new_config)


class TestColorTheme(unittest.TestCase):
    def test_values(self):
        self.assertEqual(ColorTheme.LIGHT_GRAY.value, "light_gray")
        self.assertEqual(ColorTheme.LIGHT_GRAY.name, "LIGHT_GRAY")
