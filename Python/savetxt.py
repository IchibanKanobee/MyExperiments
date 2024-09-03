import numpy as np

names  = np.array(['NAME_1', 'NAME_2', 'NAME_3'])
floats = np.array([ 0.1234 ,  0.5678 ,  0.9123 ])

ab = np.zeros(names.size, dtype=[('var1', 'U6'), ('var2', float)])
ab['var1'] = names
ab['var2'] = floats

np.savetxt('test.txt', ab, fmt="%10s %10.3f")
