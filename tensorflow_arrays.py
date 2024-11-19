import tensorflow as tf
import numpy as np

y = tf.Variable(0)

def reduce_merge(a):
  sh = a.get_shape() 
  a = sh[0]
  b = sh[1] * sh[2]
  data = np.zeros((a, b))

  for i in range (0, a):
    for j in range (0, b):
      data[i, j] = i + j
   
  return data

c = tf.constant([[[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [10.0, 11.0, 12.0, 13.0]], [[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [10.0, 11.0, 12.0, 13.0]]])
print (c.get_shape())

init = tf.initialize_all_variables()

with tf.Session() as sess:
  # Run the init operation.
  sess.run(init)
  sh = c.get_shape() 
  a = sh[0]
  b = sh[1] * sh[2]
  y = y.reshape(a, b)
  print y.get_shape()

#  res = reduce_merge(c)
#  y = (res + 5)
#  print sess.run(y)

