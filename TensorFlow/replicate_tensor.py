#https://stackoverflow.com/questions/45315545/replicate-a-row-tensor-using-tf-tile

import tensorflow as tf

vec = tf.constant([1., 2., 3., 4.])
m = 10
matrix = tf.ones([m, 1]) * vec

with tf.Session() as sess:
   print(sess.run([matrix]))

#Output: [[1., 2., 3., 4.],
#         [1., 2., 3., 4.],
#         [1., 2., 3., 4.]]
