import random
from environment_objects import *


def fitness_proportionate_selection(population):

    total_fitness = sum(herbivore.lifetime for herbivore in population)
    threshold = random.uniform(0, total_fitness)
    current = 0
    for herbivore in population:
        current += herbivore.fitness
        if current > threshold:
            return herbivore
    return population[0]


def reproduce(first_parent, second_parent):
    offspring_chromozome = [(first_parent.chromozome[0] + second_parent.chromozome[0]) / 2,
                            (first_parent.chromozome[1] + second_parent.chromozome[1]) / 2]

    return Herbivore.initiate_at_random(weights=offspring_chromozome)


def mutate(offspring):
    """
    Mutate the weights of the offspring (access them by offspring.chromozome).
    I use "weights" and "chromozome" interchangebly, because in the context of GA, it's a chromozome, in the context of NN they're weights.
    Sorry about that.
    The weights is a list of 2 numbers, e.g. [1.4, 0.8], representing the importance of the plant's information (distance, nutrition)
    So basically, we would like [1.4, 0.8] to become let's say [1.5, 0.8] or sth like that. Just slightly randomize it.
    """
    mutated_chromosome = [offspring.chromosome[0] * (0.8 + random.random() * 0.4), offspring.chromosome[1] * (0.8 + random.random() * 0.4)]

    return Herbivore.initiate_at_random(weights=mutated_chromosome)



