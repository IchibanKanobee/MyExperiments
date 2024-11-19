import numpy as np

def reshape_fun(inp):
    print inp

    in_shape = inp.shape
    print in_shape

    dim = 1 
    print in_shape[1:]
    for d in in_shape[1:]: 
        dim *= d 

    print dim

    reshape = inp.reshape([-1, dim])
    return reshape

inp = np.array([[1,1], [2,2], [3,3]])
r = reshape_fun(inp)
print r

inp = np.array([1,2,3,4,5])
r = reshape_fun(inp)
print r

