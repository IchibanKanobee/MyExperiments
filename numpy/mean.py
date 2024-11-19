import numpy as np

a = np.array([[1, 1, 1], [2, 2, 2]])

mean = np.mean(a, axis = 0) #[1.5 1.5 1.5]

print mean

zero_based = a - mean
print zero_based
