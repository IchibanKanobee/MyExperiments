import tensorflow as tf

a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])
mult = tf.constant([5])
b = tf.tile(a, mult)
with tf.Session() as sess:
    print(sess.run(a))
    print(sess.run(b))
