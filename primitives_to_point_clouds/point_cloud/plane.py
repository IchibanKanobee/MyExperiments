import numpy as np


def get_plane_point_cloud(point_count, x_low, x_high, y_low, y_high, z_low, z_high, norm_x, norm_y, norm_z, d):

    vertex = np.zeros((point_count,),
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

    for i in range (point_count):
        if (norm_x != 0.0):
            y = np.random.uniform(y_low, y_high)
            z = np.random.uniform(z_low, z_high)
            x = -(norm_y * y + norm_z * z + d) / norm_x

        elif (norm_y != 0.0):
            x = np.random.uniform(x_low, x_high)
            z = np.random.uniform(z_low, z_high)
            y = -(norm_x * x + norm_z * z + d) / norm_y

        elif (norm_z != 0.0):
            x = np.random.uniform(x_low, x_high)
            y = np.random.uniform(y_low, y_high)
            z = -(norm_x * x + norm_y * y + d) / norm_z
        else:
            x = y = z = 0.0

        vertex[i] = (x, y, z)

    return vertex

