import tensorflow as tf

init2 = tf.constant([[1, 2], [3, 4], [5, 6]])
shape2 = tf.shape(init2)
shuff2 = tf.random_shuffle(init2)

sess = tf.Session()
print (sess.run(init2))
print (sess.run(shape2))
print(sess.run(shuff2))

'''
output
[[1 2]
 [3 4]
 [5 6]]

[3 2]

[[5 6]
 [1 2]
 [3 4]]
'''

init3 = tf.constant([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
shape3 = tf.shape(init3)
shuff3 = tf.random_shuffle(init3)

print (sess.run(init3))
print (sess.run(shape3))
print(sess.run(shuff3))

'''
output
[[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]]

 [[10 11 12]
  [13 14 15]
  [16 17 18]]]

[2 3 3]

[[[10 11 12]
  [13 14 15]
  [16 17 18]]

 [[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]]]
'''
