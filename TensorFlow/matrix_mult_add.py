import tensorflow as tf

x = tf.Variable([1.0, 2.0])
a = tf.Variable([[2.0, 2.0],[3.0, 3.0]])
b = tf.Variable([3.0, 3.0])

m= tf.multiply(a, x)
s = tf.add(m, b)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print sess.run(m)
    print sess.run(s)
