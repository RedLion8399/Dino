"""This module contains the tests for the config module."""
# pylint: disable=missing-docstring

import unittest
from config import config, Config, ColorTheme

class TestConfig(unittest.TestCase):
    def test_values(self):
        config.display_scale = (800, 600)
        config.caption = "Dino"
        self.assertEqual(config.color_theme, ColorTheme.LIGHT_GRAY)
        self.assertEqual(config.display_scale, (800, 600))
        self.assertEqual(config.caption, "Dino")

    def test_singleton(self):
        new_config: Config = Config()
        self.assertEqual(config, new_config)


class TestColorTheme(unittest.TestCase):
    def test_values(self):
        self.assertEqual(ColorTheme.LIGHT_GRAY.value, "light_gray")
        self.assertEqual(ColorTheme.LIGHT_GRAY.name, "LIGHT_GRAY")
