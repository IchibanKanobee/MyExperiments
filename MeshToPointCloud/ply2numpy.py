import sys
sys.path.append("..")

from utils import file_op
from os.path import join, splitext
import os

import multiprocessing
from multiprocessing import Pool

from ply.plyfile import (PlyData, PlyElement, make2d, PlyParseError, PlyProperty)

import numpy as np


POINT_COUNT = 2048
POINT_COUNT_STR = str(POINT_COUNT)

#SOURCE_DIR = '/raid/data/tinkercad/point_clouds/manually_clean_ply/' + POINT_COUNT_STR + '/ascii/'
#DEST_DIR = '/raid/data/tinkercad/point_clouds/manually_clean_numpy/' + POINT_COUNT_STR

SOURCE_DIR = "data/ply"
DEST_DIR = "data/numpy"

# Load PLY file
def load_ply_data(filename, point_num):
    plydata = PlyData.read(filename)
#    pc = plydata['vertex'].data[:point_num]
    pc = plydata['vertex'].data
    pc_array = np.array([[x, y, z] for x,y,z in pc])
    return pc_array

def convert(f):
    name, ext = splitext(f)
    in_file = join(SOURCE_DIR, f)
    data = load_ply_data(in_file, POINT_COUNT)
    out_file = join(DEST_DIR, name + ".txt")
    print "Converting file " + f
    np.savetxt(out_file, data, fmt="%.5f")

file_op.ensure_dir_exists(DEST_DIR)
files = file_op.get_only_files(SOURCE_DIR)

p = Pool(multiprocessing.cpu_count())
p.map(convert, files)
