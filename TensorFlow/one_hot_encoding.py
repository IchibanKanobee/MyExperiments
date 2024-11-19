#https://stackoverflow.com/questions/42092508/how-can-i-encode-labels-in-tensorflow

import tensorflow as tf
import numpy as np


def get_numeric_labels(labels):
    label_count = len(labels)
    numeric_labels = np.zeros(label_count)
    classes = list(set(labels))
    class_count = len(classes)
    for i in range (label_count):
        for j in range(class_count):
            if (labels[i]==classes[j]):
                numeric_labels[i] = j
    return class_count, numeric_labels


labels = ["apple", "apple", "pear", "plum", "cherry", "cherry"]
#class_count = len(set(classes))

class_count, numeric_labels = get_numeric_labels(labels)
print numeric_labels


tf_labels= tf.constant(numeric_labels, tf.int64)
depth = tf.constant(class_count)
one_hot_encoded = tf.one_hot(indices=tf_labels, depth=depth)


with tf.Session():
  print(one_hot_encoded.eval())

