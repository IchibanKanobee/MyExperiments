#https://stackoverflow.com/questions/48126771/nearest-neighbour-search-kdtree 

import numpy as np
from sklearn.neighbors import KDTree
np.random.seed(0)
#X = np.random.random((5, 2))  # 5 points in 2 dimensions
X = np.array([[1,2,3], [3,1,2]])
tree = KDTree(X)
nearest_dist, nearest_ind = tree.query(X, k=2)  # k=2 nearest neighbors where k1 = identity
print(X)
print(nearest_dist[:, 1])    # drop id; assumes sorted -> see args!
print(nearest_ind[:, 1])     # drop id 
