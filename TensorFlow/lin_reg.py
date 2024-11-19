import tensorflow as tf
import numpy as np

rng = np.random

learning_rate = 0.0001
epochs = 100000

x_input = np.arange(10)

count = len(x_input)

y_input = np.arange(10)

l = len(y_input)

for i in range (l):
    y_input[i] = y_input[i] + np.random.uniform(-1,1)

y_input = 3 * y_input + 5
print y_input

x = tf.placeholder("float")
target = tf.placeholder("float")
a = tf.Variable(6., name= "weight")
b = tf.Variable(8., name = "bias")
y = tf.add(tf.multiply(a, x), b)

loss = tf.reduce_sum(tf.pow(y - target, 2))/(2*count)
opt = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for i in range(epochs):
       A, B, L, O= sess.run([a, b, loss, opt], feed_dict={x: x_input, target: y_input})
       print A, B, L


