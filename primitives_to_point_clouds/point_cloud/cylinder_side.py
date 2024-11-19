import numpy as np

def get_cylinder_side_point_cloud(point_count, height, radius):
    vertex = np.zeros((point_count,),
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

    for i in range (point_count):
        theta = np.random.uniform(-np.pi, np.pi)
        x = radius * np.cos(theta)
        z = radius * np.sin(theta)
        y = np.random.uniform(0, height)

        vertex[i] = (x + radius, y, z + radius)  #add radius to (x, z) to make sure they are positive for relu layer

    return vertex

