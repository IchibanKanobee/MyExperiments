import sys
sys.path.append("..")

#from utils import file_op
from os.path import join, splitext
import os

from plyfile import (PlyData, PlyElement, make2d, PlyParseError, PlyProperty)


POINT_COUNT = 2048
POINT_COUNT_STR = str(POINT_COUNT)

SOURCE_DIR = '.'
DEST_DIR = '.'

# Load PLY file
def load_ply_data(filename, point_num):
    plydata = PlyData.read(filename)
    pc = plydata['vertex'].data[:point_num]
    pc_array = np.array([[x, y, z] for x,y,z in pc])
    return pc_array

def convert(f):
    name, ext = splitext(f)
    in_file = join(SOURCE_DIR, f)
    data = load_ply_data(in_file, POINT_COUNT)
    out_file = join(DEST_DIR, name + ".txt")
    print "Converting file " + f
    np_.savetxt(out_file, data, fmt="%.5f")


convert('airplane.ply')
