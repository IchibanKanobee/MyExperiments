import numpy
from plyfile import PlyElement, PlyData

vertex = numpy.array([(0, 0, 0),
                       (0, 1, 1),
                       (1, 0, 1),
                       (1, 1, 0)],
                      dtype=[('x', 'f4'), ('y', 'f4'),
                             ('z', 'f4')])

print vertex.shape

el = PlyElement.describe(vertex, 'vertex')

PlyData([el]).write('data/some_binary.ply')
