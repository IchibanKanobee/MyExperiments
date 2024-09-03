import csv

name = '/media/ara/HDD/MyProjects/pyfin/downloads/nysdaq-july-22-2018csv'

with open(name, 'rb') as f:
    reader = csv.reader(f)
    my_list = list(reader)

print my_list
