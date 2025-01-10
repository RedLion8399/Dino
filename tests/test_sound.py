# pylint: disable=missing-docstring

import unittest
from unittest.mock import MagicMock, patch

from sound import Sound


class TestSound(unittest.TestCase):
    @patch("pygame.mixer.init")
    @patch("sound.load_sound")
    def setUp(self, mock_load_sound, mock_mixer_init):  # type: ignore  # pylint: disable=unused-argument, arguments-differ # noqa: E501
        self.mock_sound = MagicMock()
        mock_load_sound.return_value = self.mock_sound
        self.sound = Sound()

    def test_play_check_point(self):
        self.sound.play_check_point()
        self.mock_sound.play.assert_called_once()

    def test_play_die(self):
        self.sound.play_die()
        self.mock_sound.play.assert_called_once()

    def test_play_jump(self):
        self.sound.play_jump()
        self.mock_sound.play.assert_called_once()
