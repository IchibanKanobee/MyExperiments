from os import listdir
from os.path import isfile, join, isdir
import os
import shutil


def recreate_new_dir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)


def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def if_file_exists(filename):
    if isfile(filename):
        return True
    else:
        return False


def get_only_files(directory): 
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    return onlyfiles


def get_only_dirs(directory): 
    onlydirs = [f for f in listdir(directory) if isdir(join(directory, f))]
    return onlydirs



