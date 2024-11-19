import tensorflow as tf

a = tf.constant('Hello, Tensor Flow!')
#Note tf.Variable("Hello, Tensor Flow!") doesn't work, the argument must be a tensor

with tf.Session() as sess:
    r = sess.run(a)
    print r
