import os
from shutil import copyfile

source_dir = "/raid/data/mvcnn/invbase/train"
dest_dir = "/raid/data/invbase_flat_50k"

import os
from glob import glob
result = [y for x in os.walk(source_dir) for y in glob(os.path.join(x[0], '*.png'))]

size = len(result) 

count = 50000

for i in range(size):
    if (i >= count):
        break

    path_list = result[i].split(os.sep)
    l = len(path_list)
    name = path_list[l-2] + "_" + path_list[l-1]
    dst_name = os.path.join(dest_dir, name)
    copyfile(result[i], dst_name)


