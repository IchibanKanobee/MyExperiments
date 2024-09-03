import numpy as np
from random import uniform
import math

def inp(w, x, b):
    return w * x + b


def out(t):
    return np.tanh(t)


def neuron(w, x, b):
    return out(inp(w, x, b))


def tanh_deriv(x):
    t = np.tanh(x)**2
    return 1.0 - t


def neuron_der_b(w, x, b):
    return tanh_deriv(inp(w, x, b))
    
def neuron_der_w(w, x, b):
    return tanh_deriv(inp(w, x, b)) * x


def pred(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b):
    return (w21_x * neuron(w11_x, x, w11_b) + w22_x * neuron(w12_x, x, w12_b) + w2_b)


def func(x):
    return np.sin(x)


def loss(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b):
    l = 0
    for item in x:
        f = func(item)
        p = pred(item, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
        sq = (p - func(item)) * (p - func(item))
        l = l + sq
    print "Loss = " + str(l)
    return l


def loss_deriv_w2_b(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b):
    l = 0
    for item in x:
        f = func(item)
        p = pred(item, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
        sq = 2 * (p - func(item))
        l = l + sq
    print "Loss_deriv_w2_b = " + str(l)
    return l


def loss_deriv_w11_x(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b):
    l = 0
    for item in x:
        f = func(item)
        p = pred(item, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
        sq = 2 * (p - func(item)) * w11_x * neuron_der_w(w11_x, item, w11_b)
        l = l + sq
    print "Loss_derivv_w21_x = " + str(l)
    return l    

def loss_deriv_w12_x(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b):
    l = 0
    for item in x:
        f = func(item)
        p = pred(item, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
        sq = 2 * (p - func(item)) * w12_x * neuron_der_w(w12_x, item, w12_b)
        l = l + sq
    print "Loss_derivv_w21_x = " + str(l)
    return l    

    
def loss_deriv_w21_x(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b):
    l = 0
    for item in x:
        f = func(item)
        p = pred(item, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
        sq = 2 * (p - func(item)) * w21_x * neuron_der_w(w11_x, item, w11_b)
        l = l + sq
    print "Loss_derivv_w21_x = " + str(l)
    return l    


def loss_deriv_w22_x(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b):
    l = 0
    for item in x:
        f = func(item)
        p = pred(item, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
        sq = 2 * (p - func(item)) * w22_x * neuron_der_w(w12_x, item, w12_b)
        l = l + sq
    print "Loss_derivv_w21_x = " + str(l)
    return l    


def loss_deriv_w11_b(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b):
    l = 0
    for item in x:
        f = func(item)
        p = pred(item, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
        sq = 2 * (p - func(item)) * w21_x * neuron_der_b(w11_x, item, w11_b)
        l = l + sq
    print "Loss_derivv_w21_x = " + str(l)
    return l

    
def loss_deriv_w12_b(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b):
    l = 0
    for item in x:
        f = func(item)
        p = pred(item, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
        sq = 2 * (p - func(item)) * w22_x * neuron_der_b(w12_x, item, w12_b)
        l = l + sq
    print "Loss_derivv_w21_x = " + str(l)
    return l    
    

epochs = 1000
step_tanh_w_x = 0.25
step_tanh_w_b = 0.05
step_lin_w_x = 0.25
step_lin_w_b = 0.05
x = np.arange(0, math.pi, 0.05)
print x
y = func(x)
print y

w11_x = uniform(0, 1)
w11_b = uniform(0, 1)

w12_x = uniform(0, 1)
w12_b = uniform(0, 1)

w21_x = uniform(0, 1)
w22_x = uniform(0, 1)

w2_b  = uniform(0, 1)


for i in range(epochs):
    l = loss(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
    print "Loss = " + str(l)
    
    x1 = neuron(w11_x, x, w11_b)
    w21_new = w21_x - step_lin_w_x * loss_deriv_w21_x(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)

    x2 = neuron(w12_x, x, w12_b)
    w22_new = w22_x - step_lin_w_x * loss_deriv_w22_x(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)

    w2_b_new = w2_b - step_lin_w_b * loss_deriv_w2_b(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)

    w11_x_new = w11_x - step_lin_w_x * loss_deriv_w11_x(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
    w12_x_new = w12_x - step_lin_w_x * loss_deriv_w12_x(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
    w11_b_new = w11_b - step_lin_w_b * loss_deriv_w11_b(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
    w12_b_new = w12_b - step_lin_w_b * loss_deriv_w12_b(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
        
    w21_x = w_21_new
    w22_x = w22_new
    w2_b = w2_b_new
    
    w11_x = w11_new
    w12_x = w22_new
    w11_b = w11_b_new
    w12_b = w12_b_new
    
    z = pred(x, w11_x, w11_b, w12_x, w12_b, w21_x, w22_x, w2_b)
    print x
    print y
    




