'''
Basic Operations example using TensorFlow library.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

import numpy as np
import tensorflow as tf


a = tf.constant([[1,2], [3, 4]]) 
b = tf.constant([[5,6], [7, 8]]) 

c0 = tf.concat([a, b], 0)
shape0 = c0.get_shape()
print (shape0)

c1 = tf.concat([a, b], 1)
shape1 = c1.get_shape()
print (shape1)



tf.initialize_all_variables()


with tf.Session() as sess:
    print (sess.run(c0))
    print (sess.run(c1))


