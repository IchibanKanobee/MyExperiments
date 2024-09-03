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
    N = pc1.shape[0]
    M = pc2.shape[0]

    pc1_expand_dims = np.expand_dims(pc1,1)
    pc2_expand_dims = np.expand_dims(pc2,0)
    pc1_expand_tile = np.tile(pc1_expand_dims, [1,M,1])
    pc2_expand_tile = np.tile(pc2_expand_dims, [N,1,1])
    pc_diff = pc1_expand_tile - pc2_expand_tile # B,N,M,C
    pc_dist = np.sum(pc_diff ** 2, axis=-1) # B,N,M
    dist1 = np.min(pc_dist, axis=1) # B,N
    idx1 = np.argmin(pc_dist, axis=1) # B,N
    dist2 = np.min(pc_dist, axis=0) # B,M
    idx2 = np.argmin(pc_dist, axis=0) # B,M

    return pc_dist, dist1, idx1, dist2, idx2, pc1_expand_dims, pc2_expand_dims, pc1_expand_tile, pc2_expand_tile

'''

    pc1_expand_dims = np.expand_dims(pc1,2)
    pc2_expand_dims = np.expand_dims(pc2,1)
    pc1_expand_tile = np.tile(pc1_expand_dims, [1,1,M,1])
    pc2_expand_tile = np.tile(pc2_expand_dims, [1,N,1,1])
    pc_diff = pc1_expand_tile - pc2_expand_tile # B,N,M,C
    pc_dist = np.sum(pc_diff ** 2, axis=-1) # B,N,M
    dist1 = np.min(pc_dist, axis=2) # B,N
    idx1 = np.argmin(pc_dist, axis=2) # B,N
    dist2 = np.min(pc_dist, axis=1) # B,M
    idx2 = np.argmin(pc_dist, axis=1) # B,M
    return pc_dist, dist1, idx1, dist2, idx2, pc1_expand_dims, pc2_expand_dims, pc1_expand_tile, pc2_expand_tile
#    return dist1, idx1, dist2, idx2
'''


def verify_nn_distance_cup():
#    np.random.seed(0)

#    pc1arr = np.empty((1,N,3))
#    pc2arr = np.empty((1,M,3))

#    pc1arr.fill(1)
#    pc2arr.fill(2)
#    pc2arr[:,0,:] = pc1arr

#Original
#    pc1arr = np.random.random((1,N,3))
#    pc2arr = np.random.random((1,M,3))

#    pc1arr = np.array([[[1, 2, 3], [4,5,6]]])
#    pc2arr = np.array([[[4,5,6], [1, 2, 3]]])


    pc1arr = np.array([[1], [2]])
    pc2arr = np.array([[3], [4]])

    print ("Point cloud 1")
    print(pc1arr)
    print ("Point cloud 2")
    print(pc2arr)
    pc_dist, dist1, idx1, dist2, idx2, exp1_dims, exp2_dims, exp1_tiles, exp2_tiles = nn_distance_cpu(pc1arr, pc2arr)
#    dist1, idx1, dist2, idx2 = nn_distance_cpu(pc1, pc2)

#start of new
    print ("pc_dist")
    print(pc_dist)
    print ("exp1_dims")
    print(exp1_dims)
    print ("exp1_dims dimensions")
    print((exp1_dims.shape))
    print ("exp1_tiles")
    print((exp1_tiles))
    print ("exp1_tiles dimensions")
    print((exp1_tiles.shape))

    print ("exp2_dims")
    print((exp2_dims))
    print ("exp2_dims dimensions")
    print((exp2_dims.shape))
    print ("exp2_tiles")
    print(exp2_tiles)
    print ("exp2_tiles dimensions")
    print((exp2_tiles.shape))

#end of new

    print ("dist1")
    print((dist1))
    print ("idx1")
    print((idx1))
    print ("dist2")
    print(dist2)
    print ("idx2")
    print((idx2))


    N = pc1arr.shape[0]
    M = pc2arr.shape[0]

    dist = np.zeros((N,M))
    for i in range(N):
        for j in range(M):
            dist[i,j] = np.sum((pc1arr[i,:] - pc2arr[j,:]) ** 2)
    print ("dist")
    print(dist)

if __name__ == '__main__':
    verify_nn_distance_cup()
