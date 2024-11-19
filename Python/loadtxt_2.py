import numpy
with open('final.txt', 'rb') as f:
    a = f.readline()
    print a
    b = numpy.loadtxt(f, delimiter=",")
    print b
