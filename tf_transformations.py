import numpy as np
import tensorflow as tf

x = np.arange(720)
y = x.reshape(2,3,4,5,6)

a = tf.Variable(y)
shape = a.get_shape()
print shape

t1 = tf.constant([[1,2],[3,4]])
t2 = tf.constant([[5,6],[7,8]])

c1 = tf.concat(0, [t1, t2])
c2 = tf.concat(1, [t1, t2])


init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    print sess.run(c1)
    print sess.run(c2)

