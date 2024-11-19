import json


#create dict_list.json by running json_save_load.py
with open('dict_list.json', 'r') as infile:
    data = json.load(infile)
    print data

keys = []
counts = []

dict_keys = []

count = len(data)
for i in range (count):
    dict_keys.append(data[i].keys())

print dict_keys

for i in range (count):
    length = len(dict_keys[i])
    for j in range (length):
        if not dict_keys[i][j] in keys:
            keys.append(dict_keys[i][j])
            counts.append(1)
        else:
            index = keys.index(dict_keys[i][j])
            counts[index] = counts[index] + 1

print (keys)
print (counts)

stats = {}
count = len(keys)
for i in range (count):
    stats[keys[i]] = counts[i]

print (stats)
with open('dict_stats.json', 'w') as outfile:
    json.dump(stats, outfile)

