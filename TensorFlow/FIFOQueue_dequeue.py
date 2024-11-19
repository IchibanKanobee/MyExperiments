import tensorflow as tf

#Size of the queue is 3 elements
q = tf.FIFOQueue(3, "float")
init = q.enqueue_many(([1.,2.,3.],))

#Get the first element
deq = q.dequeue()
size = q.size()

with tf.Session() as sess:
    sess.run(init)
    print sess.run(size)

    print sess.run(deq)
    print sess.run(size)

    print sess.run(deq)
    print sess.run(size)

    print sess.run(deq)
    print sess.run(size)
