import numpy as np
from plyfile import plyfile
from point_cloud import box
import os

def get_point_cloud_from_file(name):
    plydata = plyfile.PlyData.read(name)
    data = plydata.elements[0].data
    arr = np.fromiter(data, dtype=[('x', '<f4'), ('y', '<f4'), ('z', '<f4')])
    return arr

directory = "data/boxes"

from os import listdir
from os.path import isfile, join
files = [f for f in listdir(directory) if isfile(join(directory, f))]


for file in files:
    name = join(directory, file)
    arr = get_point_cloud_from_file(name)
    print arr

