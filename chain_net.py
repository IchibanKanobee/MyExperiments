x = 1
f = []
f.append(x + 1)
f.append(f[-1] + 3)
print f[-1] #should be 5 (1 + 1) + 3
