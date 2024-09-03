'''
Basic Operations example using TensorFlow library.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

import numpy as np
import tensorflow as tf


a = tf.constant([[1,2], [3, 4]]) #Must have rank 2 - a matrix


shape = a.get_shape()
print shape

#pa = tf.constant([[0,0], [1,0]])
pa = tf.constant([[0,0], [0,5]])
#b = tf.constant([3,4])

pada = tf.pad(a, pa)

tf.initialize_all_variables()


with tf.Session() as sess:
    print sess.run(a)
    res = sess.run(pada)
    print res


