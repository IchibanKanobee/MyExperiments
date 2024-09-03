#requires tensorflow 1.3

import tensorflow as tf

#unif_10 = tf.constant([-9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, #4.0, 5.0, 6.0, 7.0, 8.0, 9.0])

#unif_10 = tf.constant([-9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0])

unif_10 = tf.constant([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])


mean, variance = tf.nn.moments(unif_10, axes=[0])
offset_0 = tf.constant(0.0)
scale_0 = tf.constant(1.0)
variance_epsilon = tf.constant(0.00001)
#out1 = tf.nn.batch_normalization(unif_10, mean, variance, offset_0, scale_0, variance_epsilon)
out1 = tf.nn.batch_normalization(unif_10, mean, variance, None, None, variance_epsilon)
restored = tf.multiply(out1, tf.sqrt(variance)) + mean 

with tf.Session() as sess:
    print (sess.run(unif_10))
    print (sess.run(mean))
    print (sess.run(variance))
    print (sess.run(offset_0))
    print (sess.run(scale_0))
    print (sess.run(variance_epsilon))

    print (sess.run(out1))
    print (sess.run(restored))

#results
#[-1.64314032 -1.46056914 -1.27799797 -1.0954268  -0.91285574 -0.73028457
# -0.5477134  -0.36514229 -0.18257114  0.          0.18257114  0.36514229
#  0.5477134   0.73028457  0.91285574  1.0954268   1.27799797  1.46056914
#  1.64314032]

#[-1.56660402 -1.21846974 -0.87033546 -0.52220118 -0.17406714  0.17406714
#  0.52220142  0.87033558  1.21846986  1.56660402]

#[-1.56660402 -1.21846986 -0.87033558 -0.52220142 -0.17406714  0.17406714
#  0.52220118  0.87033546  1.21846974  1.56660402]




