import tensorflow as tf
from tensorflow.contrib.data import Dataset, Iterator

import os
from glob import glob
from os.path import dirname
import cv2
import numpy as np
import sys

TRAIN_DIR = "/raid/data/cnn/m40/train"
TEST_DIR = "/raid/data/cnn/m40/test" 
DATA_DIR = "data/cnn/"

#TRAIN_DIR = "/media/ara/HDD/data/cnn/m40/train"
#TEST_DIR = "/media/ara/HDD/data/cnn/m40/test"


BATCH_SIZE = 20
SHAPE = [128, 128]

def get_labels_from_files(files):
    labels = []
    for f in files:
        directory = dirname(f)
        dirs = directory.split('/')
        dirs_len = len(dirs)
        labels.append(dirs[dirs_len - 1])
    return labels


def convert_labels_to_numbers(labels, classes):
    label_numbers = []
    label_count = len(labels)
    class_count = len(classes)
    for i in range (label_count):
        for j in range (class_count):
            if labels[i] == classes[j]:
                label_numbers.append(j)
    return label_numbers


def load_image(addr):
    # read an image and resize to (128, 128)
    # cv2 load images as BGR, convert it to RGB
    img = cv2.imread(addr)
    img = cv2.resize(img, (128, 128), interpolation=cv2.INTER_CUBIC)
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2 load images as BGR, convert it to GRAY
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype(np.float32)
    return img


def _int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def _bytes_feature(value):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


train_files = [y for x in os.walk(TRAIN_DIR) for y in glob(os.path.join(x[0], '*.png'))]
train_labels = get_labels_from_files(train_files)

classes = list(set(train_labels))
CLASS_COUNT = len(classes)


numeric_train_classes = convert_labels_to_numbers(train_labels, classes)

train_filename = DATA_DIR + "train_tfrecords"

writer = tf.python_io.TFRecordWriter(train_filename)


for i in range (len(train_files)):
    img = load_image(train_files[i])
    label = numeric_train_classes[i]

    feature = {'label': _int64_feature(label),
               'image': _bytes_feature(tf.compat.as_bytes(img.tostring()))}


    example = tf.train.Example(features=tf.train.Features(feature=feature))

    writer.write(example.SerializeToString())

writer.close()
sys.stdout.flush()


test_files = [y for x in os.walk(TEST_DIR) for y in glob(os.path.join(x[0], '*.png'))]
test_labels = get_labels_from_files(test_files)
numeric_test_classes = convert_labels_to_numbers(test_labels, classes)


test_filename = DATA_DIR + "test_tfrecords"

writer = tf.python_io.TFRecordWriter(test_filename)


for i in range (len(test_files)):
    img = load_image(test_files[i])
    label = numeric_test_classes[i]

#    feature = {'test/label': _int64_feature(label),
#               'test/image': _bytes_feature(tf.compat.as_bytes(img.tostring()))}

    feature = {'label': _int64_feature(label),
               'image': _bytes_feature(tf.compat.as_bytes(img.tostring()))}


    example = tf.train.Example(features=tf.train.Features(feature=feature))

    writer.write(example.SerializeToString())

writer.close()
sys.stdout.flush()    


