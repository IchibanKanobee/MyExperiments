import numpy as np
import tensorflow as tf

training_dataset = tf.data.Dataset.range(100).map(lambda x: x + tf.random_uniform([], -10, 10, tf.int64))

validation_dataset = tf.data.Dataset.range(50)

iterator = tf.data.Iterator.from_structure(training_dataset.output_types, training_dataset.output_shapes)

next_element = iterator.get_next()

training_init_op = iterator.make_initializer(training_dataset)
validation_init_op = iterator.make_initializer(validation_dataset)

sess = tf.Session()
for _ in range (20):
    sess.run(training_init_op)
    for _ in range (100):
        value = sess.run(next_element)
        print value

sess.run(validation_init_op)
for _ in range (50):
    value = sess.run(next_element)
    print value


