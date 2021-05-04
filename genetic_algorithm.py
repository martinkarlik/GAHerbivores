import random
from environment_objects import *


def fitness_proportionate_selection(population):
    """
    Select a herbivore out a population in proportion to its fitness (i.e. lifetime).
    """
    return population[0]


def reproduce(first_parent, second_parent):
    """
    Generate an offspring from the two parents.
    I don't know how, I guess just average their weights ([1.4, 0.8] and [1.6, 1.0] would become [1.5, 0.9]),
    but you can be more clever about it.
    """
    return first_parent


def mutate(offspring):
    """
    Mutate the weights of the offspring (access them by offspring.chromozome).
    I use "weights" and "chromozome" interchangebly, because in the context of GA, it's a chromozome, in the context of NN they're weights.
    Sorry about that.
    The weights is a list of 2 numbers, e.g. [1.4, 0.8], representing the importance of the plant's information (distance, nutrition)
    So basically, we would like [1.4, 0.8] to become let's say [1.5, 0.8] or sth like that. Just slightly randomize it.
    """
    return offspring



