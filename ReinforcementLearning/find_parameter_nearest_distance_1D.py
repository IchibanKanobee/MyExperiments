from point_cloud import PC_1D
from distance import nearest_point
import sys

point_count = 200
goal_length = 50

goal_pc = PC_1D.get_point_cloud_1D(goal_length, point_count)


distance = sys.float_info.max
found_length = 1

for i in xrange (2 * goal_length):
    print "Analysing parameter " + str(i)
    pc = PC_1D.get_point_cloud_1D(i, point_count)
    new_distance = nearest_point.get_point_cloud_nearest_point_distance(goal_pc, pc)
    if (new_distance < distance):
        distance = new_distance
        found_length = i

print distance
print found_length




