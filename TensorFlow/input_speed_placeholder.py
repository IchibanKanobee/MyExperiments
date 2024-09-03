import tensorflow as tf
import time
import numpy as np

count = 1000

x_input = np.random.normal(0, 4, count)

x = tf.placeholder(tf.float32)
y = tf.square(x)


start = time.time()

with tf.Session() as sess:
#    print sess.run(x_input)
    print sess.run(y, feed_dict={x: x_input})

end = time.time()

print "Elapsed time: " + str(end - start) + " sec."
