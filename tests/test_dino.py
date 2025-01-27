# pylint: disable=missing-docstring, disable=no-member, disable=protected-access, disable=unused-argument, disable=undefined-variable  # noqa: E501
# type: ignore


import unittest
from unittest.mock import MagicMock, call, patch

import pygame as pg

from config import config
from game_elements import Dino, GameElement, Status


class TestDino(unittest.TestCase):

    @patch.object(config, "display_scale", (800, 300))  # noqa: F821
    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test_init(
        self,
        mock_sound: MagicMock,
        mock_seperate: MagicMock,
        mock_load_image: MagicMock,
        mock_load: MagicMock,
    ) -> None:
        """This function tests the initialization of the Dino class."""
        dino: Dino = Dino()

        mock_sound.assert_called_once()
        self.assertEqual(mock_load.call_count, 2)
        self.assertEqual(mock_seperate.call_count, 2)

        self.assertEqual(dino.y_position, 300)
        self.assertEqual(dino.x_position, 200)

        self.assertEqual(dino.status, Status.RUNNING)

    # The following functions tests the process_input method of the Dino class.
    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test_process_input_from_running_to_jumping(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        event: pg.event.Event = pg.event.Event(pg.KEYDOWN, key=pg.K_UP)
        dino.process_input(event)
        self.assertEqual(dino.status, Status.JUMPING)

        dino.status = Status.RUNNING
        event: pg.event.Event = pg.event.Event(pg.KEYDOWN, key=pg.K_SPACE)
        dino.process_input(event)
        self.assertEqual(dino.status, Status.JUMPING)

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test_process_input_from_running_to_sneaking(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        event: pg.event.Event = pg.event.Event(pg.KEYDOWN, key=pg.K_DOWN)
        dino.process_input(event)
        self.assertEqual(dino.status, Status.SNEAKING)

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test_process_input_from_jumping_to_running(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        event: pg.event.Event = pg.event.Event(pg.KEYUP, key=pg.K_UP)
        dino.status = Status.JUMPING
        dino.process_input(event)
        self.assertEqual(dino.status, Status.JUMPING)

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test_process_input_from_sneaking_to_running(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        event: pg.event.Event = pg.event.Event(pg.KEYUP, key=pg.K_DOWN)
        dino.status = Status.SNEAKING
        dino.process_input(event)
        self.assertEqual(dino.status, Status.RUNNING)

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test_process_input_from_jumping_to_sneaking(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        event: pg.event.Event = pg.event.Event(pg.KEYDOWN, key=pg.K_DOWN)
        dino.status = Status.JUMPING
        dino.process_input(event)
        self.assertEqual(dino.status, Status.JUMPING)

    @patch("pygame.image.load")
    @patch("game_elements.dino.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test_load_images(
        self,
        mock_sound: MagicMock,
        mock_seperate: MagicMock,
        mock_load_image: MagicMock,
        mock_load: MagicMock,
    ) -> None:

        mock_load_image.side_effect = [["mock_surface_1"], ["mock_surface_2"]]

        Dino()
        self.assertEqual(mock_load_image.call_count, 2)
        self.assertEqual(mock_seperate.call_count, 2)
        mock_load_image.assert_has_calls(
            [
                call("dino_running.png"),
                call("dino_sneaking.png"),
            ]
        )

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test__run(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        dino.status = Status.RUNNING
        dino._run()
        self.assertEqual(dino.position_rect, dino.running_image[1])
        self.assertEqual(dino.current_image, dino.running_image[0][2])
        for _ in range(12):
            dino.counter.tick()
            dino._run()
        self.assertEqual(dino.current_image, dino.running_image[0][3])

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test__jump_animation(self, *args: MagicMock) -> None:

        dino: Dino = Dino()
        dino.status = Status.JUMPING
        dino._jump()
        self.assertEqual(dino.position_rect, dino.running_image[1])
        self.assertEqual(dino.current_image, dino.running_image[0][0])

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test__jump_calculations(self, *args: MagicMock) -> None:
        """Test only the jump for a single frame."""
        dino: Dino = Dino()
        dino.status = Status.JUMPING
        initial_y = dino.y_position
        initial_velocity = dino.jump_velocity

        dino._jump()
        self.assertEqual(dino.y_position, initial_y + initial_velocity)
        self.assertEqual(dino.jump_velocity, initial_velocity + dino.GRAVITY)

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    @patch("game_elements.GameElement.update")
    def test_jump_landing(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        dino.status = Status.JUMPING
        for _ in range(200):
            dino.update()
        self.assertEqual(dino.y_position, dino.DEFAULT_POSITION[1])

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test__sneak_animation(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        dino.status = Status.SNEAKING
        dino._sneak()
        self.assertEqual(dino.position_rect, dino.sneaking_image[1])
        self.assertEqual(dino.current_image, dino.sneaking_image[0][1])
        for _ in range(15):
            dino.counter.tick()
            dino._sneak()
        self.assertEqual(dino.current_image, dino.sneaking_image[0][0])

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    @patch("game_elements.GameElement.update")
    def test_update_animations(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        dino.status = Status.JUMPING
        dino.update()
        self.assertEqual(dino.current_image, dino.running_image[0][0])

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    @patch("game_elements.GameElement.update")
    def test_check_collision_false(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        dino.update()
        dino.hitbox = pg.Rect(0, 0, 10, 10)

        non_colliding: GameElement = GameElement(500, 200)
        non_colliding.hitbox = pg.Rect(500, 200, 50, 50)
        self.assertFalse(dino.check_collision([non_colliding]))

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    @patch("game_elements.GameElement.update")
    def test_check_collision_true(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        dino.update()
        dino.hitbox = pg.Rect(0, 0, 10, 10)

        colliding: GameElement = GameElement(dino.x_position, dino.y_position)
        colliding.hitbox: pg.Rect = pg.Rect(dino.hitbox.topleft, dino.hitbox.size)
        self.assertTrue(dino.check_collision([colliding]))

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    @patch("game_elements.GameElement.update")
    def test_check_collision_multiple(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        dino.update()
        dino.hitbox = pg.Rect(0, 0, 10, 10)

        non_colliding: GameElement = GameElement(500, 200)
        non_colliding.hitbox = pg.Rect(500, 200, 50, 50)

        colliding: GameElement = GameElement(dino.x_position, dino.y_position)
        colliding.hitbox: pg.Rect = pg.Rect(dino.hitbox.topleft, dino.hitbox.size)

        obstacles: list[GameElement] = [non_colliding, colliding]
        self.assertTrue(dino.check_collision(obstacles))

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    @patch("game_elements.GameElement.update")
    def test_check_collision_empty_list(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        dino.update()
        self.assertFalse(dino.check_collision([]))


class TestStatus(unittest.TestCase):
    def test_values(self) -> None:
        """This function tests the initialization of the Status class."""
        self.assertEqual(Status.RUNNING.value, 1)
        self.assertEqual(Status.JUMPING.value, 2)
        self.assertEqual(Status.SNEAKING.value, 3)

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test_check_collision_with_no_intersection(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        dino.hitbox = pg.Rect(0, 0, 10, 10)

        obstacle = GameElement(100, 100)
        obstacle.hitbox = pg.Rect(100, 100, 10, 10)

        self.assertFalse(dino.check_collision([obstacle]))

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test_check_collision_with_intersection(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        dino.hitbox = pg.Rect(0, 0, 10, 10)

        obstacle = GameElement(5, 5)
        obstacle.hitbox = pg.Rect(5, 5, 10, 10)

        self.assertTrue(dino.check_collision([obstacle]))

    @patch("pygame.image.load")
    @patch("recourses.load_image")
    @patch("game_elements.dino.seperate_images")
    @patch("game_elements.dino.Sound")
    def test_check_collision_with_multiple_obstacles(self, *args: MagicMock) -> None:
        dino: Dino = Dino()
        dino.hitbox = pg.Rect(0, 0, 10, 10)

        obstacle1 = GameElement(100, 100)
        obstacle1.hitbox = pg.Rect(100, 100, 10, 10)

        obstacle2 = GameElement(5, 5)
        obstacle2.hitbox = pg.Rect(5, 5, 10, 10)

        self.assertTrue(dino.check_collision([obstacle1, obstacle2]))
