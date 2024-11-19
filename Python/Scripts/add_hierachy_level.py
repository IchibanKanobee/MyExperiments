from os import listdir, mkdir, rename, rmdir
from os.path import isdir, isfile, join, basename, splitext, exists

ROOT_DIR = 'RGB256x256_formatted'

def get_only_dirs(path):
    onlydirs = [f for f in listdir(path) if isdir(join(path, f))]
    return onlydirs

def get_only_files(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles

dir1 = get_only_dirs(ROOT_DIR)
print dir1

for dr1 in dir1:
    path1 = join(ROOT_DIR, dr1)
    dir2 = get_only_dirs(path1)
#    print dir2
    for dr2 in dir2:
        path2 = join(path1, dr2)
        file2 = get_only_files(path2)
#        print file2
        for f2 in file2:
            orig = join(path2, f2)
            #print orig
            dir_name = splitext(orig)[0]
            #print dir_name
            if not exists (dir_name):
                mkdir(dir_name)
            target = join(dir_name, f2)
            print orig, target
            rename(orig, target)
            


