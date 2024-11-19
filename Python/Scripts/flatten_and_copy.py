import os
from shutil import copyfile

source_dir = "/media/ara/HDD/data/mvcnn/invbase/train/Fasteners-Bolts-Countersunk"
dest_dir = "/media/ara/HDD/data/Fasteners-Bolts-Countersunk"

import os
from glob import glob
result = [y for x in os.walk(source_dir) for y in glob(os.path.join(x[0], '*.png'))]

size = len(result) 

for i in range(size):
    path_list = result[i].split(os.sep)
    l = len(path_list)
    name = path_list[l-2] + "_" + path_list[l-1]
    dst_name = os.path.join(dest_dir, name)
    copyfile(result[i], dst_name)


