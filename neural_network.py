import random
import numpy as np


def initiate_random_weights(n_weights):
    return [random.randrange(-1, 1) for _ in range(n_weights)]


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def forward_propagate(weights, features):
    activation = sigmoid(weights[0] + np.dot(weights[1:], features))
    return activation


def get_normalized_features(features, features_maximum):
    normalized_features = []
    for i in range(len(features)):
        normalized_features.append(features[i]/features_maximum[i])

    return normalized_features
