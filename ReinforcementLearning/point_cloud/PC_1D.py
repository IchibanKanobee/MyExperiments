import numpy as np
from distance import EMD

def get_equal_weights(point_count):
    weights = np.zeros((point_count))
    for i in range (point_count):
        weights[i] = 1.0 / point_count
    return weights


def get_point_cloud_1D(length, point_count):
    point_cloud = np.zeros((point_count, 3))
    for i in range (point_count):
        point_cloud[i][0] = np.random.uniform(0, length)
    return point_cloud

def get_point_cloud_signature_1D(length, point_count):
    pc = get_point_cloud_1D(length, point_count)
    weights = get_equal_weights(point_count)
    signature = (pc, weights)
    return signature


