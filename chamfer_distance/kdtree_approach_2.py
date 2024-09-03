#https://stackoverflow.com/questions/47060685/chamfer-distance-between-two-point-clouds-in-tensorflow

import numpy as np
from sklearn.neighbors import KDTree

def chamfer_distance(arr1,arr2):
    # final = 0
    # final = tf.cast(final,tf.float32)
    num_point = 3
    tree1 = KDTree(arr1, leafsize=num_point+1)
    tree2 = KDTree(arr2, leafsize=num_point+1)
    distances1, _ = tree1.query(arr2)
    distances2, _ = tree2.query(arr1)
    av_dist1 = np.mean(distances1)
    av_dist2 = np.mean(distances2)
    dist = (av_dist1+av_dist2)
    return dist

a1 = np.array([1,2,3])
a2 = np.array([3,1,2])
dist = chamfer_distance(a1, a2)
print (dist)
