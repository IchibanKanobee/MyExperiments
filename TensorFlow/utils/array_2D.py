import numpy as np
from random import randint


#First elelemnts of this array are random numbers in the range of random_range
#The last elelement is the sum of all previous random numbers

def get_2D_random_sum_array(x, y, random_range):
    records = np.zeros([x, y])
    for i in range (x):
        for j in range (y - 1):
             records[i, j] = (randint(0, random_range))
        records[i, y - 1] = np.sum(records[i, 0:y - 1])
    return records


