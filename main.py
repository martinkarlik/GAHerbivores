import pygame
import random
from environment_objects import *


DISPLAY_SIZE = (1200, 800)
BACKGROUND_COLOR = (184, 222, 111)


NUM_HERBIVORES = 5
NUM_PLANTS = 10

if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption("Hunger Games: Herbivores")
    screen = pygame.display.set_mode(DISPLAY_SIZE)

    plants = [Plants.initiate_at_random(DISPLAY_SIZE) for _ in range(NUM_PLANTS)]
    herbivores = [Herbivore.initiate_at_random(DISPLAY_SIZE, plants) for _ in range(NUM_HERBIVORES)]

    player = Player([DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] / 2], plants)

    game_over = False
    while not game_over:

        # UPDATE EVERYTHING ACCORDING TO LOGIC

        for _ in range(NUM_PLANTS - len(plants)):
            plants.append(Plants.initiate_at_random(DISPLAY_SIZE))

        for herbivore in herbivores:
            herbivore.move()
            herbivore.eat()

        player.move()
        player.eat()



        # DRAW EVERYTHING
        screen.fill(BACKGROUND_COLOR)

        for herbivore in herbivores:
            herbivore.show(screen)

        for plant in plants:
            plant.show(screen)

        player.show(screen)

        # LISTEN FOR KEYBOARD INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_UP:
                    player.moving_direction = [0, -1]
                elif event.key == pygame.K_DOWN:
                    player.moving_direction = [0, 1]
                elif event.key == pygame.K_RIGHT:
                    player.moving_direction = [1, 0]
                elif event.key == pygame.K_LEFT:
                    player.moving_direction = [-1, 0]
            elif event.type == pygame.KEYUP:
                player.moving_direction = [0, 0]

        pygame.display.update()


