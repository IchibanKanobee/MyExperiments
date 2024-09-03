import numpy as np
from point_cloud import cylinder
from plyfile import plyfile
import os
import shutil

sample_count = 1500
point_count = 1024

min_height = 10
min_radius = 5

max_height = 100
max_radius = 50

directory = "data/cylinder/" + str(sample_count) + "_" + str(point_count)


if os.path.exists(directory):
    shutil.rmtree(directory)
    
os.makedirs(directory)

for i in range(sample_count):
    height = int(np.random.uniform(min_height, max_height))
    radius = int(np.random.uniform(min_radius, max_radius))


    vertex = cylinder.get_cylinder_point_cloud(point_count, height, radius)

    el = plyfile.PlyElement.describe(vertex, 'vertex')

    name = directory + "/cylinder_" + str(int(height)) + "_" + str(int(radius)) + "_.ply"  

    plyfile.PlyData([el]).write(name)
