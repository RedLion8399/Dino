# pylint: disable=missing-docstring, disable=no-member, disable=protected-access
# type: ignore

import unittest

import pygame as pg

from config import config
from dino import Dino, Status
from obstacles import GameElement


class TestDino(unittest.TestCase):
    def setUp(self) -> None:
        config.display_scale = (800, 200)
        config.caption = "Dino"
        config.background_color = pg.Color(255, 255, 255)
        config.init_screen()

    def test_init(self) -> None:
        """This function tests the initialization of the Dino class."""
        dino: Dino = Dino()
        self.assertEqual(dino.y_position, 200)
        self.assertEqual(dino.x_position, 200)
        self.assertEqual(dino.status, Status.RUNNING)

    # The following functions tests the process_input method of the Dino class.
    def test_process_input_from_running_to_jumping(self) -> None:
        dino: Dino = Dino()
        event: pg.event.Event = pg.event.Event(pg.KEYDOWN, key=pg.K_UP)
        dino.process_input(event)
        self.assertEqual(dino.status, Status.JUMPING)

        dino.status = Status.RUNNING
        event: pg.event.Event = pg.event.Event(pg.KEYDOWN, key=pg.K_SPACE)
        dino.process_input(event)
        self.assertEqual(dino.status, Status.JUMPING)

    def test_process_input_from_running_to_sneaking(self) -> None:
        dino: Dino = Dino()
        event: pg.event.Event = pg.event.Event(pg.KEYDOWN, key=pg.K_DOWN)
        dino.process_input(event)
        self.assertEqual(dino.status, Status.SNEAKING)

    def test_process_input_from_jumping_to_running(self) -> None:
        dino: Dino = Dino()
        event: pg.event.Event = pg.event.Event(pg.KEYUP, key=pg.K_UP)
        dino.status = Status.JUMPING
        dino.process_input(event)
        self.assertEqual(dino.status, Status.JUMPING)

    def test_process_input_from_sneaking_to_running(self) -> None:
        dino: Dino = Dino()
        event: pg.event.Event = pg.event.Event(pg.KEYUP, key=pg.K_DOWN)
        dino.status = Status.SNEAKING
        dino.process_input(event)
        self.assertEqual(dino.status, Status.RUNNING)

    def test_process_input_from_jumping_to_sneaking(self) -> None:
        dino: Dino = Dino()
        event: pg.event.Event = pg.event.Event(pg.KEYDOWN, key=pg.K_DOWN)
        dino.status = Status.JUMPING
        dino.process_input(event)
        self.assertEqual(dino.status, Status.JUMPING)

    def test_load_images(self) -> None:
        dino: Dino = Dino()
        self.assertIsInstance(dino.running_image, tuple)
        self.assertIsInstance(dino.sneaking_image, tuple)

    def test__run(self) -> None:
        dino: Dino = Dino()
        dino.status = Status.RUNNING
        dino._run()
        self.assertEqual(dino.rect, dino.running_image[1])
        self.assertEqual(dino.current_image, dino.running_image[0][2])
        for _ in range(12):
            dino.counter.tick()
            dino._run()
        self.assertEqual(dino.current_image, dino.running_image[0][3])

    def test__jump_animation(self) -> None:
        dino: Dino = Dino()
        dino.status = Status.JUMPING
        dino._jump()
        self.assertEqual(dino.rect, dino.running_image[1])
        self.assertEqual(dino.current_image, dino.running_image[0][0])

    def test__jump_movement(self) -> None:
        """This function tests the movement of the Dino when it is jumping.

        While jumping the position values are mostly unknown
        wich makes testing difficult. This function tests only if the Dino
        returns to the ground after the jump under known conditions.
        """
        dino: Dino = Dino()
        dino.status = Status.JUMPING
        dino.DEFAULT_VELOCITY = -15
        self.assertEqual(dino.y_position, dino.DEFAULT_POSITION[1])
        for _ in range(40):
            dino.counter.tick()
            dino.update()
        self.assertEqual(dino.y_position, dino.DEFAULT_POSITION[1])
        self.assertEqual(dino.status, Status.RUNNING)

    def test__sneak_animation(self) -> None:
        dino: Dino = Dino()
        dino.status = Status.SNEAKING
        dino._sneak()
        self.assertEqual(dino.rect, dino.sneaking_image[1])
        self.assertEqual(dino.current_image, dino.sneaking_image[0][0])
        for _ in range(12):
            dino.counter.tick()
            dino._sneak()
        self.assertEqual(dino.current_image, dino.sneaking_image[0][1])

    def test_update_animations(self) -> None:
        dino: Dino = Dino()
        dino.status = Status.JUMPING
        dino.update()
        self.assertEqual(dino.current_image, dino.running_image[0][0])

    def test_check_collision_false(self) -> None:
        dino: Dino = Dino()
        dino.update()
        non_colliding = GameElement(500, 200)
        non_colliding.rect = pg.Rect(500, 200, 50, 50)
        self.assertFalse(dino.check_collision([non_colliding]))

    def test_check_collision_true(self) -> None:
        dino: Dino = Dino()
        dino.update()
        colliding = GameElement(200, 200)
        colliding.rect = pg.Rect(200, 200, 50, 50)
        self.assertTrue(dino.check_collision([colliding]))

    def test_check_collision_multiple(self) -> None:
        dino: Dino = Dino()
        dino.update()
        non_colliding: GameElement = GameElement(500, 200)
        non_colliding.rect = pg.Rect(500, 200, 50, 50)
        colliding = GameElement(200, 200)
        colliding.rect = pg.Rect(200, 200, 50, 50)
        obstacles: list[GameElement] = [non_colliding, colliding]
        self.assertTrue(dino.check_collision(obstacles))

    def test_check_collision_empty_list(self) -> None:
        dino: Dino = Dino()
        dino.update()
        self.assertFalse(dino.check_collision([]))


class TestStatus(unittest.TestCase):
    def test_values(self) -> None:
        """This function tests the initialization of the Status class."""
        self.assertEqual(Status.RUNNING.value, 1)
        self.assertEqual(Status.JUMPING.value, 2)
        self.assertEqual(Status.SNEAKING.value, 3)
