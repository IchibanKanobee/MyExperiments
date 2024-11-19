from os.path import join, isfile
from shutil import copytree

src_dir = "/raid/data/mvcnn/invbase"
dest_dir = "/raid/invbase"

# ignore any files but files with '.stl' extension
ignore_func = lambda d, files: [f for f in files if isfile(join(d, f)) and f[-4:] != '.stl']
copytree(src_dir, dest_dir, ignore=ignore_func)
