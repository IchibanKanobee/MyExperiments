import numpy as np
from point_cloud import cone
from plyfile import plyfile
import math
import os
import shutil

sample_count = 1500
point_count = 1024

max_angle = 80
max_radius = 100

min_angle = 10
min_radius = 20

directory = "data/cone/" + str(sample_count) + "_" + str(point_count)

if os.path.exists(directory):
    shutil.rmtree(directory)
    
os.makedirs(directory)

for i in range(sample_count):
    angle = int(np.random.uniform(min_angle, max_angle))
    radius = int(np.random.uniform(min_radius, max_radius))

    rad = math.radians(angle)

    vertex = cone.get_cone_point_cloud(point_count, rad, radius)

    el = plyfile.PlyElement.describe(vertex, 'vertex')

    name = directory + "/cone_" + str(int(angle)) + "_" + str(int(radius)) + "_.ply"  

    plyfile.PlyData([el]).write(name)
