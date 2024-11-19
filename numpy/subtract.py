import numpy as np

A3 = np.array([1, 2, 3])
B3 = np.array([4, 5, 6])
C3 = np.array([7, 8, 9])
S3 = np.subtract(B3, A3)
L3 = np.linalg.norm(S3)

print A3, B3, C3
print type(A3)
print (type(A3) is np.ndarray)
print A3.shape
print S3
print L3



A2 = A3[:2]
B2 = B3[:2]
C2 = C3[:2]
S2 = np.subtract(B2, A2)
L2 = np.linalg.norm(S2)


print A2, B2, C3
print type (A2)
print (type(A2) is np.ndarray)
print A2.shape
print S2
print L2



A1 = A3[:1]
B1 = B3[:1]
C1 = C3[:1]
S1 = np.subtract(B1, A1)
L1 = np.linalg.norm(S1)


print A1, B1, C1
print type (A1)
print (type(A1) is np.ndarray)
print A1.shape
print S1
print L1


