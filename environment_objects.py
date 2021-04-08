import random
import pygame

plant_variants = ['grass', 'leaf', 'carrot', 'branch']

class Plants:

    def __init__(self, location, image, color=(243, 146, 51)):
        self.location = location
        self.color = color
        self.nutrition = 6
        self.image = pygame.transform.rotozoom(pygame.image.load('images/' + image + '.png'), random.randint(0, 360), 0.5)

    @staticmethod
    def initiate_at_random(display_size):
        return Plants([
            random.randint(0, display_size[0]),
            random.randint(0, display_size[1])
        ], plant_variants[random.randint(0, len(plant_variants) -1)])

    def show(self, target):
        target.blit(self.image, self.location)


class Herbivore:
    def __init__(self, location, sensed_plants, image='images/stegosaurus.png'):
        self.location = location
        self.color = (1, 197, 196)
        self.moving_direction = [0, 0]
        self.lifetime = 20
        self.sensed_plants = sensed_plants
        self.image = pygame.transform.rotozoom(pygame.image.load(image), 0, 1)


    @staticmethod
    def initiate_at_random(display_size, sensed_plants):
        return Herbivore([
            random.randint(0, display_size[0]),
            random.randint(0, display_size[1])
        ], sensed_plants)

    def show(self, target):
        # pygame.draw.circle(target, self.color, self.location, 10)
        target.blit(self.image, self.location)

    def move(self):
        self.location[0] += self.moving_direction[0] / 3.0
        self.location[1] += self.moving_direction[1] / 3.0

        self.lifetime -= 0

    def update_sensed_plants(self, sensed_plants):
        self.sensed_plants = sensed_plants

    def eat(self):

        # Loop through all the plants, and consume the one close to herbivore (if any).
        # Add its nutrition to my lifetime and delete that plant (which modifies global plant array)

        plant_consumed = False
        i = 0
        while not plant_consumed and i < len(self.sensed_plants):
            plant = self.sensed_plants[i]
            if abs(plant.location[0] - self.location[0]) < 30 and abs(plant.location[1] - self.location[1]) < 30:
                self.sensed_plants.pop(i)
                self.lifetime += plant.nutrition
                plant_consumed = True
            i += 1


class Player(Herbivore):  # Herbivore but with keyboard controls (easier testing and debugging)

    def __init__(self, location, sensed_plants):
        super().__init__(location, sensed_plants)
        self.color = (255, 255, 255)

    #
    # def eat(self):
    #     for plant in self.sensed_plants:
    #         if abs(plant.location[0] - self.location[0]) < 10 and abs(plant.location[1] - self.location[1]) < 10:
    #             print("Plant eaten.")
    #             self.sensed_plants.pop(plant)
    #             self.lifetime += plant.nutrition
