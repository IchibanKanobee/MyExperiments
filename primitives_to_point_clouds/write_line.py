import numpy as np
from plyfile import plyfile
import os
import shutil


sample_count = 1500
point_count = 128

x_low = 0.
min_x_high = 40.
max_x_high = 100.

directory = "data/line/" + str(sample_count) + "_" + str(point_count)

if os.path.exists(directory):
    shutil.rmtree(directory)
    
os.makedirs(directory)

for i in range(sample_count):
    x_high = int(np.random.uniform(min_x_high, max_x_high))


    vertex = np.zeros((2048,),
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

    for i in range (point_count):
        vertex[i] = (np.random.uniform(x_low, x_high), 0, 0)

    el = plyfile.PlyElement.describe(vertex, 'vertex')

    length = x_high - x_low

    plyfile.PlyData([el]).write(directory + '/line_' + str(int(length)) + "_.ply")  
