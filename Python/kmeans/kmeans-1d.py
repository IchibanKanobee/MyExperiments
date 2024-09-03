from sklearn.cluster import KMeans
import numpy as np

a = np.array([0,1,2,3,4,5,6,7,8,9])

a_kmeans = a.reshape(-1,1)
print (a_kmeans)
