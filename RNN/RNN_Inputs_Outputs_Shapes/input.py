import numpy as np

# Batch size = 2, sequence length = 3, number features = 1, shape=(2, 3, 1)
values231 = np.array([
    [[1], [2], [3]],
    [[2], [3], [4]]
])

print values231.shape

# Batch size = 3, sequence length = 5, number features = 2, shape=(3, 5, 2)
values352 = np.array([
    [[1, 4], [2, 5], [3, 6], [4, 7], [5, 8]],
    [[2, 5], [3, 6], [4, 7], [5, 8], [6, 9]],
    [[3, 6], [4, 7], [5, 8], [6, 9], [7, 10]]
])

print values352.shape

