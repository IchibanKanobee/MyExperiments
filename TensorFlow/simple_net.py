import tensorflow as tf
import time

sample_size = 1024
sample_count = 1000

x_input_data = tf.random_uniform([sample_size, sample_count], -10.0, 10.0)

x_sample = tf.placeholder([sample_count]. dtypes = tf.float32)
y = tf.cast((tf.reduce_mean(x_sample) > 0), tf.int32)

fc = tf.random_uniform([sampe_size, sample_size], -1.0, 1.0)
b1 = tf.random_uniform([sample_size], -1.0, 1.0)
out11 = tf.add(b1 + tf.mult(x_sample, fc))
out1 = tf.nn.sigmoid(out11)

fc2 = tf.random_uniform([sampe_size], -1.0, 1.0)
b2 = tf.random_uniform([], -1.0, 1.0)
out2 = tf.add(b2 + tf.mult(out1, fc2))
out = tf.nn.sigmoid(out2)


q = tf.FIFOQueue(sample_count, dtypes = tf.float32, shapes = (sample_size,))

loss = 
accuracy = 

enqueue_op = q.enqueue_many(x_input_data)

numberOfThreads = 1
qr = tf.train.QueueRunner(q, [enqueue_op] * numberOfThreads)
# Don't forget to add your "QueueRunner" to the QUEUE_RUNNERS collection
tf.train.add_queue_runner(qr)

dequeue_op = q.dequeue_many(sample_size)

y = tf.square(dequeue_op)


start = time.time()

with tf.Session() as sess:
#    print sess.run(x_input_data)
    sess.run(tf.global_variables_initializer())
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    print sess.run(y)
    
    coord.request_stop()
    coord.join(threads)

 
end = time.time()

print "Elapsed time: " + str(end - start) + " sec."
