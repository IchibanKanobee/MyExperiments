import numpy as np
from utils import array_2D
import tensorflow as tf

max_value = tf.placeholder(tf.int64, shape=[])
dataset = tf.data.Dataset.range(max_value)
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()

#Initialize an ietartor over Dataset with 10  elements:
sess = tf.Session()
sess.run(iterator.initializer, feed_dict={max_value:10})
for i in range (10):
    value = sess.run(next_element)
    print value

#Initialize the same ietartor over Dataset with 100  elements:
sess.run(iterator.initializer, feed_dict={max_value:100})
for i in range (100):
    value = sess.run(next_element)
    print value


