import tensorflow as tf
import time

sample_size = 1024
sample_count = 1000

x_input_data = tf.random_uniform([sample_count, sample_size], -10.0, 10.0)
y_output_data = tf.cast(tf.reduce_mean(x_input_data, axis = 1, keep_dims = True) > 0, tf.int32)

sample = tf.placeholder(dtype = tf.float32, shape = [None, sample_size])
res = tf.placeholder(tf.int32, shape = [None, 1])

#Network
w = tf.get_variable('w', shape = [sample_size, sample_size], initializer = tf.random_normal_initializer(stddev=1e-1))
b = tf.get_variable('b', shape = [sample_size], initializer = tf.constant_initializer(0.1))
z = tf.matmul(sample, w) + b
y = tf.nn.relu(z)

#y is tensor of shape [None, 1024] and dtype = float32
#we want to get to [None, 1] with dtype = int32

w2 = tf.get_variable('w2', shape = [sample_size, 1], initializer = tf.random_normal_initializer(stddev=1e-1))
b2 = tf.get_variable('b2', shape = [1], initializer = tf.constant_initializer(0.1))
z = tf.matmul(sample, w2) + b2

losses = tf.nn.sigmoid_cross_entropy_with_logits(None, tf.cast(y_output_data, tf.float32), z)
loss_op = tf.reduce_mean(losses)

pred = tf.cast(z > 0, tf.int32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(pred, res), tf.float32))
accuracy = tf.Print(accuracy, data=[accuracy], message="accuracy:")

adam = tf.train.AdamOptimizer(1e-2)
train_op = adam.minimize(loss_op, name = "train_op")



start = time.time()

with tf.Session() as sess:
#    print sess.run(x_input_data)
    sess.run(tf.global_variables_initializer())

    #accuracy before training
    x_input, y_input = sess.run([x_input_data, y_output_data])
    sess.run(accuracy, feed_dict={sample:x_input, res:y_input})

    for i in range (5000):
        x_input, y_input = sess.run([x_input_data, y_output_data])
        _, loss = sess.run([train_op, loss_op], feed_dict={sample:x_input, res:y_input})

        if (i % 500 == 0):
            print('iter:%d - loss:%f' % (i, loss))



     #check final accuracy
    x_input, y_input = sess.run([x_input_data, y_output_data])
    sess.run(accuracy, feed_dict={sample: x_input, res: y_input})

end = time.time()

print "Elapsed time: " + str(end - start) + " sec."
