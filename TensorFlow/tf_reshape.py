'''
Basic Operations example using TensorFlow library.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

import numpy as np
import tensorflow as tf


a = tf.constant([[1,2], [3, 4]]) 

shape0 = a.get_shape()
print (shape0)

b = tf.reshape(a, (1,1))
shape1 = b.get_shape()
print (shape1)



tf.initialize_all_variables()


with tf.Session() as sess:
    print (sess.run(a))
    print (sess.run(b))


