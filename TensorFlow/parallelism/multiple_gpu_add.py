import numpy as np
import tensorflow as tf

a = np.arange(8)

c = []

gpus = ['/gpu:0', '/gpu:1', '/gpu:2', '/gpu:3']
count = len(gpus)

for i, d in enumerate(gpus):
    with tf.device(d):
        a_t = tf.get_variable("a_t_"+ str(i), initializer = a[i*2])
        b_t = tf.get_variable("b_t_" + str(i), initializer = a[i*2+1])
        c.append(tf.add(a_t, b_t))

with tf.device('/cpu:0'):
    sum_ = tf.add_n(c)

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

init = tf.global_variables_initializer()
sess.run(init)

print (a)
print (sess.run(sum_))
print (sess.run(c))

