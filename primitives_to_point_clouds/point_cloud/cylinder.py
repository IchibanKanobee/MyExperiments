import numpy as np
import circle, cylinder_side


def get_point_counts(point_count, height, radius):
    s1 = 2 * np.pi * radius * height
    s2 = np.pi * radius * radius
    x = float(point_count) / (s1 + 2 * s2)

    pc1 = int (x * s1)
    pc2 = int (x * s2)
    pc3 = point_count - (pc1 + pc2)
    
    return (pc1, pc2, pc3)



def get_cylinder_point_cloud(point_count, height, radius):
    vertex = np.zeros((point_count,),
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

    pc1, pc2, pc3 = get_point_counts(point_count, height, radius)

    vertex1 = cylinder_side.get_cylinder_side_point_cloud(pc1, height, radius)
    vertex2 = circle.get_circle_point_cloud(pc2, radius, 0)
    vertex3 = circle.get_circle_point_cloud(pc3, radius, height)

    vertex[:pc1] = vertex1
    vertex[pc1:pc1 + pc2] = vertex2
    vertex[pc1 + pc2:pc1 + pc2 + pc3] = vertex3

    return vertex

