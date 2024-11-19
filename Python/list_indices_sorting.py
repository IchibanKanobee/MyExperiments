import numpy as np
from numpy import array

cut_count = 3

a = [3, 1, 5, 8, 10]
asc_indices = np.argsort(a)

print (asc_indices)

vals = array(a)[asc_indices]

print (list(vals[:cut_count]))




