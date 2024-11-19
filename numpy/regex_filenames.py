from os import listdir
from os.path import isfile, join
import re

mypath = '/raid/data/tinkercad/multi_view/final_design/0A1r3WnIJde'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print (onlyfiles)
print("\n------------------------------\n")
r = re.compile(".*00.png")
re_files = list(filter(r.match, onlyfiles))
print(re_files)
