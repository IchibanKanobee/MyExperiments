import os
from os import listdir
from os.path import isfile, isdir, join


ROOT_DIR = '/raid/best_vae_images'


def get_list_of_dirs(mypath):
    onlydirs = [f for f in listdir(mypath) if isdir(join(mypath, f))]
    return onlydirs


def get_list_of_files(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles


dirs = get_list_of_dirs(ROOT_DIR)

for dr in dirs:
    dir_path = join(ROOT_DIR, dr)
    files = get_list_of_files(dir_path)
    for fl in files:
        file_path = join(dir_path, fl)
        cmd = "python split_image.py -i " + file_path
        os.system(cmd)
