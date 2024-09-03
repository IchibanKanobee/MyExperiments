import tensorflow as tf
from tensorflow.contrib.data import Dataset, Iterator

import os
from glob import glob
from os.path import dirname, join
import cv2
import numpy as np
import sys
from utils import file_op

#TRAIN_DIR = "/raid/data/mvcnn/m40/train"
#TEST_DIR = "/raid/data/mvcnn/m40/test"

TRAIN_DIR = "/media/ara/HDD/data/mvcnn/m40/train"
TEST_DIR = "/media/ara/HDD/data/mvcnn/m40/test"

TFRECORD_DIR = "data/mvcnn/m40/"

BATCH_SIZE = 20
SHAPE = [128, 128]
VIEW_COUNT = 80
EXTENSION = ".png"


def get_labels(root_dir):
    dirs = file_op.get_only_dirs(root_dir)
    return dirs


def get_objects_of_class(root_dir, class_):
    class_dir = join(root_dir, class_)
    objects = file_op.get_only_dirs(class_dir)
    return objects


def get_views_of_object(root_dir, class_, object_, ext):
    views = []
    class_dir = join(root_dir, class_)
    object_dir = join(class_dir, object_)
    files = file_op.get_only_files(object_dir)
    for f in files:
        if (f.endswith(ext)):
            views.append(f)
    return views


def get_full_path(root_dir, class_, object_, view):
    path = join(object_, view)
    path = join(class_, path)
    path = join(root_dir, path)
    return path    


def load_image(addr):
    # read an image and resize to (128, 128)
    img = cv2.imread(addr)
    img = cv2.resize(img, (128, 128), interpolation=cv2.INTER_CUBIC)
    # cv2 load images as BGR, convert it to RGB
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2 load images as BGR, convert it to GRAY
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype(np.float32)
    return img


def _int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def _bytes_feature(value):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def create_tfrecord_file(root_dir, tfrecord_dir):
    labels = get_labels(root_dir)

    for label in labels:
        filename = tfrecord_dir + label + "_tfrecords"
        writer = tf.python_io.TFRecordWriter(filename)

        feature = {}
        label_index = labels.index(label)
        objects = get_objects_of_class(root_dir, label)
        feature['label'] = _int64_feature(label_index)

        for object_ in objects:
            views = get_views_of_object(root_dir, label, object_, EXTENSION)
            view_count = len(views)
            if (view_count != VIEW_COUNT):
            #corrupt directory, skip it
                continue
            feature['view_count'] = _int64_feature(view_count)
            for i in range (view_count):
                path = get_full_path(root_dir, label, object_, views[i])
                img = load_image(path)
                desc_key = "description_" + str(i)
                feature[desc_key] = _bytes_feature(tf.compat.as_bytes(views[i]))
                view_key = "view_" + str(i)
                feature[view_key] = _bytes_feature(tf.compat.as_bytes(img.tostring()))
        
            example = tf.train.Example(features=tf.train.Features(feature=feature))
            writer.write(example.SerializeToString())

        writer.close()
        sys.stdout.flush()

TFRECORD_TRAIN_DIR = TFRECORD_DIR + "train/"
file_op.ensure_dir_exists(TFRECORD_TRAIN_DIR)
create_tfrecord_file(TRAIN_DIR, TFRECORD_TRAIN_DIR)

TFRECORD_TEST_DIR = TFRECORD_DIR + "test/"
file_op.ensure_dir_exists(TFRECORD_TEST_DIR)
create_tfrecord_file(TEST_DIR, TFRECORD_TEST_DIR)
