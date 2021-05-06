import random
import numpy as np


def initiate_random_weights():
    return [random.randrange(-1, 1) for _ in range(3)]


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def forward_propagate(weights, features):
    bias = random.randrange(-1, 1)
    activation = sigmoid(np.dot(weights, features)+bias)
    """
    Multiply the features (plant's information) with the weights and then sigmoid them.
    """
    return activation


def get_normalized_features(features, features_maximum):
    normalized_features = []
    for i in range(len(features)):
        normalized_features.append(features[i]/features_maximum[i])

    return normalized_features
