'''
Basic Operations example using TensorFlow library.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

import numpy as np
import tensorflow as tf


a = tf.constant([[1.,2.], [3., 4.], [5.,6.], [7., 8.], [9., 10.]]) 
b = tf.layers.batch_normalization(a, training = True) 



init = tf.initialize_all_variables()


with tf.Session() as sess:
    sess.run(init)
    print (sess.run(a))
    print (sess.run(b))


