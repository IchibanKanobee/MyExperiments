import numpy as np
from plyfile import plyfile
from point_cloud import circle

point_count = 2048

radius = 100.
shift = 0

vertex = circle.get_circle_point_cloud(point_count, radius, shift)

el = plyfile.PlyElement.describe(vertex, 'vertex')

plyfile.PlyData([el]).write('data/circle.ply')
