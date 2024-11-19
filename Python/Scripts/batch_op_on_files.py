import os
from os import listdir
from os.path import isfile, isdir, join


ROOT_DIR = '/raid/best_vae_images'


def get_list_of_files(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles


files = get_list_of_files(ROOT_DIR)

for fl in files:
    file_path = join(ROOT_DIR, fl)
    cmd = "python split_image.py -i " + file_path
    os.system(cmd)
