import random
import pygame


class Plant:

    def __init__(self, location, color=(243, 146, 51)):
        self.location = location
        self.color = color
        self.nutrition = 6

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

        self.lifetime -= 0

    def update_sensed_plants(self, sensed_plants):
        self.sensed_plants = sensed_plants

    def eat(self):
        for plant in self.sensed_plants:
            if abs(plant.location[0] - self.location[0]) < 10 and abs(plant.location[1] - self.location[1]) < 10:
                print("Plant eaten.")
                self.sensed_plants.pop(0)
                self.lifetime += plant.nutrition


class Player(Herbivore):  # Herbivore but with keyboard controls (easier testing and debugging)

    def __init__(self, location, sensed_plants):
        super().__init__(location, sensed_plants)
        self.color = (255, 255, 255)


    def eat(self):
        for plant in self.sensed_plants:
            if abs(plant.location[0] - self.location[0]) < 10 and abs(plant.location[1] - self.location[1]) < 10:
                print("Plant eaten.")
                self.sensed_plants.pop(0)
                self.lifetime += plant.nutrition
