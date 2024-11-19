import sys
sys.path.append("..")

from utils import file_op
from os.path import join, splitext
import os

import multiprocessing
from multiprocessing import Pool

SOURCE_DIR = '/raid/data/tinkercad/manually_clean_stl'
DEST_DIR = '/raid/data/tinkercad/manually_clean_obj'


def convert(f):
    name, ext = splitext(f)
    in_file = join(SOURCE_DIR, f)
    out_file = join(DEST_DIR, name + ".obj")
    if not file_op.if_file_exists(out_file):
        print "Converting file " + f
        cmd = "meshlabserver -i " + in_file + " -o " + out_file
        os.system(cmd)


file_op.ensure_dir_exists(DEST_DIR)
files = file_op.get_only_files(SOURCE_DIR)

p = Pool(multiprocessing.cpu_count())
p.map(convert, files)
