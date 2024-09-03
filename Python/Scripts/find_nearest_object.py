import numpy as np
import os
from os import listdir
from os.path import isfile, join
import pprint, pickle


INPUT_DIR='/raid/vae_mvcnn_tiled_feature_vectors/restore_from_sketch/pickles/input'
UNIVERSE_DIR='/raid/vae_mvcnn_tiled_feature_vectors/restore_from_sketch/pickles/universe'


def get_list_of_files(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles


def distance(A, B):
    return np.sqrt(np.sum((A - B)**2))


def load_from_picke(filename):
    pkl_file = open(filename, 'rb')

    data = pickle.load(pkl_file)
#    pprint.pprint(data)

    pkl_file.close()
    return data


input_vectors = []
inputs = get_list_of_files(INPUT_DIR)
for i in inputs:
    data = load_from_picke(os.path.join(INPUT_DIR, i))
    #only the first elelemnt of data is meaningful, the rest are white images
    img = data[0]
    input_vectors.append(img)


universe_vectors = []
universe = get_list_of_files(UNIVERSE_DIR)
for u in universe:
    data = load_from_picke(os.path.join(UNIVERSE_DIR, u))
    universe_vectors.append(data)


input_count = len(input_vectors)
univ_count = len(universe_vectors)


for i in range(input_count):
    # Start with an arbitratry (but large) minimum distance
    min_dist = 10000
    nearest_object = ""
    nearest_index = -1

    for u in range(univ_count):
        u_vector = universe_vectors[u]
        sh = u_vector.shape
        for j in range(sh[0]):
            dist = distance(input_vectors[i], u_vector[j])
            if (dist < min_dist):
                nearest_object = universe[u]
                nearest_index = j
                min_dist = dist

    print "Nearest object is: " + nearest_object
    print "Nearest index is: " + str(nearest_index)
    print "Nearest distance: " + str(min_dist)




