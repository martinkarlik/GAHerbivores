import random

from environment_objects import *


class Population:

    def __init__(self, agents):
        self.agents = agents

    # def fitness_proportionate_selection(self):
    #     total_fitness = sum(individual.fitness for individual in population)
    #     threshold = random.uniform(0, total_fitness)
    #     current = 0
    #     for individual in population:
    #         current += individual.fitness
    #         if current > threshold:
    #             return individual
    #     return population[0]  # fail safe returns the first individual
    #
    #
    # def reproduce(first_parent, second_parent):
    #     """Generates a single offspring of two parents from a random cross-over point."""
    #
    #     crossover_point = random.randint(1, len(first_parent.chromosome))
    #
    #     return Individual(first_parent.chromosome[:crossover_point] + second_parent.chromosome[crossover_point:])
    #
    #
    # def mutate(offspring):
    #     """Mutates a single gene (i.e., number) of an offspring at a random location with a valid random number."""
    #
    #     offspring.chromosome[random.randint(0, len(offspring.chromosome) - 1)] = random.randint(1, len(offspring.chromosome))
    #     # The indices are 0-7 but the values are 1-8.
    #
    #     return offspring
    #
    #
    # def random_individual(num_of_queens):
    #     """Generates a random valid individual consisting of one row number [1, num_of_queens] for each column of the
    #     chessboard. """
    #     return Individual([random.randint(1, num_of_queens) for _ in range(num_of_queens)])
    #
    #
    # def random_population(num_of_queens, population_size):
    #     """Generates a random population of individuals."""
    #     return [random_individual(num_of_queens) for _ in range(population_size)]
    #
    #
    # def retrieve_most_fit(population):
    #     """Retrieves the most fit individual from a population of individuals."""
    #     most_fit = population[0]
    #
    #     for individual in population:
    #         if individual.fitness > most_fit.fitness:
    #             most_fit = individual
    #
    #     return most_fit
    #
    #
    # def print_most_fit(individual, generation_num):
    #     """Prints the most fit individual on an N x N chessboard of zeros."""
    #     board = [[0] * len(individual.chromosome) for _ in range(len(individual.chromosome))]
    #     print('Most fit configuration:')
    #     for idx, _ in enumerate(board):
    #         board[(len(individual.chromosome) - 1) - (individual.chromosome[idx] - 1)][idx] = 1
    #     for row in board:
    #         print(row)
    #     print('Individual:')
    #     print(individual.chromosome)
    #     print('Fitness:')
    #     print(individual.fitness)
    #     print('Number of generations:')
    #     print(generation_num)
    #     return None
    #
    #
    # def genetic_algorithm(population, max_fitness):
    #     """Generates a population of individuals by two-parent-single-offspring reproduction. Parents have a probability of
    #         being selected for crossover proportional to their individual fitness when compared with the total overall fitness
    #         of the population. A single set of parents are selected for cross-over and their genes are joined via a random
    #         cross-over point to form a single offspring. Offspring have a positive but negligible probability of mutation where
    #         a single gene at a random location is randomly mutated."""
    #
    #     mutation_probability = 0.05
    #     generation_num = 1
    #     while max_fitness not in [individual.fitness for individual in population] and generation_num < 1000:
    #
    #         offspring_population = []
    #
    #         while len(offspring_population) < len(population):
    #             parent_a = fitness_proportionate_selection(population)
    #             parent_b = fitness_proportionate_selection(population)
    #
    #             offspring = reproduce(parent_a, parent_b)
    #             if random.random() < mutation_probability:
    #                 offspring = mutate(offspring)
    #
    #             offspring_population.append(offspring)
    #
    #         population = offspring_population
    #
    #         generation_num += 1
    #
    #     return retrieve_most_fit(population), generation_num


