import numpy as np
from plyfile import plyfile
import os
import shutil


sample_count = 1500
point_count = 512

x_low = 0.
min_x_high = 40.
max_x_high = 100.

y_low = 0.
y_high = 0.

z_low = 0.
min_z_high = 20.
max_z_high = 80.

directory = "data/square/" + str(sample_count) + "_" + str(point_count)

if os.path.exists(directory):
    shutil.rmtree(directory)
    
os.makedirs(directory)

for i in range(sample_count):
    x_high = int(np.random.uniform(min_x_high, max_x_high))
    z_high = int(np.random.uniform(min_z_high, max_z_high))


    vertex = np.zeros((2048,),
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

    for i in range (point_count):
        vertex[i] = (np.random.uniform(x_low, x_high), np.random.uniform(y_low, y_high), np.random.uniform(z_low, z_high))

    el = plyfile.PlyElement.describe(vertex, 'vertex')

    width = x_high - x_low
    height =  z_high - z_low

    plyfile.PlyData([el]).write(directory + '/square_' + str(int(width)) + "_" + str(int(height)) + "_.ply")  
