from os import listdir, makedirs, rename, path
from os.path import isfile, isdir, join

ROOT_DIR = '/media/ara/HDD/TechSummitImages/vae_shapeNet_yaw_changing_100_views'

images = [f for f in listdir(ROOT_DIR) if isfile(join(ROOT_DIR, f))]

for image in images:
    ind = image.index("_separated")
    directory = join(ROOT_DIR, image[:ind])
    old_file = join(ROOT_DIR, image)
    new_file = join(directory, image)
    if not path.exists(directory):
        makedirs(directory)
    rename(old_file, new_file)
