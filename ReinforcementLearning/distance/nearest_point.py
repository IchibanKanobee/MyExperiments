import numpy as np
import sys
import math


def get_distance(p1, p2):
    dist = math.sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
    return dist


def get_nearest_distance(point, array):
    point_count = array.shape[0]
    dist = sys.float_info.max
    index = -1

    for i in range(point_count):
        new_dist = get_distance(point, array[i])
        if (new_dist < dist):
            dist = new_dist
            index = i
    return (dist, index)


def remove_element(arr, index):
    shape = arr.shape
    new_array = np.zeros((shape[0] - 1, shape[1]))
    new_index = 0
    for i in range (shape[0]):
        if (i != index):
            new_array[new_index] = arr[i]
            new_index = new_index + 1
    return new_array


def get_point_cloud_nearest_point_distance(pc1, pc2):
    point_count = pc1.shape[0]
    dist = 0
    curr_point_count = point_count

    for i in range (curr_point_count):
        min_dist, index = get_nearest_distance(pc1[0], pc2)
        dist = dist + min_dist
        pc1 = remove_element(pc1, 0)
        pc2 = remove_element(pc2, index)
        curr_point_count = curr_point_count -1

    avg_distance = dist / point_count
    return avg_distance
        

