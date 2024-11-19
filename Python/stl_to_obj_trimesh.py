import trimesh
import time

start = time.time()

mesh = trimesh.load('test.stl')
mesh.export('test.obj',file_type='obj')

end = time.time()
print(end - start)
