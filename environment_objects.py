import random
import pygame


class Plant:

    def __init__(self, location, color=(243, 146, 51)):
        self.location = location
        self.color = color

    @staticmethod
    def initiate_at_random(display_size):
        return Plant([
            random.randint(0, display_size[0]),
            random.randint(0, display_size[0])
        ])

    def show(self, target):
        pygame.draw.circle(target, self.color, self.location, 10)


class Herbivore:

    def __init__(self, location, sensed_plants):
        self.location = location
        self.color = (1, 197, 196)
        self.moving_direction = [0, 0]
        self.sensed_plants = sensed_plants

    @staticmethod
    def initiate_at_random(display_size, sensed_plants):
        return Herbivore([
            random.randint(0, display_size[0]),
            random.randint(0, display_size[0])
        ], sensed_plants)

    def show(self, target):
        pygame.draw.circle(target, self.color, self.location, 10)

    def move(self):
        self.location[0] += self.moving_direction[0] / 3.0
        self.location[1] += self.moving_direction[1] / 3.0

    def update_sensed_plants(self, sensed_plants):
        self.sensed_plants = sensed_plants


class Player:

    def __init__(self, location):
        self.location = location
        self.color = (255, 255, 255)
        self.moving_direction = [0, 0]

    @staticmethod
    def initiate_at_random(display_size):
        return Player([
            random.randint(0, display_size[0]),
            random.randint(0, display_size[1])
        ])

    def show(self, target):
        pygame.draw.circle(target, self.color, self.location, 10)

    def move(self):
        self.location[0] += self.moving_direction[0] / 3.0
        self.location[1] += self.moving_direction[1] / 3.0