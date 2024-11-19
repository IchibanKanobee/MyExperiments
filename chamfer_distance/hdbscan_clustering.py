import numpy as np
#from sklearn.metrics.pairwise import pairwise_distances
import hdbscan



dist = np.loadtxt('distance_matrix_3.txt')
print (dist)

#distance_matrix = pairwise_distances(dist)
clusterer = hdbscan.HDBSCAN(min_cluster_size=2, metric='precomputed')
clusterer.fit(dist)
print (clusterer.labels_)
