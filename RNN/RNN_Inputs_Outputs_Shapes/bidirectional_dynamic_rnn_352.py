import tensorflow as tf

import numpy as np

# Batch size = 2, sequence length = 3, number features = 1, shape=(2, 3, 1)
values231 = np.array([
    [[1], [2], [3]],
    [[2], [3], [4]]
])


# Batch size = 3, sequence length = 5, number features = 2, shape=(3, 5, 2)
values352 = np.array([
    [[1, 4], [2, 5], [3, 6], [4, 7], [5, 8]],
    [[2, 5], [3, 6], [4, 7], [5, 8], [6, 9]],
    [[3, 6], [4, 7], [5, 8], [6, 9], [7, 10]]
])

print (values352.shape)


tf.reset_default_graph()

tf_values231 = tf.constant(values352, dtype=tf.float32)

lstm_cell_fw = tf.contrib.rnn.LSTMCell(100)
lstm_cell_bw = tf.contrib.rnn.LSTMCell(105) # change to 105 just so can see the effect in output

(output_fw, output_bw), (output_state_fw, output_state_bw) = tf.nn.bidirectional_dynamic_rnn(
    cell_fw=lstm_cell_fw, 
    cell_bw=lstm_cell_bw, 
    inputs=tf_values231,
    dtype=tf.float32)
    
print(output_fw)
# tf.Tensor 'bidirectional_rnn/fw/fw/transpose:0' shape=(2, 3, 100) dtype=float32
print(output_bw)
# tf.Tensor 'ReverseV2:0' shape=(2, 3, 105) dtype=float32
print(output_state_fw.c)
# tf.Tensor 'bidirectional_rnn/fw/fw/while/Exit_2:0' shape=(2, 100) dtype=float32
print(output_state_fw.h)
# tf.Tensor 'bidirectional_rnn/fw/fw/while/Exit_3:0' shape=(2, 100) dtype=float32
print(output_state_bw.c)
# tf.Tensor 'bidirectional_rnn/bw/bw/while/Exit_2:0' shape=(2, 105) dtype=float32
print(output_state_bw.h)
# tf.Tensor 'bidirectional_rnn/bw/bw/while/Exit_3:0' shape=(2, 105) dtype=float32

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    output_fw_run, output_bw_run, output_state_fw_run, output_state_bw_run = sess.run([output_fw, output_bw, output_state_fw, output_state_bw])
    print(output_fw_run)
    print(output_bw_run)
    print(output_state_fw_run)
    print(output_state_bw_run)

