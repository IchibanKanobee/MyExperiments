import numpy as np
import tensorflow as tf


a = tf.constant([[[[17.,2.], [-35., 0.004]], [[17.,2.], [-35., 0.004]]], [[[17.,2.], [-35., 0.004]], [[17.,2.], [-35., 0.004]]]]) 


shape = a.get_shape()
print (shape)


exp = tf.exp(a)
shape = exp.get_shape()
print (shape)

tf.initialize_all_variables()


with tf.Session() as sess:
    print (sess.run(exp))


