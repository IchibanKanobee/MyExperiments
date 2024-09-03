import numpy as np

split_count = 3

a = np.array([1,2,3,4,5,6,7])

length = a.shape[0]
print length

new_length = int(length / split_count) * split_count
print new_length

new_array = a[:new_length]
print new_array

b = np.split(new_array, split_count)

print b
