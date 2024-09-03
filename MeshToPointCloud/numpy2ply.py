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

SOURCE_DIR = "/raid/data/tinkercad/output_point_clouds/pointnet-autoencoder"
DEST_DIR = "/raid/data/tinkercad/output_point_clouds/pointnet-autoencoder-ply"


##########################
def write_point_cloud_to_file(filename, cloud):
    point_count = cloud.shape[0]

    vertex = np.zeros((point_count,),
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

    for i in range (point_count):
        x = cloud[i][0]
        y = cloud[i][1]
        z = cloud[i][2]
        print "x = " + str(x) + "; y = " + str(y) + "; z = " + str(z)
        vertex[i] = (x, y, z)

    el = PlyElement.describe(vertex, 'vertex')
    PlyData([el]).write(filename)


def convert(f):
    name, ext = splitext(f)
    in_file = join(SOURCE_DIR, f)
    np_cloud = np.loadtxt(in_file)
    out_file = join(DEST_DIR, name + ".ply")
    print "Converting file " + f
    write_point_cloud_to_file(out_file, np_cloud)

file_op.ensure_dir_exists(DEST_DIR)
files = file_op.get_only_files(SOURCE_DIR)

p = Pool(multiprocessing.cpu_count())
p.map(convert, files)
