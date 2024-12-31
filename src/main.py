"""The main module contains the main functionality of the programm.

It is the file, meant to be called directly to playthe game.
It initializes the grafics as well as controlls the main game functionalitys
defined in other modules.
"""

# pylint: disable=no-member

import random as rd
import sys

import pygame as pg

from config import ColorTheme, config
from counter import Counter
from dino import Dino
from obstacles import Bird, Cactus, Cloud, GameElement, Ground


def main() -> None:
    """This is the main function of the programm.
    It is the place were every functionality is stticked together.
    It initializes the game, runs it displays changes and checks for kollisiions.
    """

    config.color_theme = ColorTheme.LIGHT_GRAY
    config.display_scale = (800, 300)
    config.caption = "Dino"
    config.background_color = pg.Color(255, 255, 255)
    config.object_speed = 7
    config.frame_rate = 60
    config.init_screen()

    game_objects: pg.sprite.Group[GameElement] = pg.sprite.Group()
    obstacle_list: list[GameElement] = []
    obstacle_group: pg.sprite.Group[GameElement] = pg.sprite.Group()
    cloud_list: list[GameElement] = []
    cloud_group: pg.sprite.Group[GameElement] = pg.sprite.Group()

    counter: Counter = Counter()
    dino: Dino = Dino()
    ground: Ground = Ground()

    def get_input() -> None:
        """This function gets the input from the user.
        It collects all inputs from the previous frame and
        processes them by modyfying the game according to the player wishes.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            dino.process_input(event)

    def game_over() -> None:
        """This function is called when the game is over."""
        counter.save_highscore()
        pg.quit()
        sys.exit()

    def update() -> None:
        """Update all grafic representations of the game elements."""
        dino.update()
        ground.update()
        cloud_group.update()
        obstacle_group.update()
        game_objects.update()

    def update_obstacles(obstacles: list[GameElement]) -> list[GameElement]:
        """Update all grafic representations of the game elements.

        Checks if the obstacles are still on the screen and
        removes them if they are not from the list with possible collisions.
        """
        return [obstacle for obstacle in obstacles if obstacle.alive()]  # type: ignore

    def update_clouds(clouds: list[GameElement]) -> list[GameElement]:
        """Update all grafic representations of the cloud elements.

        Checks if the clouds are still on the screen and
        removes them if they are not from the list with possible collisions.
        """
        return [cloud for cloud in clouds if cloud.alive()]

    def spawn_objects() -> None:
        """Spawn a new objects on the screen.

        Several different object types exist and are spawned.
        1. Obstacles
        2. Ground
        3. Clouds

        The number of obstacles that can exist paart of the game
        can go up to 3 but only with a certain probability.

        The ground is always present.

        Clouds can also exist up to 3 but they are counted
        separately from the obstacles.
        """

        # Obstacles
        if len(obstacle_list) < 3:
            # Only spawn obstacles every 20 frames
            if counter.cactus_counter > 20:
                # Chose between cactus and bird
                # Cacti are double the chance than birds
                match rd.randint(0, 400):
                    case 0 | 1 | 2 | 3:
                        obstacle_list.append(Cactus())
                    case 4:
                        obstacle_list.append(Bird())
                    case _:
                        pass

        for obstacle in obstacle_list:
            obstacle_group.add(obstacle)

        # Clouds
        if len(cloud_list) < 3:
            # Only spawn clouds every 100 frames
            if counter.cloud_counter > 100:
                if not rd.randint(0, 1000):
                    cloud_list.append(Cloud())

        for cloud in cloud_list:
            cloud_group.add(cloud)

        # Ground
        game_objects.add(ground)

    while True:
        obstacle_list = update_obstacles(obstacle_list)
        cloud_list = update_clouds(cloud_list)
        spawn_objects()
        get_input()
        counter.tick()
        update()

        if dino.check_collision(obstacle_list):
            break

        pg.display.flip()
        pg.time.Clock().tick(config.frame_rate)
        config.window.fill(config.background_color)

    game_over()


if __name__ == "__main__":
    main()
