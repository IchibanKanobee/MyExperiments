import numpy as np

class Perceptron_2:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    @property
    def w(self):
        return self.w

    @property
    def b(self):
        return self.b

    def inp(self, x):
        return self.w * x + self.b

    def __activation(self, t):
        return np.tanh(t)

    def out(self, x):
        return self.__activation(self.inp(x))

    def activation_deriv(self, x):
        t = np.tanh(x)**2
        return 1.0 - t

    def deriv_b(self, x):
        return self.activation_deriv(self.inp(x))
  
    def deriv_w(self, x):
        return self.activation_deriv(self.inp(x)) * x

