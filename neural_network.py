import random
import numpy as np


class PlantDirectionClassifier:

    def __init__(self):
        self.weights = self.initiate_random()

    @staticmethod
    def initiate_random():
        return [random.random() for _ in range(3)]

    def forward_propagate(self, features):
        return 0
