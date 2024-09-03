import sys
sys.path.append("..")

from utils import file_op
from os.path import join, splitext
import os

SOURCE_DIR = '/raid/data/tinkercad/sample2/processed_20_views'
DEST_DIR = '/raid/data/tinkercad/sample2/processed_thumbnails'

file_op.ensure_dir_exists(DEST_DIR)
dirs = file_op.get_only_dirs(SOURCE_DIR)

for d in dirs:
    files = file_op.get_only_files(join(SOURCE_DIR, d))
    files.sort()
    source_file = join(d, files[0])
    source_file = join(SOURCE_DIR, source_file)
    dest_file = join(DEST_DIR, d + "_" + files[0])
    cmd = "cp " + source_file + " " + dest_file 
    os.system(cmd)

