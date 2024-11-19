import numpy as np

x = np.array(["a", "b", "c", "d"])
#generate an array with strings
x_arrstr = np.char.mod('%s', x)
#combine to a string
x_str = ",".join(x_arrstr)
print x_str
