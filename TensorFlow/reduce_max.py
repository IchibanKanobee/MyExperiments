import tensorflow as tf

'''
init = tf.constant([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
shape = tf.shape(init)
red0 = tf.reduce_max(init, axis=0)
shape0 = tf.shape(red0)
red1 = tf.reduce_max(init, axis=1)
shape1 = tf.shape(red1)
red2 = tf.reduce_max(init, axis=2)
shape2 = tf.shape(red2)


sess = tf.Session()

print (sess.run(init))
print (sess.run(shape))
print ("---------------\n")

print(sess.run(red0))
print (sess.run(shape0))
print ("---------------\n")

print(sess.run(red1))
print (sess.run(shape1))
print ("---------------\n")

print(sess.run(red2))
print (sess.run(shape2))
print ("---------------\n")
'''

init = tf.constant([[1, 5, 3], [4, 2, 6]])
shape = tf.shape(init)
red0 = tf.reduce_max(init, axis=0)
shape0 = tf.shape(red0)

sess = tf.Session()

print (sess.run(init))
print (sess.run(shape))
print ("---------------\n")

print(sess.run(red0))
print (sess.run(shape0))
print ("---------------\n")


'''
output

'''
