# pylint: disable=missing-docstring, disable=no-member, disable=protected-access
# type: ignore

import unittest

import pygame as pg

from config import config
from dino import Dino, Status


class TestDino(unittest.TestCase):
    def setUp(self) -> None:
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

    def test__jump(self) -> None:
        dino: Dino = Dino()
        dino.status = Status.JUMPING
        dino._jump()
        self.assertEqual(dino.rect, dino.running_image[1])
        self.assertEqual(dino.current_image, dino.running_image[0][0])

    def test__sneak(self) -> None:
        dino: Dino = Dino()
        dino.status = Status.SNEAKING
        dino._sneak()
        self.assertEqual(dino.rect, dino.sneaking_image[1])
        self.assertEqual(dino.current_image, dino.sneaking_image[0][0])
        for _ in range(12):
            dino.counter.tick()
            dino._sneak()
        self.assertEqual(dino.current_image, dino.sneaking_image[0][1])

    def test_update(self) -> None:
        dino: Dino = Dino()
        dino.status = Status.JUMPING
        dino.update()
        self.assertEqual(dino.current_image, dino.running_image[0][0])


class TestStatus(unittest.TestCase):
    def test_values(self) -> None:
        """This function tests the initialization of the Status class."""
        self.assertEqual(Status.RUNNING.value, 1)
        self.assertEqual(Status.JUMPING.value, 2)
        self.assertEqual(Status.SNEAKING.value, 3)
