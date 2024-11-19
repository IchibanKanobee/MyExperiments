import numpy
a = numpy.array([[0.0,1.630000e+01,1.990000e+01,1.840000e+01],
                 [1.0,1.630000e+01,1.990000e+01,1.840000e+01],
                 [2.0,1.630000e+01,1.990000e+01,1.840000e+01]])
with open('final.txt', 'wb') as f:
    f.write(b'SP,1,2,3\n')
    numpy.savetxt(f, a, fmt="%10.5f", delimiter=",")
