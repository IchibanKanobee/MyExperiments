import tensorflow as tf
from utils import file_op
from os.path import join

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



TRAIN_TFRECORD_DIR = "data/mvcnn/m40_small/train"
TEST_TFRECORD_DIR = "data/mvcnn/m40_small/test"


filenames = tf.placeholder(tf.string, shape=[None])
dataset = tf.data.TFRecordDataset(filenames)


dataset = dataset.map(_parser)

dataset = dataset.repeat()
dataset = dataset.batch(32)

iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()


sess = tf.Session()



fs = file_op.get_only_files(TRAIN_TFRECORD_DIR)

file_count = len(fs)
training_filenames = []

for i in range (file_count):
    training_filenames.append(join(TRAIN_TFRECORD_DIR, fs[i]))

sess.run(iterator.initializer, feed_dict={filenames: training_filenames})

for i in range (20):
    value = sess.run(next_element)
    print value




fs = file_op.get_only_files(TEST_TFRECORD_DIR)

file_count = len(fs)
test_filenames = []

for i in range(file_count):
    test_filenames.append(join(TEST_TFRECORD_DIR, fs[i]))

sess.run(iterator.initializer, feed_dict={filenames: test_filenames})

for i in range (20):
    value = sess.run(next_element)
    print value

