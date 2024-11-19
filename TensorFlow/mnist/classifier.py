import tensorflow as tf
import input_data


CLASSES = 10
BATCH_SIZE = 20

data_sets = input_data.read_data_sets("data", False)

images = tf.placeholder(tf.float32, shape=(784,), name="images")
labels = tf.placeholder(tf.int32, shape=(10,), name="labels")



