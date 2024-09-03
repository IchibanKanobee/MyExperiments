from os import listdir, rename
from os.path import isfile, join
mypath = "dog"

for i, filename in enumerate(listdir(mypath)):
    rename(mypath + "/" + filename, mypath + "/" + mypath + "_" + str(i) + ".jpg")


