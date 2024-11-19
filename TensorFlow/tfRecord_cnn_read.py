import tensorflow as tf
import scipy.misc


DATA_DIR = "data/cnn/"
OUTPUT_DIR = "output/images/cnn/"

BATCH_SIZE = 32

def _parser(record):
    features={
        'label': tf.FixedLenFeature([], tf.int64),
        'image': tf.FixedLenFeature([], tf.string)
    }
    parsed_record = tf.parse_single_example(record, features)
    image_decoded = tf.decode_raw(parsed_record['image'], tf.float32)
    image = tf.reshape(image_decoded, [128, 128])

    label = tf.cast(parsed_record['label'], tf.int32)

    return image, label

filenames = tf.placeholder(tf.string, shape=[None])
dataset = tf.data.TFRecordDataset(filenames)

dataset = dataset.map(_parser)
dataset = dataset.repeat()
dataset = dataset.batch(BATCH_SIZE)

iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()


sess = tf.Session()

#Run tfRecord_write.py to get tfrecord files

training_filenames = [DATA_DIR + "train_tfrecords"]
sess.run(iterator.initializer, feed_dict={filenames: training_filenames})

for i in range (100):
    value = sess.run(next_element)
    images = value[0]
    for j in range (BATCH_SIZE):
        name = "Image_" + str(i) + "_" + str(j) + ".png"
        image_path = OUTPUT_DIR + name
        scipy.misc.imsave(image_path, images[j])
    labels = value[1]
    print images


#validation_filenames = ["test.tfrecords"]
#sess.run(iterator.initializer, feed_dict={filenames: validation_filenames})
