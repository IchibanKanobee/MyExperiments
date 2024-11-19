import tensorflow as tf
tf.reset_default_graph()

import numpy as np

# Batch size = 2, sequence length = 3, number features = 1, shape=(2, 3, 1)
values231 = np.array([
    [1, 2, 3],
    [2, 3, 4]
])

print (values231.shape)

# Batch size = 3, sequence length = 5, number features = 2, shape=(3, 5, 2)
values352 = np.array([
    [[1, 4], [2, 5], [3, 6], [4, 7], [5, 8]],
    [[2, 5], [3, 6], [4, 7], [5, 8], [6, 9]],
    [[3, 6], [4, 7], [5, 8], [6, 9], [7, 10]]
])


tf_values231 = tf.constant(values231, dtype=tf.float32)
lstm_cell = tf.contrib.rnn.LSTMCell(num_units=100)
outputs, state = tf.nn.static_rnn(cell=lstm_cell, dtype=tf.float32, inputs=tf_values231)

print(outputs)
# tf.Tensor 'rnn_3/transpose:0' shape=(2, 3, 100) dtype=float32
print(state.c)
# tf.Tensor 'rnn_3/while/Exit_2:0' shape=(2, 100) dtype=float32
print(state.h)
# tf.Tensor 'rnn_3/while/Exit_3:0' shape=(2, 100) dtype=float32

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    output_run, state_run = sess.run([outputs, state])
    print (output_run)
    print(state_run)
