#Context managers allow us to properly manage resources so we can specify what to set up and tear down when working with certain objects
from contextlib import contextmanager

# f = open('sample.txt', 'w')
# f.write('Lopern ipsum dolor sit amet')
# f.close()

with open('sample.txt', 'w') as f:
    f.write('Lopern ipsum dolor sit amet')


class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_File('sample2.txt', 'w') as f:
    f.write('Lopern ipsum dolor sit amet')

print (f.closed)

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with open_file('sample3.txt', 'w') as f:
    f.write('Lopern ipsum dolor sit amet')


print (f.closed)