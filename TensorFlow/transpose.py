import tensorflow as tf

init3 = tf.constant([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 10], [21, 22, 23, 24]]])
shape3 = tf.shape(init3)

#ind = tf.random_shuffle(tf.range(0, 3))

perm = tf.constant([1, 0, 2])

shuffled = tf.transpose(init3, perm)
shape_transp = tf.shape(shuffled)

sess = tf.Session()
print (sess.run(init3))
print (sess.run(shape3))
print (sess.run(perm))
print (sess.run(shuffled))
print (sess.run(shape_transp))


