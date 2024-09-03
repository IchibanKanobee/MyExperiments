import tensorflow as tf

#Size of the queue is 3 elements
q = tf.FIFOQueue(3, "float")
init = q.enqueue_many(([1.,1.,1.],))

enq = q.enqueue(2.0)
deq = q.dequeue()
size = q.size()

with tf.Session() as sess:
    sess.run(init)
    print sess.run(size)

    for i in range (10):
        print sess.run(deq)
        print sess.run(size)

        print sess.run(enq)
        print sess.run(size)
