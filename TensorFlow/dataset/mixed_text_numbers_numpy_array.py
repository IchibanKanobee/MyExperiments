import tensorflow as tf
import numpy as np


np_a = np.array([["a","b"], ["c","d"]])
np_b = np.array([[1,2], [3,4]])

dataset = tf.data.Dataset.from_tensor_slices((np_a, np_b))
print(dataset)


it = iter(dataset)
n = next(it)
print(n[0].numpy(), n[1].numpy())
n = next(it)
print(n[0].numpy(), n[1].numpy())
