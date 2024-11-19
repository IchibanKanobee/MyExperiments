import os, shutil
from os import listdir
from os.path import isfile, join


DATA_ROOT = "/raid/data/Images/Grayscale256x256/train"

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def get_only_files(dir):
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
    return onlyfiles


subdirs = get_immediate_subdirectories(DATA_ROOT)

for item in subdirs:
    dir = os.path.join(DATA_ROOT, item)

    files = get_only_files(dir)

    for file in files:
        only_name = os.path.splitext(file)[0]

        dir_for_file = os.path.join(dir, only_name)

        if os.path.exists(dir_for_file):
            shutil.rmtree(dir_for_file)
        os.makedirs(dir_for_file)

        old_path = os.path.join(dir, file)
        new_path = os.path.join(dir_for_file, file)

        shutil.move(old_path, new_path)



