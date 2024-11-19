#Based on https://kratzert.github.io/2017/06/15/example-of-tensorflows-new-input-pipeline.html

import tensorflow as tf
from tensorflow.contrib.data import Dataset, Iterator

import os
from glob import glob
from os.path import dirname

TRAIN_DIR = "/raid/data/cnn/m40/train"
TEST_DIR = "/raid/data/cnn/m40/test" 
BATCH_SIZE = 20

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


def input_parser(img_path, label):
    one_hot = tf.one_hot(label, CLASS_COUNT)

    img_file = tf.read_file(img_path)
    img_decoded = tf.image.decode_image(img_file, channels=1)
    return img_decoded, one_hot


def get_dataset(images, labels, batch_size):
    data = Dataset.from_tensor_slices((images, labels))
    data = data.map(input_parser)
    data = data.shuffle(buffer_size = 10000)
    data = data.batch(batch_size)
    return data


train_files = [y for x in os.walk(TRAIN_DIR) for y in glob(os.path.join(x[0], '*.png'))]
train_labels = get_labels_from_files(train_files)

classes = list(set(train_labels))
CLASS_COUNT = len(classes)

train_classes = convert_labels_to_numbers(train_labels, classes)

test_files = [y for x in os.walk(TEST_DIR) for y in glob(os.path.join(x[0], '*.png'))]
test_labels = get_labels_from_files(test_files)
test_classes = convert_labels_to_numbers(test_labels, classes)

train_images = tf.constant(train_files)
train_labels = tf.constant(train_classes)

test_images = tf.constant(test_files)
test_labels = tf.constant(test_classes)

#Create Dataset objects
train_data = get_dataset(train_images, train_labels, BATCH_SIZE)
test_data = get_dataset(test_images, test_labels, BATCH_SIZE)


#Create Iterator object
iterator = Iterator.from_structure(train_data.output_types, train_data.output_shapes)
next_element = iterator.get_next()

#Create two initializations to switch between datasets
train_init_op = iterator.make_initializer(train_data)
test_init_op = iterator.make_initializer(test_data)


with tf.Session() as sess:
    sess.run(train_init_op)

    while(True):
        try:
            elem = sess.run(next_element)
            print elem
            print "------------------------"
        except tf.errors.OutOfRangeError:
            print ("End of training dataset")
            break



    sess.run(test_init_op)

    while(True):
        try:
            elem = sess.run(next_element)
            print elem
            print "------------------------"
        except tf.errors.OutOfRangeError:
            print ("End of testing dataset")
            break

#    print sess.run(train_labels)
