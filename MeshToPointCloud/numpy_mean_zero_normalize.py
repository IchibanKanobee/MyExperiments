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

#SOURCE_DIR = '/raid/data/tinkercad/point_clouds/manually_clean_numpy/' + POINT_COUNT_STR + '/numpy_mean_0/'
#DEST_DIR = '/raid/data/tinkercad/point_clouds/manually_clean_numpy/' + POINT_COUNT_STR + '/numpy_mean_0_normalized/'

SOURCE_DIR = 'data/numpy_centered'
DEST_DIR = 'data/numpy_centered_normalised'


def normalize(f):
    radius = 0
    in_file = join(SOURCE_DIR, f)
    print ("Normalizing file " + f)
    data = np.loadtxt(in_file)
    data_shape = data.shape
    norm_data = np.zeros(data_shape)

#    if (data_shape == (POINT_COUNT, 3)):
    for i in range (data_shape[0]):
        r = np.linalg.norm(data[i])
        if (r > radius):
            radius = r

    for i in range (data_shape[0]):
        norm_data[i] = data[i] / radius

    out_file = join(DEST_DIR, f)
    np.savetxt(out_file, norm_data, fmt="%.5f")
#    else:
#        "Could not convert file " + f
#        print data_shape


file_op.ensure_dir_exists(DEST_DIR)
files = file_op.get_only_files(SOURCE_DIR)

p = Pool(multiprocessing.cpu_count())
p.map(normalize, files)
