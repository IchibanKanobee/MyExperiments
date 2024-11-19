import numpy as np
import os

VECTOR_SOURCE_DIR = '/raid/vae_mvcnn_tiled_feature_vectors/vector_arithmetics'
AIRPLANE_VECTOR_SOURCE_DIR = VECTOR_SOURCE_DIR + "/airplane/samples"
SHIP_VECTOR_SOURCE_DIR = VECTOR_SOURCE_DIR + "/airplane/samples"
OUTPUT_DIR = VECTOR_SOURCE_DIR + "/" + "results"
AVERAGE_VECTOR_FILE_NAME = "average_airplane.txt"
AIRPLANE_MILITARY_MINUS_CIV1_PLUS_CIV2 = "airplane_military_minus_civ1_plus_civ2.txt"
AIRPLANE_MINUS_SHIP1_PLUS_SHIP2 = "airplane_minus_ship1_plus_ship2.txt"
NEW_MILITARY_FROM_RATIO = "new_miltary_airplane_from_ratio.txt"
AIRPLANE_SQUARE_ROOT = "airplane_square_root.txt"



def div0( a, b ):
    """ ignore / 0, div0( [-1, 0, 1], 0 ) -> [0, 0, 0] """
    with np.errstate(divide='ignore', invalid='ignore'):
        c = np.true_divide( a, b )
        c[ ~ np.isfinite( c )] = 0  # -inf inf NaN
    return c


#average airplane
fv = []
for file in os.listdir(AIRPLANE_VECTOR_SOURCE_DIR):
    if file.endswith(".txt"):
        fv.append(file)

file_count = len(fv)

print file_count

file_name = os.path.join(AIRPLANE_VECTOR_SOURCE_DIR, fv[0])
average_vector = np.loadtxt(file_name)

for i in range(1, file_count):
    file_name = os.path.join(AIRPLANE_VECTOR_SOURCE_DIR, fv[i])
    average_vector += np.loadtxt(file_name)

average_vector = average_vector / file_count
res = np.asarray(average_vector)
np.savetxt(OUTPUT_DIR + "/" + AVERAGE_VECTOR_FILE_NAME, res)


#military_minus_civilian
military_file_name = os.path.join(AIRPLANE_VECTOR_SOURCE_DIR, "feature_vector_0021.txt")
military_vector = np.loadtxt(military_file_name)

civilian_file_name = os.path.join(AIRPLANE_VECTOR_SOURCE_DIR, "feature_vector_0012.txt")
civilian_vector1 = np.loadtxt(civilian_file_name)

vector = np.loadtxt(military_file_name)
dif = vector - civilian_vector1


#dif_plus_civilian2
civilian_file_name = os.path.join(AIRPLANE_VECTOR_SOURCE_DIR, "feature_vector_0031.txt")
civilian_vector2 = np.loadtxt(civilian_file_name)

#add difference to civilian airplane several times
vector = civilian_vector2 + dif
res = np.asarray(vector)
file_name = OUTPUT_DIR + "/" + AIRPLANE_MILITARY_MINUS_CIV1_PLUS_CIV2
np.savetxt(file_name, res)


#airplane_minus_ship
airplane_file_name = os.path.join(AIRPLANE_VECTOR_SOURCE_DIR, "feature_vector_0012.txt")
airplane_vector = np.loadtxt(airplane_file_name)

ship_file_name1 = os.path.join(SHIP_VECTOR_SOURCE_DIR, "feature_vector_0000.txt")
ship_vector1 = np.loadtxt(ship_file_name1)

dif = airplane_vector- ship_vector1

#dif_plus_ship2
ship_file_name = os.path.join(SHIP_VECTOR_SOURCE_DIR, "feature_vector_0002.txt")
ship_vector2 = np.loadtxt(civilian_file_name)

#add difference to civilian airplane several times
vector = ship_vector2 + dif
res = np.asarray(vector)
file_name = OUTPUT_DIR + "/" + AIRPLANE_MINUS_SHIP1_PLUS_SHIP2
np.savetxt(file_name, res)


#ratio
military_vector2 = div0(military_vector, civilian_vector1) * civilian_vector2
res = np.asarray(military_vector2)
file_name = OUTPUT_DIR + "/" + NEW_MILITARY_FROM_RATIO
np.savetxt(file_name, res)


#square_root
civilian_vector_sq_root = np.sqrt(civilian_vector1)
res = np.asarray(civilian_vector_sq_root)
file_name = OUTPUT_DIR + "/" + AIRPLANE_SQUARE_ROOT
np.savetxt(file_name, res)

