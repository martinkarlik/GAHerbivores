import random
import pygame
import math

import neural_network as nn

plant_variants = ['grass', 'leaf', 'carrot', 'branch']


class Plant:

    def __init__(self, location, image, color=(243, 146, 51)):
        self.location = location
        self.color = color
        self.nutrition = 1000
        self.image = pygame.transform.rotozoom(pygame.image.load('images/' + image + '.png'), random.randint(0, 360), 0.5)

    @staticmethod
    def initiate_at_random(display_size):
        return Plant([
            random.randint(0, display_size[0]),
            random.randint(0, display_size[1])
        ], plant_variants[random.randint(0, len(plant_variants) -1)])

    def show(self, target):
        target.blit(self.image, self.location)

    def get_location(self):
        return self.location


class Herbivore:

    def __init__(self, location, sensed_plants, image='images/stegosaurus.png'):
        self.location = location
        self.color = (1, 197, 196)

        self.moving_direction = [0, 0]
        self.sensed_plants = sensed_plants
        self.turning_speed = 0.1
        self.is_turning = False
        self.turn_target = 0
        self.image = pygame.transform.rotozoom(pygame.image.load(image), 0, 1)

        self.lifetime = 5000
        self.chromozome = nn.initiate_random_weights()


    @staticmethod
    def initiate_at_random(display_size, sensed_plants):
        return Herbivore([
            random.randint(0, display_size[0]),
            random.randint(0, display_size[1])
        ], sensed_plants)

    def show(self, target):
        target.blit(self.image, self.location)

    def move(self):
        self.location[0] += self.moving_direction[0] / 3.0
        self.location[1] += self.moving_direction[1] / 3.0

        self.lifetime -= 1

    def update_sensed_plants(self, sensed_plants):
        self.sensed_plants = sensed_plants

    def update_moving_direction(self, target_location):
        target_direction = self.location - target_location
        target_vector_length = math.sqrt(math.pow(target_direction[0], 2) + math.pow(target_direction[1], 2))
        normalized_target_direction = [target_direction[0] / target_vector_length,
                                       target_direction[1] / target_vector_length]
        if self.moving_direction != normalized_target_direction:
            if self.is_turning:
                self.moving_direction += self.turn_target
                if self.moving_direction == normalized_target_direction:
                    self.is_turning = False
            else:
                self.turn_target = normalized_target_direction - self.moving_direction
                self.turn_target = self.turn_target * self.turning_speed
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
                self.lifetime += plant.nutrition
                plant_consumed = True
            i += 1

    def lock_target(self):

        desired_plant_index = 0
        max_confidence = 0

        for i in range(0, len(self.sensed_plants)):
            features = self._construct_features(self.sensed_plants[i])
            confidence = nn.forward_propagate(self.chromozome, features)
            if confidence > max_confidence:
                desired_plant_index = i
                max_confidence = confidence

        # desired_plant = self.sensed_plants[0]

        desired_plant = self.sensed_plants[0]
        self.update_moving_direction(desired_plant.location)

    def move(self):
        self.location[0] += self.moving_direction[0] / 3.0
        self.location[1] += self.moving_direction[1] / 3.0

    def _construct_features(self, plant):
        """
        Get the features we care about, so that would be
        features = [my distance to the plant, plant's nutrition]
        """
        return []


class Player(Herbivore):  # Herbivore but with keyboard controls (easier testing and debugging)

    def __init__(self, location, sensed_plants):
        super().__init__(location, sensed_plants)
        self.color = (255, 255, 255)
