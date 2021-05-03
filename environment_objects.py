import random
import pygame
import math


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

    def get_location(self):
        return self.location


class Herbivore:

    def __init__(self, location, sensed_plants):
        self.location = location
        self.color = (1, 197, 196)
        self.moving_direction = [0, 0]
        self.sensed_plants = sensed_plants
        self.turning_speed = 0.1
        self.is_turning = False
        self.turn_target = 0

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

    def update_plant_positions(self, sensed_plants):
        self.sensed_plants = sensed_plants

    def update_moving_direction(self, plant_id):
        target_direction = self.location - self.sensed_plants[plant_id].get_location()
        target_vector_length = math.sqrt(math.pow(target_direction[0]) + math.pow(target_direction[1]))
        normalized_target_direction = [target_direction[0] / target_vector_length,
                                       target_direction[1] / target_vector_length]
        if self.moving_direction != normalized_target_direction:
            if self.is_turning:
                self.moving_direction += self.turn_target
                if self.moving_direction == normalized_target_direction:
                    self.is_turning = False
            else:
                self.turn_target = normalized_target_direction - self.moving_direction
                self.turn_target = self.turn_target*self.turning_speed
                self.is_turning = True




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
