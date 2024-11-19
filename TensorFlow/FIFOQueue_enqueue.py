import tensorflow as tf

#Size of the queue is 3 elements
q = tf.FIFOQueue(3, "float")
enq = q.enqueue(1.0)

size = q.size()

with tf.Session() as sess:
    sess.run(enq)
    print sess.run(size)

    sess.run(enq)
    print sess.run(size)

    sess.run(enq)
    print sess.run(size)
