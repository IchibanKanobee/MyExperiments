import numpy as np


def get_circle_point_cloud(point_count, radius, shift):

    vertex = np.zeros((point_count,),
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

    for i in range (point_count):
        x = np.random.uniform(-radius, radius)
        y = shift
        z_ = np.sqrt(radius * radius - x * x)
        z = np.random.uniform(-z_, z_)
        vertex[i] = (x + radius, y, z + radius) #add radius to (x, z) to make sure they are positive for relu layer

    return vertex


