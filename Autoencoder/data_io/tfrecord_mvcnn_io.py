import sys
sys.path.append("../../")
#sys.path.append("../")

import tensorflow as tf
from tensorflow.data import Dataset, Iterator

import os
from glob import glob
from os.path import dirname, join, isdir
import cv2
import numpy as np

from common import quat_utils
from os import listdir
from utils import file_op


SHAPE = (256, 256)
VIEW_COUNT = 80
EXTENSION = ".png"


def get_labels(root_dir):
    dirs = file_op.get_only_dirs(root_dir)
    return dirs


def get_objects_of_class(root_dir, class_, train_or_test):
    class_dir = join(root_dir, class_)
    class_dir = join(class_dir, train_or_test)
    objects = file_op.get_only_dirs(class_dir)
    return objects


def get_views_of_object(root_dir, class_, object_, ext, train_or_test):
    views = []
    class_dir = join(root_dir, class_)
    class_dir = join(class_dir, train_or_test)
    object_dir = join(class_dir, object_)
    files = file_op.get_only_files(object_dir)
    for f in files:
        if (f.endswith(ext)):
            views.append(f)
    return views


def get_full_path(root_dir, class_, object_, train_or_test, view):
    path = join(object_, view)
    path = join(train_or_test, path)
    path = join(class_, path)
    path = join(root_dir, path)
    return path    


def load_image(addr):
    # read an image and resize to (128, 128)
    try:
        img = cv2.imread(addr)
        img = cv2.resize(img, SHAPE, interpolation=cv2.INTER_CUBIC)
    # cv2 load images as BGR, convert it to RGB
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2 load images as BGR, convert it to GRAY
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = img.astype(np.float32)
        return img
    except:
        return None


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



def create_class_tfrecord_files(labels, label, root_dir, tfrecord_dir, train_or_test):
    target_dir = join(tfrecord_dir, train_or_test)
    file_op.ensure_dir_exists(target_dir)
    filename = join(target_dir,label + "_tfrecords" + "_" + train_or_test)
    print("Creating tfrecord file " + filename)
    writer = tf.python_io.TFRecordWriter(filename)

    feature = {}
    label_index = labels.index(label)
    objects = get_objects_of_class(root_dir, label, train_or_test)
    feature['label'] = _int64_feature(label_index)

    for object_ in objects:
        views = get_views_of_object(root_dir, label, object_, EXTENSION, train_or_test)
        view_count = len(views)
        if (view_count != VIEW_COUNT):
            # corrupt directory, skip it
            continue
        feature['view_count'] = _int64_feature(view_count)
        for i in range(view_count):
            path = get_full_path(root_dir, label, object_, train_or_test, views[i])
            img = load_image(path)
            if (img is None):
                break
            desc_key = "description_" + str(i)
            feature[desc_key] = _bytes_feature(tf.compat.as_bytes(views[i]))
            view_key = "view_" + str(i)
            feature[view_key] = _bytes_feature(tf.compat.as_bytes(img.tostring()))

        example = tf.train.Example(features=tf.train.Features(feature=feature))
        writer.write(example.SerializeToString())

    writer.close()
    sys.stdout.flush()


def create_shapenet_tfrecord_files(root_dir, tfrecord_dir):
    labels = get_labels(root_dir)

    for label in labels:
        create_class_tfrecord_files(labels, label, root_dir, tfrecord_dir, "train")
        create_class_tfrecord_files(labels, label, root_dir, tfrecord_dir, "test")


def tfrecord_parser(record):
    file_features={
        'label': tf.FixedLenFeature([], tf.int64),
        'view_count': tf.FixedLenFeature([], tf.int64)
    }
    count = 80  #need to determine view_count dynamically
    for i in range(count):
        desc_key = "description_" + str(i)
        file_features[desc_key] = tf.FixedLenFeature([], tf.string)
        view_key = "view_" + str(i)
        file_features[view_key] = tf.FixedLenFeature([], tf.string)

    parsed_record = tf.parse_single_example(record, file_features)

    images_list = []
    descriptions_list = []

    for i in range (count):
        desc_key = "description_" + str(i)
        view_key = "view_" + str(i)
        descriptions_list.append(parsed_record[desc_key])
        image_decoded = tf.decode_raw(parsed_record[view_key], tf.float32)
        image_resized = tf.reshape(image_decoded, [256, 256])
        images_list.append(image_resized)

    images = images_list[0]
    descriptions = [descriptions_list[0]]

    for i in range (count - 1):
        images = tf.concat([images, images_list[i+1]], 0)
        descriptions = tf.concat([descriptions, [descriptions_list[i+1]]], 0)


    label = tf.cast(parsed_record['label'], tf.int32)
    view_count = tf.cast(parsed_record['view_count'], tf.int32)

    feature = {}
    feature["view_count"] = view_count
    feature["decriptions"] = descriptions
    feature["images"] = images
    feature["label"] = label

    return feature