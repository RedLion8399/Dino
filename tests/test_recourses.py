"""This module contains the tests for the recources module."""
# pylint: disable=missing-function-docstring, missing-class-docstring
# pylint: disable=no-member, unused-variable
import unittest
import pygame as pg
from recourses import load_image, load_sound, seperate_images

class TestLoadImage(unittest.TestCase):
    def setUp(self) -> None:
        """Initialize the pygame module and create a display surface for the tests."""
        pg.init()
        pg.display.set_mode((100, 100))

    def test_load_image_error(self) -> None:
        with self.assertRaises(SystemExit):
            load_image("not_found.png")

    def test_load_image(self) -> None:
        image: pg.Surface = load_image("birds.png")
        self.assertIsInstance(image, pg.Surface)

    def test_load_image_colorkey(self) -> None:
        image: pg.Surface = load_image("birds.png")
        self.assertEqual(image.get_at((1, 1)), (0, 0, 0, 0))

class TestSeperateImages(unittest.TestCase):
    def setUp(self) -> None:
        """Initialize the pygame module and create a display surface for the tests."""
        pg.init()
        pg.display.set_mode((100, 100))
    def test_seperate_images(self) -> None:
        image: pg.Surface = load_image("birds.png")
        images: list[pg.Surface] = seperate_images(image, (2, 1))
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
