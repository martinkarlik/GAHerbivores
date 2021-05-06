import random
import numpy as np


def initiate_random_weights():
    return [random.random() for _ in range(2)]


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def forward_propagate(weights, features):
    """
    Multiply the features (plant's information) with the weights and then sigmoid them.
    """
    return random.random()


def get_normalized_features(features):
    return features