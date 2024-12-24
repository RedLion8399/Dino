"""This module contains the tests for the recources module."""
# pylint: disable=missing-function-docstring, missing-class-docstring
import unittest
import pygame as pg
from recourses import load_image, load_sound, seperate_images

class TestLoadImage(unittest.TestCase):
    def setUp(self) -> None:
        """Initialize the pygame module and create a display surface for the tests."""
        pg.init()
        screen: pg.Surface = pg.display.set_mode((100, 100))

    def test_load_image_error(self) -> None:
        with self.assertRaises(SystemExit):
            load_image("light_gray", "not_found.png")

    def test_load_image(self) -> None:
        image: pg.Surface = load_image("light_gray", "birds.png")
        self.assertIsInstance(image, pg.Surface)

    def test_load_image_colorkey(self) -> None:
        image: pg.Surface = load_image("light_gray", "birds.png")
        self.assertEqual(image.get_at((1, 1)), (0, 0, 0, 0))

class TestSeperateImages(unittest.TestCase):
    def setUp(self) -> None:
        """Initialize the pygame module and create a display surface for the tests."""
        pg.init()
        screen: pg.Surface = pg.display.set_mode((100, 100))
    def test_seperate_images(self) -> None:
        image: pg.Surface = load_image("light_gray", "birds.png")
        images: list[pg.Surface] = seperate_images(image, (2, 1))
        self.assertEqual(len(images), 2)
