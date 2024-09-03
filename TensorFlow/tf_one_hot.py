'''
Basic Operations example using TensorFlow library.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

import numpy as np
import tensorflow as tf


indices = [0, 3, 7]
depth = 10
one_hot = tf.one_hot(indices, depth)


tf.initialize_all_variables()


with tf.Session() as sess:
    print (sess.run(one_hot))


