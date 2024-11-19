import tensorflow as tf

tf.enable_eager_execution()

dataset = tf.data.Dataset.from_tensor_slices([[8, 3, 0, 8, 2, 1], [5, 2, 7, 0, 3, 5]])
dataset

for elem in dataset:
  print(elem.numpy())


it = iter(dataset)

print(next(it).numpy())
print(next(it).numpy())
