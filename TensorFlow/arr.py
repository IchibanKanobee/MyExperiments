import tensorflow as tf


a = tf.zeros([10])
b = tf.constant(5)

a = a + 3
a = a * 5
#a = b * 3 

with tf.Session() as sess:
    r = sess.run(a)
    print r
