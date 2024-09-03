import numpy as np

def get_sphere_point_cloud(point_count, radius):
    vertex = np.zeros((point_count,),
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

    for i in range (point_count):
        theta = np.random.uniform(-np.pi, np.pi)
        phi = np.random.uniform(-np.pi, np.pi)
        x = radius * np.cos(theta) * np.sin(phi)
        y = radius * np.sin(theta) * np.sin(phi)
        z = radius * np.cos(phi)

        vertex[i] = (x + radius, y + radius, z + radius) #add radius to to keep (x,y,z) to be positive (for relu layer)

    return vertex

