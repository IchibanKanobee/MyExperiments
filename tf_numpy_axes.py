# Numpy axis is the same as dimension.One dimensional array has 1 axis, 2 dimensional - 2 axises, 3D - 3 axises, and so on. Along axis means that all other dimensions are fixed, the only dimension that changes the index is the axis in question. For example, if we have a 2D array a00, a01, a10, a11, then along axis 0 meand a00, a10, which is the column of the matrix; along axis 1 means a00, a01, which is the row of the matrix. Let us look at some examples.

import tensorflow as tf
import numpy as np

t1 = tf.Variable([[1,2,3],[4,5,6]])
t2 = tf.Variable([[7,8,9],[10,11,12]])

s0 = tf.reduce_sum(t1)
s1 = tf.reduce_sum(t1, 0)
s2 = tf.reduce_sum(t1, 1)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    print sess.run(s0)
    print sess.run(s1)
    print sess.run(s2)
