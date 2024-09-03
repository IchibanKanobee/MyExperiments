import tensorflow as tf

with tf.device('/gpu:1'):       # Run nodes with GPU 0
    m1 = tf.constant([[3., 5.]])
    m2 = tf.constant([[2.],[4.]])
    product = tf.matmul(m1, m2)    

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess.run(product))

sess.close()
