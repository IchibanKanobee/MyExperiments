import tensorflow as tf

init3 = tf.constant([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 10], [21, 22, 23, 24]]])
shape3 = tf.shape(init3)

def gather_axis(params, indices, axis=0):
    return tf.stack(tf.unstack(tf.gather(tf.unstack(params, axis=axis), indices)), axis=axis)

ind = tf.random_shuffle(tf.range(0, 3))

shuffled_along_axis_1 = gather_axis(init3, ind, 1)

sess = tf.Session()
print (sess.run(init3))
print (sess.run(shape3))
print (sess.run(ind))
print (sess.run(shuffled_along_axis_1))


'''
Output
[[[ 1  2  3  4]
  [ 5  6  7  8]
  [ 9 10 11 12]]

 [[13 14 15 16]
  [17 18 19 10]
  [21 22 23 24]]]
[2 3 4]
[1 2 0]
[[[ 1  2  3  4]
  [ 9 10 11 12]
  [ 5  6  7  8]]

 [[13 14 15 16]
  [21 22 23 24]
  [17 18 19 10]]]
'''

