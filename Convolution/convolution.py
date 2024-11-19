import numpy as np
from scipy import misc

def convolve_one_step(mat, con):
    con_shape = con.shape
    mat_shape = mat.shape
    if (mat_shape != con_shape):
            raise Exception("The size of kernel must be equal to the size of convolved matrix part")
    result = 0
    for i in range (con_shape[0]):
        for j in range (con_shape[1]):
            result += con[i, j] * mat[i, j]
    return result

def get_stride_pad(mat, con, stride):
    mat_shape = mat.shape
    con_shape =con.shape
    stride_pad_x = stride - (mat_shape[0] - con_shape[0]) % stride
    stride_pad_y = stride - (mat_shape[1] - con_shape[1]) % stride
    return (stride_pad_x, stride_pad_y)


def convolve(mat, con, stride = 1):
    #Step 1 pad to be able to start with (0, 0)
    con_shape = con.shape
    pad_x = (int) (con_shape[0] / 2)
    pad_y = (int) (con_shape[1] / 2)
    npad = ((pad_x, pad_x), (pad_y, pad_y))
    mat_pad = np.pad(mat, pad_width=npad, mode='constant', constant_values=0)
    mat_shape = mat.shape
    print mat_pad

    #Step2 Extend mat_pad if necessary to adjust for strides > 1
    stride_pad_x, stride_pad_y = get_stride_pad(mat_pad, con, stride)
    npad = (0, stride_pad_x), (0, stride_pad_y)
    mat_pad = np.pad(mat_pad, pad_width=npad, mode='constant', constant_values=0)

    #Step 3 apply convolution to each slice of the size og the convolution matrix

    count_x = (int) (mat_shape[0] / stride)
    count_y = (int) (mat_shape[1] / stride)

    res = np.zeros(shape = (count_x, count_y))

    for i in range (count_x):
        for j in range(count_y):
            res[i,j] = convolve_one_step(mat_pad[i*stride:i*stride+con_shape[0], j*stride:j*stride+con_shape[0]], con)

    return res



def normalize(mat):
    res = mat.clip(0, 255)
    return res


lena = misc.imread('lena512.jpg')
print (lena)

print (lena.shape)
print (lena.dtype)

mat3 = np.ones(9)
mat3 = mat3.reshape(3,3)
print mat3

#mat4 = np.array([[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]])

mat4 = np.ones([4,4])

con3 = np.array([[-1, -1, -1], [-1,8,-1], [-1,-1,-1]])
#print con3

#res = convolve_one_step(mat3, con3)
#print res

#res = convolve(mat4, con3)
res = convolve(mat4, con3, 2)
print mat4


lena_con = convolve(lena, con3)
lena_res = normalize(lena_con)
misc.imsave("lena_con_stride_1.jpg", lena_res)

lena_con = convolve(lena, con3, 2)
lena_res = normalize(lena_con)
misc.imsave("lena_con_stride_2.jpg", lena_res)

