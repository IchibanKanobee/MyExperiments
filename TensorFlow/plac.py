import tensorflow as tf
import numpy as np

a = tf.placeholder(tf.float32)
b = tf.Variable(0)
c = np.arange(10)

b = a + 3

with tf.Session() as sess:
    r = sess.run(b, feed_dict={a: c})
    print r
