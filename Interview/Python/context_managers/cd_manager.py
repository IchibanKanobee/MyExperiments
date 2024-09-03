import os

cwd = os.getcwd()
os.chdir('Sample-Dir-One')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('Sample-Dir-Two')
print(os.listdir())
os.chdir(cwd)


class Change_Directory():
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.cwd = os.getcwd()

    def __enter__(self):
        os.chdir(self.dir_name)

    def __exit__(self, exc_type, exc_val, traceback):
        os.chdir(self.cwd)

with Change_Directory('Sample-Dir-One'):
    print(os.listdir())

with Change_Directory('Sample-Dir-Two'):
    print(os.listdir())


