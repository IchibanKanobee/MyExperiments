import os
from shutil import copyfile
from utils import file_op
from os.path import join


source_dir = "/media/ara/HDD/data/mvcnn/m40"
dest_dir = "/media/ara/HDD/data/cnn/m40"


def get_first_file_with_ext(files, ext):
    for f in files:
        filename, file_extension = os.path.splitext(f)
        if (file_extension == ext):
            return f


train_test = file_op.get_only_dirs(source_dir)
for top_dirs in train_test:
    top_dirs_path = join(source_dir, top_dirs)
    classes = file_op.get_only_dirs(top_dirs_path)
    for class_ in classes:
        target_dir_1 = join(dest_dir, top_dirs)
        target_dir = join(target_dir_1, class_)
        class_path = join(top_dirs_path, class_)
        subclasses = file_op.get_only_dirs(class_path)
        for subclass in subclasses:
            subclass_path = join(class_path, subclass)
            files = sorted(file_op.get_only_files(subclass_path))
            source_file = get_first_file_with_ext(files, ".png")
            if source_file is not None:
                source_path = join(subclass_path, source_file)
                file_op.ensure_dir_exists(target_dir)
                target_file = subclass + "_" + source_file
                target_path = join(target_dir, target_file)
                print "Copying file " + source_path         
                copyfile(source_path, target_path)
 
