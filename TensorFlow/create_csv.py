import numpy as np
from utils import array_2D

record_count = 500
element_count = 5
random_range = 10

records = array_2D.get_2D_random_sum_array(record_count, element_count, random_range)
print records

#Store in the csv file
filename = "Synthetic_data_%d.csv" % (record_count)
np.savetxt(filename, records.astype(int), fmt="%i", delimiter=",")

