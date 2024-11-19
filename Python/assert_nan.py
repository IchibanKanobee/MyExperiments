import math
import numpy as np

a = np.array([[1,2], [3,4]])
b = np.array([[1,float('nan')], [3,4]])

print np.isin(a, 1)
print np.isin(b, float('nan'))
print np.isin(b, math.nan)

