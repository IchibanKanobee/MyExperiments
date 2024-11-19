import tensorflow as tf
import time

count = 1000

x_input_data = tf.random_normal([count], mean=0, stddev=4)
q = tf.FIFOQueue(count, dtypes = tf.float32, shapes = ())

enqueue_op = q.enqueue_many(x_input_data)

numberOfThreads = 1
qr = tf.train.QueueRunner(q, [enqueue_op] * numberOfThreads)
# Don't forget to add your "QueueRunner" to the QUEUE_RUNNERS collection
tf.train.add_queue_runner(qr)

dequeue_op = q.dequeue_many(count)

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
