"""This module contains the tests for the obstacles module."""
# pylint: disable=missing-docstring, no-member
import unittest
import pygame as pg
from obstacles import GameElement, Cactus

class TestGameElement(unittest.TestCase):
    def test_init(self):
        game_element = GameElement(0, 0)
        self.assertEqual(game_element.x_position, 0)
        self.assertEqual(game_element.y_position, 0)


class TestCactus(unittest.TestCase):
    def setUp(self) -> None:
        pg.init()
        pg.display.set_mode((800, 600))

    def test_init_position(self):
        cactus = Cactus(0, 0)
        self.assertEqual(cactus.x_position, 0)
        self.assertEqual(cactus.y_position, 0)

    def test_init_images(self):
        cactus = Cactus(0, 0)
        self.assertIsInstance(cactus.image_1, tuple)
        self.assertIsInstance(cactus.image_2, tuple)
        self.assertIsInstance(cactus.image_1[0], list)
        self.assertIsInstance(cactus.image_2[0], list)
        self.assertIsInstance(cactus.image_1[1], pg.Rect)
        self.assertIsInstance(cactus.image_2[1], pg.Rect)
