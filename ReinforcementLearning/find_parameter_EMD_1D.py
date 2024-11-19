from point_cloud import PC_1D
from distance import EMD
import sys

point_count = 20
goal_length = 10

goal_signature = PC_1D.get_point_cloud_signature_1D(goal_length, point_count)

distance = sys.float_info.max
found_length = 1

for i in xrange (2 * goal_length):
    print "Analysing parameter " + str(i)
    signature = PC_1D.get_point_cloud_signature_1D(i, point_count)
    new_distance = EMD.getEMD(signature, goal_signature)
    if (new_distance < distance):
        distance = new_distance
        found_length = i

print distance
print found_length



