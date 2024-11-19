#Teaching a single neuron to calculate 2 X A + 8 function


import numpy as np
from random import uniform

def tanh(x):
    return np.tanh(x)

def tanh_deriv(x):
#    print "x = " + str(x)
    t = np.tanh(x)**2
#    print "t = " + str(t)
    return 1.0 - t

def pred(w_x, x, w_b):
    return (tanh(w_x * x + w_b))

def pred_deriv_w_x(w_x, x, w_b):
    l = (tanh_deriv(w_x * x + w_b) * x)
#    print "pred_deriv_w_x = " + str(l)
    return l

def pred_deriv_w_b(w_x, x, w_b):
    l = tanh_deriv(w_x * x + w_b)
#    print "pred_deriv_w_b = " + str(l)
    return l

def func(x):
#    return (2 * x + 8)
    return (2 * x)

def loss(w_x, x, w_b):
    l = 0
    for item in x:
        f = func(item)
        p = pred(w_x, item, w_b)
        sq = (pred(w_x, item, w_b) - func(item)) * (pred(w_x, item, w_b) - func(item))
        l = l + sq
    print "Loss = " + str(l)
    return l

def loss_deriv_w_x(w_x, x, w_b):
    l = 0
    for item in x:
        sq = 2 * (pred(w_x, item, w_b) - func(item)) * pred_deriv_w_x(w_x, item, w_b)
        l = l + sq
#    print "Loss_deriv_w_x = " + str(l)
    return l

def loss_deriv_w_b(w_x, x, w_b):
    l = 0
    for item in x:
        sq = 2 * (pred(w_x, item, w_b) - func(item)) * pred_deriv_w_b(w_x, item, w_b)
        l = l + sq
    print "Loss_deriv_w_b = " + str(l)
    return l

epochs = 1000
step_w_x = 1.0
step_w_b = 1.0
x = np.arange(0, 1, 0.05)
print x

w_x = uniform(0, 1)
w_b = uniform(0, 1)

for i in range(epochs):
    l = loss(w_x, x, w_b)
    w_x = w_x - step_w_x * loss_deriv_w_x(w_x, x, w_b)
    print "w_x = " + str(w_x)
    w_b = w_b - step_w_b * loss_deriv_w_b(w_x, x, w_b)
    print "w_b = " + str(w_b)    

