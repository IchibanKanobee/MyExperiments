'''
Basic Operations example using TensorFlow library.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

import numpy as np
import tensorflow as tf

#matrix1 = tf.constant([[3., 3.]])


# Create another Constant that produces a 2x1 matrix.
#matrix2 = tf.constant([[2.],[2.]])

#product = tf.matmul(matrix1, matrix2)

#add = matrix1[0,0]
#output = matrix1[0, :]

d = tf.constant([[1,2], [3,4]])
shape = d.get_shape()

dim = shape[0] * shape[1]
val = dim.value

e = tf.zeros_like(d)
e = tf.reshape(e, [1, dim.value])

nar = np.zeros(dim.value)

#nar = tf.Session().run(d)


for i in range (0, shape[0]):
    for j in range (0, shape[1]):
        nar[i*j + j] = d[i,j]

with tf.Session() as sess:
 #   result = sess.run(product)
 #   print(result)
    print (shape)
    print dim
    print sess.run(e)
    print nar
  #  print sess.run(output)
  #  print sess.run(add)


