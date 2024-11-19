import json

data  = ["a", "b", "c"]

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

with open('data.json', 'r') as infile:
    data = json.load(infile)
    print (data)


dict_list = [{"age":10, "sex":"male"}, {"age":8, "sex":"female", "name": "Nikki"}, {"age":9}]

with open('dict_list.json', 'w') as outfile:
    json.dump(dict_list, outfile)

with open('dict_list.json', 'r') as infile:
    data = json.load(infile)
    print (data)

