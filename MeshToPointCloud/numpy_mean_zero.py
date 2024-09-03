import sys
sys.path.append("..")

from utils import file_op
from os.path import join, splitext
import os

import multiprocessing
from multiprocessing import Pool

import numpy as np


POINT_COUNT = 2048
POINT_COUNT_STR = str(POINT_COUNT)

#SOURCE_DIR = '/raid/data/tinkercad/point_clouds/manually_clean_numpy/' + POINT_COUNT_STR
#DEST_DIR = '/raid/data/tinkercad/point_clouds/manually_clean_numpy/' + POINT_COUNT_STR + '/numpy_mean_0/'

SOURCE_DIR = 'data/numpy'
DEST_DIR = 'data/numpy_centered'

def mean_to_zero(f):
    name, ext = splitext(f)
    in_file = join(SOURCE_DIR, f)
    print ("Converting file " + f)
    data = np.loadtxt(in_file)
    data_shape = data.shape
#    if (data_shape == (POINT_COUNT, 3)):
    mean = np.mean(data, axis = 0)
    mean_0 = data - mean
    out_file = join(DEST_DIR, f)
    np.savetxt(out_file, mean_0, fmt="%.5f")
#    else:
#        "Could not convert file " + f
#        print data_shape


file_op.ensure_dir_exists(DEST_DIR)
files = file_op.get_only_files(SOURCE_DIR)

p = Pool(multiprocessing.cpu_count())
p.map(mean_to_zero, files)
