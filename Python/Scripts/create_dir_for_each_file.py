from os import listdir, mkdir, rename, rmdir
from os.path import isdir, isfile, join, basename, splitext, exists

ROOT_DIR = '/raid/best_vae_images'


def get_only_files(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles

files = get_only_files(ROOT_DIR)
print files

for f2 in files:
    orig = join(ROOT_DIR, f2)
    #print orig
    dir_name = splitext(orig)[0]
    #print dir_name
    if not exists (dir_name):
        mkdir(dir_name)
    target = join(dir_name, f2)
    print orig, target
    rename(orig, target)
            


