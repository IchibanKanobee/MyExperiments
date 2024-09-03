import numpy as np

a = np.array([[1, 1, 1], [2, 2, 2]])

shape = a.shape

b = np.zeros(shape)

radius = 0

for i in range (shape[0]):
    print a[i]
    r = np.linalg.norm(a[i])
    if (r > radius):
        radius = r

print radius

for i in range (shape[0]):
    norm_a = a[i] / radius
    print norm_a
    norm_radius = np.linalg.norm(norm_a)
    print norm_radius
    b[i] = norm_a

print b


