import tensorflow as tf
from tensorflow.contrib.data import Dataset, Iterator

import os
from glob import glob
from os.path import dirname
from utils import file_op
import random

TRAIN_TFRECORD_DIR = "data/mvcnn/m40/train/"
TEST_TFRECORD_DIR = "data/mvcnn/m40/test/"

MODEL_DIR = "generated_model/mvcnn_tiled/m40/"

file_op.ensure_dir_exists(MODEL_DIR)

BATCH_SIZE = 4
SHAPE = [128, 128]

CLASS_COUNT = 40
VIEW_COUNT = 80

LEARNING_RATE_DECAY_FACTOR = 0.1
INITIAL_LEARNING_RATE = 0.001
NUM_EPOCHS_PER_DECAY = 20


def data_input_fn(filenames, batch_size=1000, shuffle=True):
    def _parser(record):
        file_features={
            'label': tf.FixedLenFeature([], tf.int64),
            'view_count': tf.FixedLenFeature([], tf.int64)
        }
        count = VIEW_COUNT
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
        if shuffle:
            #randomly shuffle the list of filenames
            input_filenames = random.sample(filenames, len(filenames))
        else:
            input_filenames = filenames

        dataset = tf.data.TFRecordDataset(input_filenames)
#        dataset = tf.data.TFRecordDataset(filenames)

        dataset = dataset.map(_parser)

        dataset = dataset.repeat()
        dataset = dataset.batch(BATCH_SIZE)

        if shuffle:
            # Shuffle the input unless we are predicting
            dataset = dataset.shuffle(buffer_size=BATCH_SIZE*4)

#        iterator = dataset.make_initializable_iterator()
        iterator = dataset.make_one_shot_iterator()

        features, labels = iterator.get_next()
        return features, labels

    return _input_fn



def concat_width(inf):
    items = tf.unstack(inf)
    conc = items[0]
    ln = len(items)
    for i in range (1, ln):
       conc = tf.concat([conc, items[i]], 1)
    return conc


def mvcnn_tiled_model_fn(features, labels, mode, params):

    if mode == tf.estimator.ModeKeys.PREDICT:
        tf.logging.info("my_model_fn: PREDICT, {}".format(mode))
    elif mode == tf.estimator.ModeKeys.EVAL:
        tf.logging.info("my_model_fn: EVAL, {}".format(mode))
    elif mode == tf.estimator.ModeKeys.TRAIN:
        tf.logging.info("my_model_fn: TRAIN, {}".format(mode))


    #Input layer
    images = features["images"]
    images_resized = tf.reshape(images, [-1, VIEW_COUNT, 128, 128, 1], name='input_resized')
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
    tf.summary.histogram('conv1', conv1)


    #Convolutional Layer#2 and Pooling #2
    conv2 = tf.layers.conv2d(inputs = conv1,
                             filters=96,
                             kernel_size=[3,3],
                             padding="same",
                             strides=(2,2),
                             activation=tf.nn.relu)
    tf.summary.histogram('conv2', conv2)

    conv3 = tf.layers.conv2d(inputs = conv2,
                             filters=256,
                             kernel_size=[5,5],
                             padding="same",
                             strides=(2,2),
                             activation=tf.nn.relu)
    tf.summary.histogram('conv3', conv3)

    conv4 = tf.layers.conv2d(inputs = conv3,
                             filters=256,
                             kernel_size=[3,3],
                             padding="same",
                             strides=(2,2),
                             activation=tf.nn.relu)
    tf.summary.histogram('conv4', conv4)

    conv5 = tf.layers.conv2d(inputs = conv4,
                             filters=512,
                             kernel_size=[3,3],
                             padding="same",
                             strides=(1,1),
                             activation=tf.nn.relu)
#    tf.summary.histogram('conv5', conv5)


    conv6 = tf.layers.conv2d(inputs = conv5,
                             filters=512,
                             kernel_size=[3,3],
                             padding="same",
                             strides=(1,1),
                             activation=tf.nn.relu)
    tf.summary.histogram('conv6', conv6)

    conv6_shape = conv6.get_shape()

    inf = tf.reshape(conv6, [BATCH_SIZE, VIEW_COUNT, conv6_shape[1], conv6_shape[2], conv6_shape[3]])

    items = tf.unstack(inf)
    concats = []

    for item in items:
        conc = concat_width(item)
        concats.append(conc)


    reduce_inf = tf.stack(concats)

    conv7 = tf.layers.conv2d(inputs = reduce_inf,
                             filters=512,
                             kernel_size=[3,3],
                             padding="same",
                             strides=(1,1),
                             activation=tf.nn.relu)
    tf.summary.histogram('conv7', conv7)

    conv8 = tf.layers.conv2d(inputs = conv7,
                             filters=512,
                             kernel_size=[3,3],
                             padding="same",
                             strides=(2,2),
                             activation=tf.nn.relu)
    tf.summary.histogram('conv8', conv8)
#    conv8_flat = tf.contrib.layers.flatten(conv8)

    conv9 = tf.layers.conv2d(inputs = conv8,
                             filters=512,
                             kernel_size=[3,3],
                             padding="same",
                             strides=(2,2),
                             activation=tf.nn.relu)
    tf.summary.histogram('conv9', conv9)
    conv9_flat = tf.contrib.layers.flatten(conv9)

#    conv10 = tf.layers.conv2d(inputs = conv9,
#                             filters=512,
#                             kernel_size=[4,4],
#                             padding="same",
#                             strides=(3,3),
#                             activation=tf.nn.relu)
#    tf.summary.histogram('conv10', conv10)

    #not sure if this is correct!!!
#    conv10_flat = tf.contrib.layers.flatten(conv10)

    #Dense Layer
#    dense = tf.layers.dense(inputs=conv10_flat, units=4096, activation=tf.nn.relu)
    dense = tf.layers.dense(inputs=conv9_flat, units=2048, activation=tf.nn.relu)
#    dense = tf.layers.dense(inputs=conv8_flat, units=2048, activation=tf.nn.relu)
    dropout = tf.layers.dropout(inputs=dense, rate=0.5, training=mode == tf.estimator.ModeKeys.TRAIN)

    #Logits layer
    logits = tf.layers.dense(inputs=dropout, units = CLASS_COUNT)

    tf.summary.text('labels', tf.as_string(labels))
    tf.summary.text('logits', tf.as_string(tf.argmax(input=logits, axis=1)))

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
#        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
        learning_rate = tf.train.exponential_decay (INITIAL_LEARNING_RATE, 20000, LEARNING_RATE_DECAY_FACTOR, True)

#tf.train.get_global_step() * BATCH_SIZE, (7880 * NUM_EPOCHS_PER_DECAY) / BATCH_SIZE, LEARNING_RATE_DECAY_FACTOR, True)
#10000, LEARNING_RATE_DECAY_FACTOR, True)
            
        tf.summary.scalar('leaning rate', learning_rate)

        optimizer = tf.train.MomentumOptimizer(learning_rate=learning_rate, momentum=0.9)
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
    model_fn=mvcnn_tiled_model_fn,
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


train_spec = tf.estimator.TrainSpec(input_fn=train_input_fn, max_steps=100000)
eval_spec = tf.estimator.EvalSpec(input_fn=eval_input_fn, steps=1000, start_delay_secs=0)

tf.estimator.train_and_evaluate(classifier, train_spec, eval_spec)

#classifier.train(input_fn=train_input_fn, max_steps=100)
#classifier.evaluate(input_fn=eval_input_fn, steps=100)
