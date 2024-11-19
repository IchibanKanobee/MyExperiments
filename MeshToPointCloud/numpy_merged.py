import sys
sys.path.append("..")

from utils import file_op
from os.path import join, splitext
import os
import numpy as np


POINT_COUNT = 2048
POINT_COUNT_STR = str(POINT_COUNT)

SOURCE_DIR = '/raid/data/tinkercad/sample2/point_clouds/ply/' + POINT_COUNT_STR + '/numpy'
DEST_DIR = '/raid/data/tinkercad/sample2/point_clouds/ply/' + POINT_COUNT_STR + '/numpy_single'

file_op.ensure_dir_exists(DEST_DIR)
files = file_op.get_only_files(SOURCE_DIR)

count = len(files)
print count

common = np.zeros(shape=(count * POINT_COUNT, 3))
print common.shape

i = 0
for f in files:
    print "Converting file " + str(i) + " out of " + str(count)
    in_file = join(SOURCE_DIR, f)
    data = np.loadtxt(in_file)
    data_shape = data.shape
    if (data_shape != (POINT_COUNT, 3)):
        print ("Skipping file " + f )
        print data_shape
        continue    
    common[i * POINT_COUNT : (i + 1) * POINT_COUNT] = data
    i = i + 1

out_file = join(DEST_DIR, "common.txt")
np.savetxt(out_file, common, fmt="%.5f")
print common

