import random

import numpy as np
import pygame
import math
import numpy as np

import neural_network as nn

DISPLAY_SIZE = (1200, 800)
MAX_DISTANCE = np.sqrt(2)*DISPLAY_SIZE[1]
MAX_PLANT_NUTRITION = 1000
MAX_CAFFEINE = 1
plant_variants = ['grass', 'leaf', 'carrot', 'branch']


class Plant:

    def __init__(self, location, image, color=(243, 146, 51)):
        self.location = location
        self.color = color
        self.nutrition = 1000
        self.caffeine = 0.8
        self.image = pygame.transform.rotozoom(pygame.image.load('images/' + image + '.png'), random.randint(0, 360), 0.5)

    @staticmethod
    def initiate_at_random():
        return Plant([
            random.randint(0, DISPLAY_SIZE[0]),
            random.randint(0, DISPLAY_SIZE[1])
        ], plant_variants[random.randint(0, len(plant_variants) - 1)])

    def show(self, target):
        target.blit(self.image, self.location)

    def get_location(self):
        return self.location


class Herbivore:

    def __init__(self, location, weights, image):

        self.location = location
        self.color = (1, 197, 196)

        self.isMating = False
        self.isDead = False

        self.moving_direction = [0, 1]
        self.sensed_plants = sensed_plants
        self.target_plant_location = None
        self.turning_speed = 0.01
        self.sensed_plants = None

        self.speed_multiplier = 0.7
        self.is_turning = False
        self.angle_to_plant = None
        self.image = pygame.transform.rotozoom(pygame.image.load(image), 0, 1)

        self.lifetime = 0
        self.hunger = 5000
        self.chromosome = weights if weights is not None else nn.initiate_random_weights()

    @staticmethod
    def initiate_at_random(weights=None, image='images/stegosaurus.png'):
        return Herbivore([
            random.randint(0, DISPLAY_SIZE[0]),
            random.randint(0, DISPLAY_SIZE[1])
        ], weights, image)

    def show(self, target):
        target.blit(self.image, self.location)

    def move(self):
        self.location[0] += self.moving_direction[0] * self.speed_multiplier
        self.location[1] += self.moving_direction[1] * self.speed_multiplier

        self.hunger -= 1

    def update_sensed_plants(self, sensed_plants):
        self.sensed_plants = sensed_plants

    def update_moving_direction(self):
        target_direction = np.subtract(self.location, self.target_plant_location)
        target_vector_length = math.sqrt(math.pow(target_direction[0], 2) + math.pow(target_direction[1], 2))
        normalized_target_direction = [target_direction[0] / target_vector_length,
                                       target_direction[1] / target_vector_length]
        if not np.allclose(self.moving_direction, normalized_target_direction):
            if self.is_turning:
                self.moving_direction = np.add(self.moving_direction, self.turn_target)
                if np.allclose(self.moving_direction, normalized_target_direction):
                    self.moving_direction = normalized_target_direction
                    self.is_turning = False
            else:
                self.turn_target = np.subtract(normalized_target_direction, self.moving_direction)
                self.turn_target = np.multiply(self.turn_target, self.turning_speed)
                self.angle_to_plant = self.angle_to_plant * self.turning_speed
                self.is_turning = True

    def eat(self):
        """
        Loop through all the plants, and consume the one close to herbivore (if any).
        Add its nutrition to my lifetime and delete that plant (which modifies global plant array).
        """

        i = 0
        plant_consumed = False
        while i < len(self.sensed_plants) and not plant_consumed:
            plant = self.sensed_plants[i]
            if abs(plant.location[0] - self.location[0]) < 30 and abs(plant.location[1] - self.location[1]) < 30:
                self.sensed_plants.pop(i)
                self.hunger += plant.nutrition
                plant_consumed = True
            i += 1

    def lock_target(self):

        desired_plant_index = 0
        max_confidence = 0

        for i in range(0, len(self.sensed_plants)):
            features = self._construct_features(self.sensed_plants[i])
            confidence = nn.forward_propagate(self.chromosome, features)
            if confidence > max_confidence:
                desired_plant_index = i
                max_confidence = confidence

        desired_plant = self.sensed_plants[desired_plant_index]

        # print(len(self.sensed_plants))
        # desired_plant = self.sensed_plants[random.randint(0, len(self.sensed_plants) - 1)]

        desired_plant = self.sensed_plants[0]
        self.target_plant_location = desired_plant.location
        self.angle_to_plant = get_angle(normalize(np.subtract(desired_plant.location, self.location)), [0, 0],
                                        self.moving_direction)
        print(self.angle_to_plant)
        # self.moving_direction = self._get_moving_direction(desired_plant.location)
        # self.update_moving_direction(desired_plant.location)

    def _construct_features(self, plant):
        target_direction = [self.location[0] - plant.location[0], self.location[1] - plant.location[1]]
        plant_distance = math.sqrt(math.pow(target_direction[0], 2) + math.pow(target_direction[1], 2))

        features = [plant_distance, plant.nutrition, plant.caffeine]
        features_maximum = [MAX_DISTANCE, MAX_PLANT_NUTRITION, MAX_CAFFEINE]
        normalized_features = nn.get_normalized_features(features, features_maximum)

        return normalized_features

    def _get_moving_direction(self, target):
        # Geza's clever math and physics stuff
        magnitude = max(abs(target[0] - self.location[0]), abs(target[1] - self.location[1]))
        return [(target[0] - self.location[0]) / magnitude, (target[1] - self.location[1]) / magnitude]



def get_angle(a, b, c):
    print(a)
    print(b)
    print(c)
    angle = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    return angle


def normalize(vector):
    vector_length = math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2))
    normalized_vector = [vector[0] / vector_length,
                         vector[1] / vector_length]
    return normalized_vector
