"""This module contains the tests for the dino module."""
# pylint: disable=no-member
# pylint: disable=missing-function-docstring

import unittest
import pygame as pg
from dino import Dino, Status

class TestDino(unittest.TestCase):
    """This class contains the tests for the Dino class."""

    def test_init(self) -> None:
        """This function tests the initialization of the Dino class."""
        dino: Dino = Dino()
        self.assertEqual(dino.y_position, 20)
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


class TestStatus(unittest.TestCase):
    """This class contains the tests for the Status class."""

    def test_values(self) -> None:
        """This function tests the initialization of the Status class."""
        self.assertEqual(Status.RUNNING.value, 1)
        self.assertEqual(Status.JUMPING.value, 2)
        self.assertEqual(Status.SNEAKING.value, 3)
