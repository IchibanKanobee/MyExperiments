import numpy as np
import tensorflow as tf
from os import listdir
from os.path import isfile, join
from plyfile import plyfile


DATA_DIR = '/raid/MyProjects/python-point-cloud/data/spheres'
#DATA_DIR = '/media/ara/HDD/MyProjects/python-point-cloud/data/spheres'
BATCH_SIZE = 16
PARAMS_VECTOR_SIZE = 256 #sparse vector for holding param values for different primitives
POINT_COUNT = 2048
DIMS = 3
EPOCHS = 500

labels = {"box":0,
          "cylinder":1,
          "sphere":2,
          "plane":3
         }

##########################
def get_primitive_params_pos_start_from_label(label):
    label_count = len(labels)
    pos = PARAMS_VECTOR_SIZE / label_count * label
    return pos


##########################
def get_primitive_file_label_params(name):
    """Returns label and parameters, derived from a file name, in a sparse vector
    First, is the label of the class (for example, box is 0)
    Next, are parameters like width, length, height, or other parameters relevant to the class
    The position of the parameters in the vector is determined by the class, and is positioned to ensure sparsity of the vector
    """
    params = name.split('_')
    count = len(params)
    p = np.zeros(PARAMS_VECTOR_SIZE)
    label = int (labels[params[0]])
    pos = get_primitive_params_pos_start_from_label(label)
    p[pos] = label
    for i in range (pos + 1, pos + count - 1): #count -1 because last param is the ".ply" extension
        p[i] = int (params[i-pos])

    return p

##########################
def get_point_cloud_from_file(dir, name):
    filename = join(dir, name)
    plydata = plyfile.PlyData.read(filename)
    data = plydata.elements[0].data
    arr = np.fromiter(data, dtype=[('x', '<f4'), ('y', '<f4'), ('z', '<f4')])
    return arr


##########################
def write_point_cloud_to_file(dir, name, cloud):
    filename = join(dir, name)
    point_count = cloud.shape[0]

    vertex = np.zeros((point_count,),
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

    for i in range (point_count):
        x = cloud[i][0]
        y = cloud[i][1]
        z = cloud[i][2]
        vertex[i] = (x, y, z)

    el = plyfile.PlyElement.describe(vertex, 'vertex')
    plyfile.PlyData([el]).write(filename)



##########################
def get_point_clouds_labels_params(files):
    """Returns label and parameters for each file in a numpy array
    """
    count = files.size
    params = np.zeros(shape = (count, PARAMS_VECTOR_SIZE))
    for i in range(count):
        file_name = files[i]
        param = get_primitive_file_label_params(file_name)
        params[i] = param
    
    return params


##########################
def get_point_clouds_data(dir, files):
    """Returns point cloud data in shape(BATCH_SIZE, POINT_COUNT, DIMS)
    """
    batch_size = files.size
    data = np.zeros(shape=(batch_size, POINT_COUNT, DIMS))
    point_data = np.zeros(shape=(POINT_COUNT, DIMS))
    point = np.zeros(shape=(DIMS))
    for i in range(batch_size):
        file_name = files[i]
        file_data = get_point_cloud_from_file(dir, file_name)
        for j in range(POINT_COUNT):
            for k in range(DIMS):
                t = file_data[j]
                point[k] = t[k]
            point_data[j] = point
        data[i] = point_data
    return data


##########################
def batch_distance_matrix_general(A, B):
    r_A = tf.reduce_sum(A * A, axis=2, keep_dims=True)
    r_B = tf.reduce_sum(B * B, axis=2, keep_dims=True)
    m = tf.matmul(A, tf.transpose(B, perm=(0, 2, 1)))
    D = r_A - 2 * m + tf.transpose(r_B, perm=(0, 2, 1))
    return D


##########################
def knn_indices_general(queries, points, k, sorted=True):
    queries_shape = tf.shape(queries)
    batch_size = queries_shape[0]
    point_num = queries_shape[1]
    D = batch_distance_matrix_general(queries, points)
    distances, point_indices = tf.nn.top_k(-D, k=k, sorted=sorted)
    batch_indices = tf.tile(tf.reshape(tf.range(batch_size), (-1, 1, 1, 1)), (1, point_num, k, 1))
    indices = tf.concat([batch_indices, tf.expand_dims(point_indices, axis=3)], axis=3)
    return -distances, indices


##########################
# A shape is (batch_size, point_count, dims), B shape is (batch_size, point_count, dims)
def chamfer_distance_loss(A, B):
    distances, _ = knn_indices_general(A, B, 1, False)
    return tf.reduce_mean(distances)


############################
############################
#List all files, and shuffle them randomly into an np.array
files = [f for f in listdir(DATA_DIR) if isfile(join(DATA_DIR, f))]
data_files = np.array(files)
np.random.shuffle(data_files)
count = data_files.size

#tf_pc_params = tf.placeholder(tf.int32, shape = [None, PARAMS_VECTOR_SIZE])
tf_pc_params = tf.placeholder(tf.float32, shape = [None, PARAMS_VECTOR_SIZE])
tf_pc_data = tf.placeholder(tf.float32, shape = [None, POINT_COUNT, DIMS])



#Dummy data for now
#tf_params = tf_pc_params
#tf_data = tf_pc_data

#Network
w = tf.get_variable('w', shape = [DIMS, PARAMS_VECTOR_SIZE, POINT_COUNT])
b = tf.get_variable('b', shape = [DIMS, POINT_COUNT])

outs = []

for i in range(DIMS):
    t1 = tf.matmul(tf_pc_params, w[i]) + b[i]
    t2 = tf.nn.relu(t1)
    outs.append(t2)

z0 = tf.stack(outs)

z = tf.transpose(z0, perm=[1, 2, 0])
loss_op = chamfer_distance_loss(z, tf_pc_data)
loss_summary = tf.summary.scalar("loss", loss_op)

adam = tf.train.AdamOptimizer(1e-2)
train_op = adam.minimize(loss_op, name = "train_op")

sum_writer = tf.summary.FileWriter("summary/spheres")

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    loss = 10

    for i in range (EPOCHS):

        print('-------------------------')
        print('Current iteration:%d' % (i))

        for j in xrange(0, count, BATCH_SIZE):
            print('Processing batch:%d' % (j / BATCH_SIZE))
            params = get_point_clouds_labels_params(data_files[j:j+BATCH_SIZE])
            data = get_point_clouds_data(DATA_DIR, data_files[j:j+BATCH_SIZE])
            _, loss, loss_sum = sess.run([train_op, loss_op, loss_summary], feed_dict = {tf_pc_params:params, tf_pc_data:data})

        print('-------------------------')
        print('iter:%d - loss:%f' % (i, loss))
        sum_writer.add_summary(loss_sum, i)

        if (i % 5 == 0):
            out_clouds = sess.run(z, feed_dict = {tf_pc_params:params, tf_pc_data:data})
            name = "Iteration_" + str(i) + ".ply"
            print('Writing out point cloud file ' + name)
            write_point_cloud_to_file("output/spheres", name, out_clouds[0])



