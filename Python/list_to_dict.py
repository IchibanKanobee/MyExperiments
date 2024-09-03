list_ = [1,2,3,4]
count = len(list_)

dict_ = {"a_0" : 0}

for i in range(count):
    key = "a_" + str(i+1)
    dict_[key] = list_[i]

print dict_
