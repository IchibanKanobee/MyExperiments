#Based on https://kratzert.github.io/2017/06/15/example-of-tensorflows-new-input-pipeline.html

import tensorflow as tf
from tensorflow.contrib.data import Dataset, Iterator

import os
from glob import glob
from os.path import dirname

TRAIN_DIR = "/raid/data/cnn/m40/train"
TEST_DIR = "/raid/data/cnn/m40/test"

DATA_DIR = "data/cnn/"
MODEL_DIR = "generated_model/cnn/"

#TRAIN_DIR = "/media/ara/HDD/data/cnn/m40/train"
#TEST_DIR = "/media/ara/HDD/data/cnn/m40/test"


BATCH_SIZE = 20
SHAPE = [128, 128]

def get_labels_from_files(files):
    labels = []
    for f in files:
        directory = dirname(f)
        dirs = directory.split('/')
        dirs_len = len(dirs)
        labels.append(dirs[dirs_len - 1])
    return labels


def convert_labels_to_numbers(labels, classes):
    label_numbers = []
    label_count = len(labels)
    class_count = len(classes)
    for i in range (label_count):
        for j in range (class_count):
            if labels[i] == classes[j]:
                label_numbers.append(j)
    return label_numbers


def input_parser(img_path, label):
    one_hot = tf.one_hot(label, CLASS_COUNT)

    img_file = tf.read_file(img_path)
    img_decoded = tf.image.decode_image(img_file, channels=1)
    return img_decoded, one_hot


train_files = [y for x in os.walk(TRAIN_DIR) for y in glob(os.path.join(x[0], '*.png'))]
train_labels = get_labels_from_files(train_files)

classes = list(set(train_labels))
CLASS_COUNT = len(classes)


def data_input_fn(filenames, batch_size=1000, shuffle=False):
    
    def _parser(record):
        features={
            'label': tf.FixedLenFeature([], tf.int64),
            'image': tf.FixedLenFeature([], tf.string)
        }
        parsed_record = tf.parse_single_example(record, features)
        image = tf.decode_raw(parsed_record['image'], tf.float32)

        label = tf.cast(parsed_record['label'], tf.int32)

        return image, label
        
    def _input_fn():
        dataset = tf.data.TFRecordDataset(filenames)
        dataset = dataset.map(_parser)
        if shuffle:
            dataset = dataset.shuffle(buffer_size=10000)

        dataset = dataset.repeat(None) # Infinite iterations: let experiment determine num_epochs
        dataset = dataset.batch(batch_size)
        
        iterator = dataset.make_one_shot_iterator()
        features, labels = iterator.get_next()
        
        return features, labels
    return _input_fn


def cnn_model_fn(features, labels, mode, params):
    if mode == tf.estimator.ModeKeys.PREDICT:
        tf.logging.info("my_model_fn: PREDICT, {}".format(mode))
    elif mode == tf.estimator.ModeKeys.EVAL:
        tf.logging.info("my_model_fn: EVAL, {}".format(mode))
    elif mode == tf.estimator.ModeKeys.TRAIN:
        tf.logging.info("my_model_fn: TRAIN, {}".format(mode))


    #Input layer
    input_layer = tf.reshape(features, [-1, 128, 128, 1], name='input_reshape')
    tf.summary.image('input', input_layer)


    #Convolutional layer
    conv1 = tf.layers.conv2d(inputs = input_layer,
                             filters=32,
                             kernel_size=[5,5],
                             padding="same",
                             strides=(2,2),
                             activation=tf.nn.relu)

    #Pooling Layer #1
    pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=(2, 2), strides=2, padding='same')


    #Convolutional Layer#2 and Poling #2
    conv2 = tf.layers.conv2d(inputs = pool1,
                             filters=64,
                             kernel_size=[5,5],
                             padding="same",
                             strides=(2,2),
                             activation=tf.nn.relu)
    pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=(2,2), strides=2, padding='same')

    #Dense Layer
    pool2_flat = tf.reshape(pool2, [-1, 8 * 8 * 64])
    dense = tf.layers.dense(inputs=pool2_flat,
                            units=1024,
                            activation=tf.nn.relu)
    dropout = tf.layers.dropout(inputs=dense,
                                rate=0.4,
                                training=mode == tf.estimator.ModeKeys.TRAIN)

    #Logits layer
    logits = tf.layers.dense(inputs=dropout, units = CLASS_COUNT)

    predictions = {
      # Generate predictions (for PREDICT and EVAL mode)
      "classes": tf.argmax(input=logits, axis=1),
      # Add `softmax_tensor` to the graph. It is used for PREDICT and by the
      # `logging_hook`.
      "probabilities": tf.nn.softmax(logits, name="softmax_tensor")
     }

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

    # Calculate Loss (for both TRAIN and EVAL modes)
    loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

    # Configure the Training Op (for TRAIN mode)
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
        train_op = optimizer.minimize(
            loss=loss,
            global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)

    # Add evaluation metrics (for EVAL mode)
    eval_metric_ops = {
          "accuracy": tf.metrics.accuracy(
              labels=labels, predictions=predictions["classes"])}
    return tf.estimator.EstimatorSpec(
          mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


run_config = tf.estimator.RunConfig(
#    model_dir=args.model_directory, 
    model_dir= MODEL_DIR + "dataset_model",
    save_checkpoints_steps=20, 
    save_summary_steps=20)

hparams = {
    'learning_rate': 1e-3, 
    'dropout_rate': 0.4,
#    'data_directory': os.path.expanduser(args.data_directory)
    'data_directory': "."
}

classifier = tf.estimator.Estimator(
    model_fn=cnn_model_fn, 
    config=run_config,
    params=hparams
)


train_batch_size = 1000
    
#train_input_fn = data_input_fn(glob.glob(os.path.join(hparams['data_directory'], 'train-*.tfrecords')), batch_size=train_batch_size)
#eval_input_fn = data_input_fn(os.path.join(hparams['data_directory'], 'validation.tfrecords'), batch_size=100)

train_input_fn = data_input_fn([DATA_DIR + 'train_tfrecords'], batch_size=train_batch_size)
eval_input_fn = data_input_fn([DATA_DIR + 'test_tfrecords'], batch_size=100)


train_spec = tf.estimator.TrainSpec(input_fn=train_input_fn, max_steps=100)
eval_spec = tf.estimator.EvalSpec(input_fn=eval_input_fn, steps=100, start_delay_secs=0)

tf.estimator.train_and_evaluate(classifier, train_spec, eval_spec)

