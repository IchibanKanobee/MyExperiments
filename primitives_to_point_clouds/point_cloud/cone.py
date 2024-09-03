import numpy as np
import circle, cone_side


def get_point_counts(point_count, angle, radius):
    height = radius * np.tan(angle)
    s1 = np.pi * radius * np.sqrt(radius*radius + height*height)
    s2 = np.pi * radius * radius
    x = float(point_count) / (s1 + s2)

    pc1 = int (x * s1)
    pc2 = point_count - pc1
    
    return (pc1, pc2)


def get_cone_point_cloud(point_count, angle, radius):
    vertex = np.zeros((point_count,),
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

    pc1, pc2 = get_point_counts(point_count, angle, radius)

    vertex1 = cone_side.get_cone_side_point_cloud(pc1, angle, radius)
    vertex2 = circle.get_circle_point_cloud(pc2, radius, 0)

    vertex[:pc1] = vertex1
    vertex[pc1:pc1 + pc2] = vertex2

    return vertex

