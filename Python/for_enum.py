import numpy as np

for i, d in enumerate(['/gpu:0', '/gpu:1']):
    print(i)
    print(d)
    print("----")


a = np.arange(8)
print(a)

gpus = ['/gpu:0', '/gpu:1']
count = len(gpus)
for i, d in enumerate(gpus):
    print(a[i*count] + a[i*count+1])
    print(d)
    print("----")

