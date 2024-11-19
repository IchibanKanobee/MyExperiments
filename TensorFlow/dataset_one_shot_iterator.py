import numpy as np
from utils import array_2D
import tensorflow as tf

record_count = 500
element_count = 5
random_range = 10

records = array_2D.get_2D_random_sum_array(record_count, element_count, random_range)

dataset = tf.data.Dataset.from_tensor_slices(records)
iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()


with tf.Session() as sess:
    for i in range (record_count):
        print sess.run(next_element)


