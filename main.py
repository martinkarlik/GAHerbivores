import pygame
import random
from environment_objects import *
import genetic_algorithm as ga


DISPLAY_SIZE = (1200, 800)
BACKGROUND_COLOR = (184, 222, 111)

NUM_GENERATIONS = 20
TIME_PER_GENERATION = 10000
MUTATION_PROBABILITY = 0.05

NUM_HERBIVORES = 10
NUM_PLANTS = 5


if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption("Hunger Games: Herbivores")
    screen = pygame.display.set_mode(DISPLAY_SIZE)
    font = pygame.font.Font('freesansbold.ttf', 32)

    plants = []
    herbivores = [Herbivore.initiate_at_random() for _ in range(NUM_HERBIVORES)]
    most_fit = None

    for i in range(1, NUM_GENERATIONS):

        for ii in range(TIME_PER_GENERATION):

            # Replant plants if some have been eaten.
            plants_updated = False
            for _ in range(NUM_PLANTS - len(plants)):
                plants_updated = True
                plants.append(Plant.initiate_at_random())

            for herbivore in herbivores:
                herbivore.update_sensed_plants(plants)
                #herbivore.move()
                #herbivore.eat()

                if plants_updated or ii == 0:
                    herbivore.lock_target()

                if not herbivore.is_dead:

                    herbivore.score -= 1
                    herbivore.update_sensed_plants(plants)
                    herbivore.update_moving_direction()
                    if not herbivore.is_turning:
                        herbivore.move()
                        herbivore.eat()

                    if herbivore.score <= 0:
                        herbivore.is_dead = True
                        herbivore.image = pygame.transform.rotozoom(herbivore.image, 180, 1)
                        print("poor herbivore died :(")


            # DRAW EVERYTHING
            screen.fill(BACKGROUND_COLOR)

            for herbivore in herbivores:
                herbivore.show(screen)

            for plant in plants:
                plant.show(screen)


            text = font.render("Generation: {}".format(i), True, (0, 0, 0), BACKGROUND_COLOR)
            text_rect = text.get_rect()
            text_rect.bottomleft = (0, 40)
            screen.blit(text, text_rect)

            text = font.render("Time: {}".format(ii), True, (0, 0, 0), BACKGROUND_COLOR)
            text_rect = text.get_rect()
            text_rect.bottomleft = (0, 80)
            screen.blit(text, text_rect)

            best_lifetime = most_fit.lifetime if most_fit is not None else "-"
            text = font.render("Best life: {}".format(best_lifetime), True, (0, 0, 0), BACKGROUND_COLOR)
            text_rect = text.get_rect()
            text_rect.bottomleft = (0, 120)
            screen.blit(text, text_rect)

            best_weights = [round(num, 2) for num in most_fit.chromosome] if most_fit else "-"
            text = font.render("Best weights: {}".format(best_weights), True, (0, 0, 0), BACKGROUND_COLOR)
            text_rect = text.get_rect()
            text_rect.bottomleft = (0, 160)
            screen.blit(text, text_rect)

            pygame.display.update()

        # EVOLVE NEW GENERATION

        most_fit = ga.get_most_fit(herbivores)

        offspring_population = []
        while len(offspring_population) < len(herbivores):

            parent_a = ga.fitness_proportionate_selection(herbivores)
            parent_b = ga.fitness_proportionate_selection(herbivores)

            offspring = ga.reproduce(parent_a, parent_b)

            if random.random() < MUTATION_PROBABILITY:
                offspring = ga.mutate(offspring)

            offspring_population.append(offspring)

        plants = []
        herbivores = offspring_population







