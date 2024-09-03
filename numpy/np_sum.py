import numpy as np

a = np.array([[1,1,1], [2,2,2]])

s1 = np.sum(a)
print s1

s2 = np.sum(a, axis = 0)
print s2

s3 = np.sum(a, axis = 1)
print s3

