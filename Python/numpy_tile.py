import numpy as np

a = np.array([1,2,3,4,5])
print a

a1 = a[:,None]
print a1

b = np.tile(a1, (1,2))
print b

