"""This module contains the tests for the obstacles module."""

# pylint: disable=missing-docstring, no-member

import unittest

import pygame as pg

from config import config
from obstacles import Bird, Cactus, Cloud, GameElement, Ground


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
        game_element.OBJECT_SPEED = 9
        game_element.move()
        self.assertEqual(game_element.x_position, -9)

    def test_update(self):
        game_element = GameElement(0, 0)
        game_element.current_image = pg.Surface((100, 100))
        game_element.rect = pg.Rect(0, 0, 100, 100)
        game_element.OBJECT_SPEED = 5
        game_element.update()
        self.assertEqual(game_element.x_position, -5)
        self.assertEqual(game_element.y_position, 0)

    def test_update_kill(self):
        game_element = GameElement(0, 0)
        elements: pg.sprite.Group[GameElement] = pg.sprite.Group()  # type: ignore
        elements.add(game_element)
        game_element.current_image = pg.Surface((100, 100))
        game_element.rect = pg.Rect(0, 0, 100, 100)
        game_element.update()
        self.assertEqual(game_element.alive(), False)

    def test_update_alive(self):
        game_element = GameElement(100, 0)
        elements: pg.sprite.Group[GameElement] = pg.sprite.Group()  # type: ignore
        elements.add(game_element)
        game_element.current_image = pg.Surface((100, 100))
        game_element.rect = pg.Rect(0, 0, 100, 100)
        game_element.update()
        self.assertEqual(game_element.alive(), True)


class TestCactus(unittest.TestCase):
    def setUp(self) -> None:
        config.display_scale = (800, 300)
        config.caption = "Dino"
        config.background_color = pg.Color(255, 255, 255)
        config.init_screen()

    def test_init_position(self):
        cactus = Cactus()
        self.assertEqual(cactus.x_position, config.display_scale[0])
        self.assertEqual(cactus.y_position, 200)

    def test_init_images(self):
        cactus = Cactus()
        self.assertIsInstance(cactus.image_1, tuple)
        self.assertIsInstance(cactus.image_2, tuple)
        self.assertIsInstance(cactus.image_1[0], list)
        self.assertIsInstance(cactus.image_2[0], list)
        self.assertIsInstance(cactus.image_1[1], pg.Rect)
        self.assertIsInstance(cactus.image_2[1], pg.Rect)

    def test_random_image(self):
        cactus = Cactus()
        cactus.random_image()
        self.assertIsInstance(cactus.current_image, pg.Surface)
        self.assertIsInstance(cactus.rect, pg.Rect)


class TestBird(unittest.TestCase):
    def setUp(self) -> None:
        config.display_scale = (800, 300)
        config.caption = "Dino"
        config.background_color = pg.Color(255, 255, 255)
        config.init_screen()

    def test_init_position(self):
        bird = Bird()
        self.assertEqual(bird.x_position, config.display_scale[0])
        self.assertIn(bird.y_position, [75, 200])

    def test_init_images(self):
        bird = Bird()
        self.assertIsInstance(bird.image, tuple)


class TestCloud(unittest.TestCase):
    def setUp(self) -> None:
        config.display_scale = (800, 300)
        config.caption = "Dino"
        config.background_color = pg.Color(255, 255, 255)
        config.init_screen()

    def test_init_position(self):
        cloud = Cloud()
        self.assertEqual(cloud.x_position, config.display_scale[0])
        self.assertIn(cloud.y_position, range(50, 101))

    def test_init_images(self):
        cloud = Cloud()
        self.assertTrue(cloud.current_image)
        self.assertTrue(cloud.rect)


class TestGround(unittest.TestCase):
    def setUp(self) -> None:
        config.display_scale = (800, 300)
        config.caption = "Dino"
        config.background_color = pg.Color(255, 255, 255)
        config.init_screen()

    def test_init_position(self):
        ground = Ground()
        self.assertEqual(ground.x_position, config.display_scale[0])
        self.assertEqual(ground.y_position, config.display_scale[1])

    def test_init_images(self):
        ground = Ground()
        self.assertTrue(ground.immage_1)
        self.assertTrue(ground.immage_2)
        self.assertTrue(ground.rect_1)
        self.assertTrue(ground.rect_2)
