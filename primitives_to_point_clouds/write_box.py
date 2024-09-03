import numpy as np
from plyfile import plyfile
from point_cloud import box
import os
import shutil


sample_count = 1500
#point_count = 2048
point_count = 1024

max_length = 100
max_width = 80
max_height = 50

min_length = 50
min_width = 30
min_height = 10

directory = "data/box/" + str(sample_count) + "_" + str(point_count)

if os.path.exists(directory):
    shutil.rmtree(directory)
    
os.makedirs(directory)

for i in range(sample_count):
    length = int(np.random.uniform(min_length, max_length))
    width = int(np.random.uniform(min_width, max_width))
    height = int(np.random.uniform(min_height, max_height))

    vertex = box.get_box_point_cloud(point_count, length, width, height)
    el = plyfile.PlyElement.describe(vertex, 'vertex')
    name = directory + "/box_" + str(int(length)) + "_" + str(int(width)) + "_" + str(int(height)) + "_.ply"  
    plyfile.PlyData([el]).write(name)
