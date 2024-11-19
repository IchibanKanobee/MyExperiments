import tensorflow as tf

start = 3
limit = 18
delta = 3

param = tf.range(start, limit, delta)
ind = tf.constant([3, 1, 4])
gath = tf.gather(param, ind)

with tf.Session() as sess:
    p, g = sess.run([param, gath])
    print p
    print g
