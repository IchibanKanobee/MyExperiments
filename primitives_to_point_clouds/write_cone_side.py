import numpy as np
from plyfile import plyfile
from point_cloud import cone_side

point_count = 2048

radius = 100.
angle = np.pi/3.

vertex = cone_side.get_cone_side_point_cloud(point_count, angle, radius)

el = plyfile.PlyElement.describe(vertex, 'vertex')

plyfile.PlyData([el]).write('data/cone_side.ply')
