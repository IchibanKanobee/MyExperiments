import numpy as np
from distance import utils

#Works
a = np.array([[0, 2], [0, 4]])
a1 = utils.pc_normalize(a)
print a1

#Doesn't work
#a = np.array([[[0, 2], [0, 4]], [[0, 2], [0, 4]]])
#a1 = utils.pc_normalize(a)
#print a1

#Works
a = np.array([[[0, 2], [0, 4]], [[0, 2], [0, 4]]])
count = a.shape[0]
for i in range (count):
    a1 = utils.pc_normalize(a[i])
    print a1
