import numpy as np
from plyfile import plyfile
from point_cloud import sphere
import os
import shutil

sample_count = 1500
point_count = 1024

max_radius = 2000
min_radius = 20

directory = "data/sphere/" + str(sample_count) + "_" + str(point_count)

if os.path.exists(directory):
    shutil.rmtree(directory)
    
os.makedirs(directory)

for i in range(sample_count):
    radius = int(np.random.uniform(min_radius, max_radius))

    vertex = sphere.get_sphere_point_cloud(point_count, radius)

    el = plyfile.PlyElement.describe(vertex, 'vertex')
    name = directory + "/sphere_" + str(int(radius)) + "_.ply"  
    plyfile.PlyData([el]).write(name)
