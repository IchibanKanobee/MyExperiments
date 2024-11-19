import tensorflow as tf
import numpy as np


np_a = np.array([["a","b"], ["c","d"]])

dataset = tf.data.Dataset.from_tensor_slices(np_a)
print(dataset)


it = iter(dataset)
print(next(it).numpy())
print(next(it).numpy())
