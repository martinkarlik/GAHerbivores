import random
from environment_objects import *


def fitness_proportionate_selection(population):

    total_fitness = sum(herbivore.lifetime for herbivore in population)
    threshold = random.uniform(0, total_fitness)
    current = 0
    for herbivore in population:
        current += herbivore.lifetime
        if current > threshold:
            return herbivore

    return population[0]


def reproduce(first_parent, second_parent):

    offspring_chromosome = [(first_parent.chromosome[i] + second_parent.chromosome[i]) / 2 for i in range(len(first_parent.chromosome))]

    return Herbivore.initiate_at_random(weights=offspring_chromosome)


def mutate(offspring):
    mutated_chromosome = [offspring.chromosome[i] * (0.8 + random.random() * 0.4) for i in range(len(offspring.chromosome))]

    return Herbivore.initiate_at_random(weights=mutated_chromosome)



