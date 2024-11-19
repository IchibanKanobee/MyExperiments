import tensorflow as tf
import numpy as np


np_a = np.array([[1,2], [3,4]])

dataset = tf.data.Dataset.from_tensor_slices(np_a)
print(dataset)

it = iter(dataset)
print(next(it).numpy())
print(next(it).numpy())
