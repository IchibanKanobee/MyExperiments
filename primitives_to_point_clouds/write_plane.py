import numpy as np
from plyfile import plyfile
from point_cloud import plane

point_count = 2048
x_low = 0.
x_high = 100.

y_low = 0.
y_high = 100.

z_low = 0.
z_high = 100.

norm_x = 1.
norm_y = 1.
norm_z = 1.
d = 0

vertex = plane.get_plane_point_cloud(point_count, x_low, x_high, y_low, y_high, z_low, z_high, norm_x, norm_y, norm_z, d)

el = plyfile.PlyElement.describe(vertex, 'vertex')

name = "data/plane_" + str(int(norm_x)) + "_" + str(int(norm_y)) + "_" + str(int(norm_z)) + "_" + str(int(d)) + "_.ply"  

plyfile.PlyData([el]).write(name)
