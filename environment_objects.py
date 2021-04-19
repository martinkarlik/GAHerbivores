import random
import pygame

from neural_network import *


class Plant:

    def __init__(self, location, color=(243, 146, 51)):
        self.location = location
        self.color = color
        self.nutrition = 2000

    @staticmethod
    def initiate_at_random(display_size):
        return Plant([
            random.randint(0, display_size[0]),
            random.randint(0, display_size[1])
        ])

    def show(self, target):
        pygame.draw.circle(target, self.color, self.location, 10)


class Herbivore:

    def __init__(self, location, sensed_plants):
        self.location = location
        self.color = (1, 197, 196)

        self.moving_direction = [0, 0]
        self.lifetime = 20
        self.sensed_plants = sensed_plants

        self.lifetime = 5000
        self.model = PlantDirectionClassifier()

    @staticmethod
    def initiate_at_random(display_size, sensed_plants):
        return Herbivore([
            random.randint(0, display_size[0]),
            random.randint(0, display_size[1])
        ], sensed_plants)

    def show(self, target):
        pygame.draw.circle(target, self.color, self.location, 10)

    def move(self):
        self.location[0] += self.moving_direction[0] / 3.0
        self.location[1] += self.moving_direction[1] / 3.0

        self.lifetime -= 1

    def update_sensed_plants(self, sensed_plants):
        self.sensed_plants = sensed_plants

    def eat(self):

        # Loop through all the plants, and consume the one close to herbivore (if any).
        # Add its nutrition to my lifetime and delete that plant (which modifies global plant array)

        i = 0
        plant_consumed = False
        while i < len(self.sensed_plants) and not plant_consumed:
            plant = self.sensed_plants[i]
            if abs(plant.location[0] - self.location[0]) < 30 and abs(plant.location[1] - self.location[1]) < 30:
                self.sensed_plants.pop(i)
                self.lifetime += plant.nutrition
                plant_consumed = True
            i += 1

    def _construct_features(self):
        # Use self.sensed_plants to construct a list of features
        return []

    def _get_moving_direction(self, target):
        # Geza's clever math and physics stuff
        magnitude = max(abs(target[0] - self.location[0]), abs(target[1] - self.location[1]))

        return [(target[0] - self.location[0]) / magnitude, (target[1] - self.location[1]) / magnitude]

    def lock_target(self):

        # features = self._construct_features()
        # output = self.model.forward_propagate(features)

        # desired_plant = self.sensed_plants[output]
        desired_plant = self.sensed_plants[0]

        self.moving_direction = self._get_moving_direction(desired_plant.location)


class Player(Herbivore):  # Herbivore but with keyboard controls (easier testing and debugging)

    def __init__(self, location, sensed_plants):
        super().__init__(location, sensed_plants)
        self.color = (255, 255, 255)
