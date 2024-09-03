import random
import tensorflow as tf

def func(x1, x2, x3, x4):
    return (2*x1 + 3*x2 + 4 *x3 +5 * x4)


def get_parameters(low, high):
    a = [random.randint(low, high), random.randint(low, high), random.randint(low, high), random.randint(low, high)]
    return a


def create_record(low, high):
    a = get_parameters(low, high)
    b = func(a[0], a[1], a[2], a[3])
    el = (a[0] , a[1], a[2], a[3], b)
    s = ','.join(str(s) for s in el)
    return s

def create_array(count, low, high):
    arr = []
    for i in range(count):
        a = create_record(low, high)
        arr.append(a)
    print arr
    return arr


def create_file(name, count):
    low = 1
    high = 10
    arr = create_array(count, low, high)
    count = len(arr)
    with open(name, 'wb')  as myfile:
        for item in arr:
            myfile.write("%s\n" % item)

#Create 2 csv files. All functions above are helper functions to create the files.
create_file("file0.csv", 5)
create_file("file1.csv", 5)

#Output strings (e.g. filenames) to a queue for an input pipeline.
filename_queue = tf.train.string_input_producer(["file0.csv", "file1.csv"])
#A Reader that outputs the lines of a file delimited by newlines.
reader = tf.TextLineReader()
#Returns the next record (key, value pair) produced by a reader.
key, value = reader.read(filename_queue)

record_defaults = [[1], [1], [1], [1], [1]]
#Convert CSV records to tensors. Each column maps to one tensor.
col1, col2, col3, col4, col5 = tf.decode_csv(value, record_defaults=record_defaults)
#Stacks a list of rank-R tensors into one rank-(R+1) (concatenate along axis)
features = tf.stack([col1, col2, col3, col4])


with tf.Session() as sess:
#A coordinator for threads.This class implements a simple mechanism to coordinate the termination of a set of threads.
    coord = tf.train.Coordinator()
#Starts all queue runners collected in the graph. This is a companion method to add_queue_runner(). It just starts threads for all queue runners collected in the graph. It returns the list of all threads.
    threads = tf.train.start_queue_runners(coord=coord)

    for i in range(10):
        example, label = sess.run([features, col5])
        print "example:"
        print example
        print "label:"
        print label

coord.request_stop()
coord.join.threads()
