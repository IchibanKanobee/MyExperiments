import numpy as np
from distance import utils, nndistance_cpu

#a = np.array([[[[0, 2], [0, 4]]], [[[0, 4], [0, 2]]], [[[2, 0], [4, 0]]], [[[4, 0], [2, 0]]], [[[2, 3], [4, 5]]], [[[4, 5], [2, 3]]]])
a = np.array([[[[0, 2, 1], [0, 4, 1], [0, 3, 1]]], [[[0, 4, 1], [0, 3, 1], [0, 2, 1]]], [[[0, 3, 1], [0, 2, 1], [0, 4, 1]]],
[[[2, 0, 1], [4, 0, 1], [3, 0, 1]]], [[[4, 0, 1], [3, 0, 1], [2, 0, 1]]], [[[3, 0, 1], [4, 0, 1], [2, 0, 1]]],
[[[2, 3, 1], [4, 5, 1], [3, 5, 1]]], [[[3, 5, 1], [4, 5, 1], [2, 3, 1]]], [[[2, 3, 1], [3, 5, 1], [4, 5, 1]]]])


s = a.shape
b = np.zeros(s)

print (s)

pc_count = a.shape[0]
batch_size = a.shape[1]
dist = np.zeros((pc_count, pc_count))


for i in range (pc_count):
    for j in range(batch_size):
        a_norm = utils.pc_normalize(a[i][j])
        b[i][j] = a_norm

print ("Normalized centered point clouds:")
print (b)

for i in range(pc_count):
    for j in range (i, pc_count):
        dist[i, j] = nndistance_cpu.nn_distance_cpu(b[i], b[j])
        dist [j, i] = dist[i, j]
 
print ("Distance matrix")
print (dist)

np.savetxt('distance_matrix_3.txt', dist)
