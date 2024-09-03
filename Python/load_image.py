from PIL import Image
import numpy as np

image = Image.open("img-10-01.png")
np_image = np.array(image)
sh = np_image.shape
print sh

f1=open('out.txt', 'w+')

for i in range (sh[0]):
    for j in range(sh[1]):
        print >> f1, np_image[i][j]




f1.close()
#np_tile = np.tile(np_image, 3)
#np_3_channels = np_tile.reshape([sh[0], sh[1], -1])
#print (np_image.shape)
#print (np_3_channels.shape)
#assert (np_3_channels[0] == np_image)
