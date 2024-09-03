import tensorflow as tf


a = tf.Variable(2)
b = tf.constant(5)

#a = b + 3
a = b * 3 

with tf.Session() as sess:
    r = sess.run(a)
    print r
