import random
import pygame


class Carnivore:

    def __init__(self, location):
        self.location = location

    @staticmethod
    def initiate_at_random(display_size):
        return Carnivore([
            random.randint(0, display_size[0]),
            random.randint(0, display_size[0])
        ])

    def show(self, target):
        pygame.draw.circle(target, (0, 0, 0), self.location, 10)

    def wander_around_uselessly(self):
        self.location[0] += random.randint(-1, 1) / 3.0
        self.location[1] += random.randint(-1, 1) / 3.0


class Broccoli:

    def __init__(self, location):
        self.location = location

    @staticmethod
    def initiate_at_random(display_size):
        return Broccoli([
            random.randint(0, display_size[0]),
            random.randint(0, display_size[0])
        ])

    def show(self, target):
        pygame.draw.circle(target, (100, 0, 0), self.location, 10)


class Herbivore:

    def __init__(self, location):
        self.location = location
        self.moving_direction = [0, 0]

    def show(self, target):
        pygame.draw.circle(target, (255, 255, 255), self.location, 10)

    def move(self):
        self.location[0] += self.moving_direction[0] / 3.0
        self.location[1] += self.moving_direction[1] / 3.0
