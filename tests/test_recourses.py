"""This module contains the tests for the recources module."""

# pylint: disable=missing-function-docstring, missing-class-docstring
# pylint: disable=no-member, unused-variable

import unittest
import os
import pygame as pg
from recourses import load_image, load_sound, seperate_images, full_path


class TestLoadImage(unittest.TestCase):
    def setUp(self) -> None:
        """Initialize the pygame module and create a display surface for the tests."""
        pg.init()
        pg.display.set_mode((100, 100))

    def test_load_image_error(self) -> None:
        with self.assertRaises(SystemExit):
            load_image("not_found.png")

    def test_load_image(self) -> None:
        image: tuple[pg.Surface, pg.Rect] = load_image("birds.png")
        self.assertIsInstance(image, tuple)
        self.assertIsInstance(image[0], pg.Surface)
        self.assertIsInstance(image[1], pg.Rect)

    def test_load_image_colorkey(self) -> None:
        image: tuple[pg.Surface, pg.Rect] = load_image("birds.png")
        self.assertEqual(image[0].get_at((1, 1)), (0, 0, 0, 0))


class TestSeperateImages(unittest.TestCase):
    def setUp(self) -> None:
        """Initialize the pygame module and create a display surface for the tests."""
        pg.init()
        pg.display.set_mode((100, 100))

    def test_seperate_images(self) -> None:
        image: tuple[pg.Surface, pg.Rect] = load_image("birds.png")
        images: tuple[list[pg.Surface], pg.Rect] = seperate_images(image[0], (2, 1))
        self.assertEqual(len(images), 2)


class TestLoadSound(unittest.TestCase):
    def setUp(self) -> None:
        """Initialize the pygame module and create a display surface for the tests."""
        pg.mixer.init()

    def test_load_sound_error(self) -> None:
        with self.assertRaises(SystemExit):
            load_sound("not_found.wav")

    def test_load_sound(self) -> None:
        sound: pg.mixer.Sound = load_sound("die.wav")
        self.assertIsInstance(sound, pg.mixer.Sound)


class TestFullPath(unittest.TestCase):

    def test_full_path_image(self) -> None:
        path: str = full_path("birds.png", True)
        self.assertTrue(os.path.exists(path))

    def test_full_path_sound(self) -> None:
        path: str = full_path("die.wav")
        self.assertTrue(os.path.exists(path))
