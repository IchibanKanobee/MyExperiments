import tensorflow as tf
from tensorflow.contrib.data import Dataset, Iterator

import os
from glob import glob
from os.path import dirname
from utils import file_op

TRAIN_TFRECORD_DIR = "data/mvcnn/m40/train/"
TEST_TFRECORD_DIR = "data/mvcnn/m40/test/"

MODEL_DIR = "generated_model/mvcnn/m40/"

file_op.ensure_dir_exists(MODEL_DIR)

#TRAIN_DIR = "/media/ara/HDD/data/cnn/m40/train"
#TEST_DIR = "/media/ara/HDD/data/cnn/m40/test"


BATCH_SIZE = 4
SHAPE = [128, 128]


CLASS_COUNT = 40


def data_input_fn(filenames, batch_size=1000, shuffle=False):
    def _parser(record):
        file_features={
            'label': tf.FixedLenFeature([], tf.int64),
            'view_count': tf.FixedLenFeature([], tf.int64)
        }
        count = 80  #need to determine view_count dynamically
        for i in range(count):
            desc_key = "description_" + str(i)
            file_features[desc_key] = tf.FixedLenFeature([], tf.string)
            view_key = "view_" + str(i)
            file_features[view_key] = tf.FixedLenFeature([], tf.string)

        parsed_record = tf.parse_single_example(record, file_features)

        images_list = []
        descriptions_list = []

        for i in range (count):
            desc_key = "description_" + str(i)
            view_key = "view_" + str(i)
            descriptions_list.append(parsed_record[desc_key])
            image_decoded = tf.decode_raw(parsed_record[view_key], tf.float32)
            image_resized = tf.reshape(image_decoded, [128, 128])
            images_list.append(image_resized)

        images = images_list[0]
        descriptions = [descriptions_list[0]]

        for i in range (count - 1):
            images = tf.concat([images, images_list[i+1]], 0)
            descriptions = tf.concat([descriptions, [descriptions_list[i+1]]], 0)


        label = tf.cast(parsed_record['label'], tf.int32)
        view_count = tf.cast(parsed_record['view_count'], tf.int32)

        feature = {}
        feature["view_count"] = view_count
        feature["decriptions"] = descriptions
        feature["images"] = images

        return feature, label

    def _input_fn():
        dataset = tf.data.TFRecordDataset(filenames)


        dataset = dataset.map(_parser)

        dataset = dataset.repeat()
        dataset = dataset.batch(BATCH_SIZE)

#        iterator = dataset.make_initializable_iterator()
        iterator = dataset.make_one_shot_iterator()

        features, labels = iterator.get_next()
        return features, labels

    return _input_fn


def mvcnn_model_fn(features, labels, mode, params):

    if mode == tf.estimator.ModeKeys.PREDICT:
        tf.logging.info("my_model_fn: PREDICT, {}".format(mode))
    elif mode == tf.estimator.ModeKeys.EVAL:
        tf.logging.info("my_model_fn: EVAL, {}".format(mode))
    elif mode == tf.estimator.ModeKeys.TRAIN:
        tf.logging.info("my_model_fn: TRAIN, {}".format(mode))


    #Input layer
    images = features["images"]
    images_resized = tf.reshape(images, [-1, 80, 128, 128, 1], name='input_resized')
    shape = images_resized.get_shape()
    input_layer = tf.reshape(images, [-1, shape[2], shape[3], shape[4]], name='input_layer')
    tf.summary.image('input', input_layer)


    #Convolutional layer
    conv1 = tf.layers.conv2d(inputs = input_layer,
                             filters=96,
                             kernel_size=[7,7],
                             padding="same",
                             strides=(2,2),
                             activation=tf.nn.relu)

    #Pooling Layer #1
    pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=(3,3), strides=2, padding='same')


    #Convolutional Layer#2 and Pooling #2
    conv2 = tf.layers.conv2d(inputs = pool1,
                             filters=256,
                             kernel_size=[5,5],
                             padding="same",
                             strides=(2,2),
                             activation=tf.nn.relu)
    pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=(3,3), strides=2, padding='same')


    #Convolutional Layer#3
    conv3 = tf.layers.conv2d(inputs = pool2,
                             filters=512,
                             kernel_size=[3,3],
                             padding="same",
                             strides=(1,1),
                             activation=tf.nn.relu)


    #Convolutional Layer#4
    conv4 = tf.layers.conv2d(inputs = conv3,
                             filters=512,
                             kernel_size=[3,3],
                             padding="same",
                             strides=(1,1),
                             activation=tf.nn.relu)


    #Convolutional Layer#5 and Pooling #5
    conv5 = tf.layers.conv2d(inputs = conv4,
                             filters=512,
                             kernel_size=[3,3],
                             padding="same",
                             strides=(1,1),
                             activation=tf.nn.relu)
    pool5 = tf.layers.max_pooling2d(inputs=conv5, pool_size=(3,3), strides=2, padding='same')

    pool5_shape = pool5.get_shape()

    inf = tf.reshape(pool5, [-1, 80, pool5_shape[1], pool5_shape[2], pool5_shape[3]])

    reduce_inf = tf.reduce_max(inf, reduction_indices=1)

    #not sure if this is correct!!!
    reduce_inf_flat = tf.contrib.layers.flatten(reduce_inf)

    #Dense Layer
    dense = tf.layers.dense(inputs=reduce_inf_flat,
                            units=4096,
                            activation=tf.nn.relu)
    dropout = tf.layers.dropout(inputs=dense,
                                rate=0.5,
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
#        optimizer = tf.train.MomentumOptimizer(learning_rate=0.001, momentum=0.9)
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
    model_dir= MODEL_DIR + "dataset_model",
    save_checkpoints_steps=20, 
    save_summary_steps=20)

hparams = {
    'learning_rate': 1e-3, 
    'dropout_rate': 0.4,
    'data_directory': "."
}

classifier = tf.estimator.Estimator(
    model_fn=mvcnn_model_fn,
    config=run_config,
    params=hparams
)


train_files = file_op.get_only_files(TRAIN_TFRECORD_DIR)
file_count = len(train_files)
for i in range(file_count):
    train_files[i] = TRAIN_TFRECORD_DIR + train_files[i]

train_input_fn = data_input_fn(train_files, batch_size=BATCH_SIZE)


test_files = file_op.get_only_files(TEST_TFRECORD_DIR)
file_count = len(train_files)
for i in range(file_count):
    test_files[i] = TEST_TFRECORD_DIR + test_files[i]

eval_input_fn = data_input_fn(test_files, batch_size=100)


train_spec = tf.estimator.TrainSpec(input_fn=train_input_fn, max_steps=50000)
eval_spec = tf.estimator.EvalSpec(input_fn=eval_input_fn, steps=10000, start_delay_secs=0)

tf.estimator.train_and_evaluate(classifier, train_spec, eval_spec)

#classifier.train(input_fn=train_input_fn, max_steps=100)
#classifier.evaluate(input_fn=eval_input_fn, steps=100)