import tensorflow as tf
import os
import glob


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
    """Model function for CNN."""

    is_training = mode == tf.estimator.ModeKeys.TRAIN
    
    with tf.name_scope('Input'):
        # Input Layer
        input_layer = tf.reshape(features, [-1, 128, 128, 1], name='input_reshape')
        tf.summary.image('input', input_layer)

    with tf.name_scope('Conv_1'):
        # Convolutional Layer #1
        conv1 = tf.layers.conv2d(
          inputs=input_layer,
          filters=32,
          kernel_size=(5, 5),
          padding='same',
          activation=tf.nn.relu,
          trainable=is_training)

        # Pooling Layer #1
        pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=(2, 2), strides=2, padding='same')

    with tf.name_scope('Conv_2'):
        # Convolutional Layer #2 and Pooling Layer #2
        conv2 = tf.layers.conv2d(
            inputs=pool1,
            filters=64,
            kernel_size=(5, 5),
            padding='same',
            activation=tf.nn.relu,
            trainable=is_training)
        
        pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=(2, 2), strides=2, padding='same')

    with tf.name_scope('Dense_Dropout'):
        # Dense Layer
        # pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])
        pool2_flat = tf.contrib.layers.flatten(pool2)
        dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu, trainable=is_training)
        dropout = tf.layers.dropout(inputs=dense, rate=params['dropout_rate'], training=is_training)

    with tf.name_scope('Predictions'):
        # Logits Layer
        logits = tf.layers.dense(inputs=dropout, units=55, trainable=is_training)

    predicted_logit = tf.argmax(input=logits, axis=1, output_type=tf.int32)
    scores = tf.nn.softmax(logits, name='softmax_tensor')

    # Generate Predictions
    predictions = {
      'classes': predicted_logit,
      'probabilities': scores
    }

    # PREDICT
    if mode == tf.estimator.ModeKeys.PREDICT:
        export_outputs = {
            'prediction': tf.estimator.export.ClassificationOutput(
                scores=scores,
                classes=tf.cast(predicted_logit, tf.string))
        }

        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions, export_outputs=export_outputs)

    # TRAIN and EVAL
    loss = tf.losses.softmax_cross_entropy(onehot_labels=labels, logits=logits)

    accuracy = tf.metrics.accuracy(tf.argmax(labels, axis=1), predicted_logit)
    eval_metric = { 'accuracy': accuracy }

    # Configure the Training Op (for TRAIN mode)
    if mode == tf.estimator.ModeKeys.TRAIN:
        tf.summary.scalar('accuracy', accuracy[0])
        train_op = tf.contrib.layers.optimize_loss(
            loss=loss,
            global_step=tf.train.get_global_step(),
            learning_rate=params['learning_rate'],
            optimizer='Adam')
    else:
        train_op = None

    return tf.estimator.EstimatorSpec(
        mode=mode,
        loss=loss,
        train_op=train_op,
        eval_metric_ops=eval_metric,
        predictions=predictions)


run_config = tf.estimator.RunConfig(
#    model_dir=args.model_directory, 
    model_dir="cnn_dataset_model", 
    save_checkpoints_steps=20, 
    save_summary_steps=20)

hparams = {
    'learning_rate': 1e-3, 
    'dropout_rate': 0.4,
#    'data_directory': os.path.expanduser(args.data_directory)
    'data_directory': "."
}

mnist_classifier = tf.estimator.Estimator(
    model_fn=cnn_model_fn, 
    config=run_config,
    params=hparams
)


train_batch_size = 1000
    
#train_input_fn = data_input_fn(glob.glob(os.path.join(hparams['data_directory'], 'train-*.tfrecords')), batch_size=train_batch_size)
#eval_input_fn = data_input_fn(os.path.join(hparams['data_directory'], 'validation.tfrecords'), batch_size=100)

train_input_fn = data_input_fn(['train-tfrecords'], batch_size=train_batch_size)
eval_input_fn = data_input_fn(['test.tfrecords'], batch_size=100)

#train_input_fn = data_input_fn('train-tfrecords', batch_size=train_batch_size)
#eval_input_fn = data_input_fn('test.tfrecords', batch_size=100)

train_spec = tf.estimator.TrainSpec(input_fn=train_input_fn, max_steps=40)
eval_spec = tf.estimator.EvalSpec(input_fn=eval_input_fn, steps=100, start_delay_secs=0)

tf.estimator.train_and_evaluate(mnist_classifier, train_spec, eval_spec)


