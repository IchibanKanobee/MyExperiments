import tensorflow as tf
import numpy as np

def nn_distance_cpu(pc1, pc2):
    '''
    Input:
        pc1: float TF tensor in shape (B,N,C) the first point cloud
        pc2: float TF tensor in shape (B,M,C) the second point cloud
    Output:
        dist1: float TF tensor in shape (B,N) distance from first to second
        idx1: int32 TF tensor in shape (B,N) nearest neighbor from first to second
        dist2: float TF tensor in shape (B,M) distance from second to first
        idx2: int32 TF tensor in shape (B,M) nearest neighbor from second to first
    '''
    N = pc1.get_shape()[1].value
    M = pc2.get_shape()[1].value
    pc1_expand_dims = tf.expand_dims(pc1,2)
    pc2_expand_dims = tf.expand_dims(pc2,1)
    pc1_expand_tile = tf.tile(pc1_expand_dims, [1,1,M,1])
    pc2_expand_tile = tf.tile(pc2_expand_dims, [1,N,1,1])
    pc_diff = pc1_expand_tile - pc2_expand_tile # B,N,M,C
    pc_dist = tf.reduce_sum(pc_diff ** 2, axis=-1) # B,N,M
    dist1 = tf.reduce_min(pc_dist, axis=2) # B,N
    idx1 = tf.argmin(pc_dist, axis=2) # B,N
    dist2 = tf.reduce_min(pc_dist, axis=1) # B,M
    idx2 = tf.argmin(pc_dist, axis=1) # B,M
    return pc_dist, dist1, idx1, dist2, idx2, pc1_expand_dims, pc2_expand_dims, pc1_expand_tile, pc2_expand_tile
#    return dist1, idx1, dist2, idx2


def verify_nn_distance_cup():
    np.random.seed(0)
    sess = tf.Session()

#    N = 5
#    M = 6

    N = 2
    M = 2

    pc1arr = np.empty((1,N,3))
    pc2arr = np.empty((1,M,3))

#    pc1arr.fill(1)
#    pc2arr.fill(2)
#    pc2arr[:,0,:] = pc1arr

    pc1arr = np.array([[[1, 2, 3], [4,5,6]]])
    pc2arr = np.array([[[4,5,6], [1, 2, 3]]])

#Original
#    pc1arr = np.random.random((1,N,3))
#    pc2arr = np.random.random((1,M,3))

    print ("Point cloud 1")
    print(pc1arr)
    print ("Point cloud 2")
    print(pc2arr)
    pc1 = tf.constant(pc1arr)
    pc2 = tf.constant(pc2arr)
    pc_dist, dist1, idx1, dist2, idx2, exp1_dims, exp2_dims, exp1_tiles, exp2_tiles = nn_distance_cpu(pc1, pc2)
#    dist1, idx1, dist2, idx2 = nn_distance_cpu(pc1, pc2)

#start of new
    print ("pc_dist")
    print(sess.run(pc_dist))
    print ("exp1_dims")
    print(sess.run(exp1_dims))
    print ("exp1_dims dimensions")
    print(sess.run(tf.shape(exp1_dims)))
    print ("exp1_tiles")
    print(sess.run(exp1_tiles))
    print ("exp1_tiles dimensions")
    print(sess.run(tf.shape(exp1_tiles)))

    print ("exp2_dims")
    print(sess.run(exp2_dims))
    print ("exp2_dims dimensions")
    print(sess.run(tf.shape(exp2_dims)))
    print ("exp2_tiles")
    print(sess.run(exp2_tiles))
    print ("exp2_tiles dimensions")
    print(sess.run(tf.shape(exp2_tiles)))

#end of new

    print ("dist1")
    print(sess.run(dist1))
    print ("idx1")
    print(sess.run(idx1))
    print ("dist2")
    print(sess.run(dist2))
    print ("idx2")
    print(sess.run(idx2))


    
    dist = np.zeros((N,M))
    for i in range(N):
        for j in range(M):
            dist[i,j] = np.sum((pc1arr[0,i,:] - pc2arr[0,j,:]) ** 2)
    print ("dist")
    print(dist)

if __name__ == '__main__':
    verify_nn_distance_cup()
