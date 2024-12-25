"""This module contains the tests for the obstacles module."""
# pylint: disable=missing-docstring, no-member
import unittest
import pygame as pg
from obstacles import GameElement, Cactus
from config import config

class TestGameElement(unittest.TestCase):
    def setUp(self) -> None:
        config.display_scale = (800, 600)
        config.caption = "Dino"
        config.init_screen()

    def test_init(self):
        game_element = GameElement(0, 0)
        self.assertEqual(game_element.x_position, 0)
        self.assertEqual(game_element.y_position, 0)
    
    def test_move(self):
        game_element = GameElement(0, 0)
        game_element.move(9)
        self.assertEqual(game_element.x_position, -9)

    def test_update(self):
        game_element = GameElement(0, 0)
        game_element.current_image = pg.Surface((100, 100))
        game_element.rect = pg.Rect(0, 0, 100, 100)
        game_element.update(5)
        self.assertEqual(game_element.x_position, -5)
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
