import tensorflow as tf

from tensorflow.python.framework import ops
from tensorflow.python.framework import dtypes

from os import listdir
from os.path import isfile, join, isdir

import numpy as np
import scipy.misc

ROOT = "/raid/data/ArnoldRendering/Train"

epochs = 10
BATCH_SIZE = 5

IMAGE_HEIGHT = 512
IMAGE_WIDTH = 512
NUM_CHANNELS = 3

def get_files(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles


def get_directories(root):
    onlydirs = [f for f in listdir(root) if isdir(join(root, f))]
    return onlydirs


def get_label_dict(root):
    dic = {}
    dirs = get_directories(root)
    for i, d in enumerate(dirs):
        dic[d] = i
    return dic

def get_files_and_labels(root):
    label_dic = get_label_dict(root)

    files = []
    labels = []

    dirs = get_directories(root)

    for d in dirs:
        l = int(label_dic[d])
        dr = join(ROOT, d)
        fl = get_files(dr)
        for f in fl:
            labels.append(l)
            files.append(join (dr, f))

    print labels

    return files, labels


file_list, label_list = get_files_and_labels(ROOT)

#count = len(file_list)

#tf_images = ops.convert_to_tensor(file_list, dtype=dtypes.string)
tf_images = tf.convert_to_tensor(file_list)

#tf_labels = ops.convert_to_tensor(label_list, dtype=dtypes.int32)
tf_labels = tf.convert_to_tensor(label_list)


img, label = tf.train.slice_input_producer([tf_images, tf_labels],
                                            shuffle = True)

file_contents = tf.read_file(img)
image = tf.image.decode_jpeg(file_contents, channels=3)


image.set_shape([IMAGE_HEIGHT, IMAGE_WIDTH, NUM_CHANNELS])

image_batch, label_batch = tf.train.batch([image, label], batch_size=BATCH_SIZE)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    for i in range(epochs):
#        l = label.eval()
#        image_array = image.eval()
#        img_name = "image_" + str(i) + ".jpg"
#        scipy.misc.imsave(img_name, image_array)
#        print l
        lb = label_batch.eval()
        print lb

    coord.request_stop()
    coord.join(threads)
    sess.close()



