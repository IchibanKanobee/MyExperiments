import numpy as np

def get_cone_side_point_cloud(point_count, angle, radius):
    vertex = np.zeros((point_count,),
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

    for i in range (point_count):
        x = np.random.uniform(-radius, radius)
        z_ = np.random.uniform(np.sqrt(radius*radius - x*x))
        s = np.random.uniform(-1,1)
        z = np.sign(s) * z_
        y = (radius - np.sqrt(x*x + z*z)) * np.tan(angle)

        vertex[i] = (x + radius, y, z + radius) #Add radius to (x, z) to make them positive for relu layer

    return vertex

