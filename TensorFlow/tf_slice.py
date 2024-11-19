import tensorflow as tf

t = tf.constant([[1, 1], [2, 2], [3,3], [4,4], [5, 5]])
print t.shape

t1 = tf.slice(t, (0, 0), (3, 2))
t2 = tf.slice(t, (3, 0), (2, 2))

with tf.Session() as sess:
    print(sess.run(t))
    print(sess.run(t1)) #[[1, 1], [2, 2], [3,3]]
    print(sess.run(t2)) #[[4,4], [5, 5]]

