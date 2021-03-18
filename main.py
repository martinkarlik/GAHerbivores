import pygame
import random
from environment_objects import *


DISPLAY_SIZE = (1200, 800)
GRASS_COLOR = (60, 178, 0)

NUM_CARNIVORES = 20

if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption("Herbivores vs. Carnivores")
    screen = pygame.display.set_mode(DISPLAY_SIZE)

    carnivores = [Carnivore.initiate_at_random(DISPLAY_SIZE) for _ in range(NUM_CARNIVORES)]

    broccoli = Broccoli.initiate_at_random(DISPLAY_SIZE)
    herbivore = Herbivore([DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] / 2])

    game_over = False
    while not game_over:

        # UPDATE EVERYTHING ACCORDING TO LOGIC
        for carnivore in carnivores:
            carnivore.wander_around_uselessly()

        herbivore.move()

        # DRAW EVERYTHING
        screen.fill(GRASS_COLOR)

        for carnivore in carnivores:
            carnivore.show(screen)

        broccoli.show(screen)
        herbivore.show(screen)

        # LISTEN FOR KEYBOARD INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_UP:
                    herbivore.moving_direction = [0, -1]
                elif event.key == pygame.K_DOWN:
                    herbivore.moving_direction = [0, 1]
                elif event.key == pygame.K_RIGHT:
                    herbivore.moving_direction = [1, 0]
                elif event.key == pygame.K_LEFT:
                    herbivore.moving_direction = [-1, 0]
            elif event.type == pygame.KEYUP:
                herbivore.moving_direction = [0, 0]

        pygame.display.update()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
