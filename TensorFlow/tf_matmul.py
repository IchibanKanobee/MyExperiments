'''
Basic Operations example using TensorFlow library.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

import numpy as np
import tensorflow as tf


a = tf.constant([[1,2], [3, 4]]) 
b = tf.constant([[5,6], [7, 8]]) 

c0 = tf.matmul(a, b)
shape0 = c0.get_shape()
print (shape0)

'''
d = tf.constant([1,2]) 
e = tf.constant([3,4]) 

f = tf.matmul(d, e, transpose_b=True)
shape1 = f.get_shape()
print (shape1)
'''
'''
d = tf.constant([[1,1,1]])
e = tf.constant([[2,2,2], [3,3,3]])
f = tf.matmul(d, e)
shape2 = f.get_shape()
print (shape2)
'''

tf.initialize_all_variables()


with tf.Session() as sess:
    print (sess.run(c0))
#    print (sess.run(f))


