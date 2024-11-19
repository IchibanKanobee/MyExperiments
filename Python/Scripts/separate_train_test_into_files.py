import os

root = "/raid/data/hpinn"
#root = "/home/ara/Desktop/xbox"

file_train = open('file_train.txt', 'w')
file_test = open('file_test.txt', 'w')

for path, subdirs, files in os.walk(root):
    for name in files:
        inp = os.path.join(path, name)
        print inp
        if "train" in inp:
            file_train.write(inp + "\n")
        elif "test" in inp:
            file_test.write(inp + "\n")


