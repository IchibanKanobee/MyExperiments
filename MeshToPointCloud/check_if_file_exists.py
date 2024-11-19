import sys
sys.path.append("..")

from utils import file_op
import json
from os.path import join, splitext


SOURCE_DIR = "/raid/data/tinkercad/sample2/designs_stl"
EXT = ".stl"

with open('categories.json') as f:
    data = json.load(f)

    all_files = []
    existing_files = []
    missing_files = []

    file_list = data.values()
    for files in file_list:
        for f in files:
            name = f + EXT
            path = join(SOURCE_DIR, name)
            all_files.append(name)
            if (file_op.if_file_exists(path)):
                existing_files.append(name)
            else:
                missing_files.append(name)

    all = open('all_files.txt', 'w')
    all.writelines(["%s\n" % item for item in all_files])

    existing = open('existing_files.txt', 'w')
    existing.writelines(["%s\n" % item for item in existing_files])

    missing = open('missing_files.txt', 'w')
    missing.writelines(["%s\n" % item for item in missing_files])


