import numpy as np
import plane


def get_point_counts(point_count, length, width, height):
    s1 = length * width
    s2 = length * height
    s3 = width * height
    x = float(point_count) / (2 * (s1 + s2 + s3))

    pc1 = int (x * s1)
    pc2 = int (x * s2)
    pc3 = pc2
    pc4 = int (x * s3)
    pc5 = pc4
    pc6 = point_count - (pc1 + pc2 + pc3 + pc4 + pc5)
    
    return (pc1, pc2, pc3, pc4, pc5, pc6)



def get_box_point_cloud(point_count, length, width, height):

    vertex = np.zeros((point_count,),
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

    pc1, pc2, pc3, pc4, pc5, pc6 = get_point_counts(point_count, length, width, height)

    vertex1 = plane.get_plane_point_cloud(pc1, 0, length, 0, 0, 0, width, 0, 1, 0, 0)
    vertex6 = plane.get_plane_point_cloud(pc6, 0, length, 0, 0, 0, width, 0, 1, 0, -height)

    vertex2 = plane.get_plane_point_cloud(pc2, 0, length, 0, height, 0, 0, 0, 0, 1, 0)
    vertex3 = plane.get_plane_point_cloud(pc3, 0, length, 0, height, 0, 0, 0, 0, 1, -width)

    vertex4 = plane.get_plane_point_cloud(pc4, 0, 0, 0, height, 0, width, 1, 0, 0, 0)
    vertex5 = plane.get_plane_point_cloud(pc5, 0, 0, 0, height, 0, width, 1, 0, 0, -length)

    vertex[:pc1] = vertex1
    vertex[pc1:pc1 + pc2] = vertex2
    vertex[pc1 + pc2:pc1 + pc2 + pc3] = vertex3
    vertex[pc1 + pc2 + pc3:pc1 + pc2 + pc3 + pc4] = vertex4
    vertex[pc1 + pc2 + pc3 + pc4:pc1 + pc2 + pc3 + pc4 + pc5] = vertex5
    vertex[pc1 + pc2 + pc3 + pc4 + pc5:pc1 + pc2 + pc3 + pc4 + pc5 + pc6] = vertex6

    return vertex

