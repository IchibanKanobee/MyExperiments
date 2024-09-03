import numpy as np

class Perceptron_2:
    def __init__(self, w1, w2, b):
        self.w1 = w1
        self.w2 = w2
        self.b = b

    @property
    def w1(self):
        return self.w1

    @property
    def w2(self):
        return self.w2

    @property
    def b(self):
        return self.b

    def inp(self, x1, x2):
        return self.w1 * x1 + self.w2 * x2 + self.b

    def __activation(self, t):
        return np.tanh(t)

    def out(self, x1, x2):
        return self.__activation(self.inp(x1, x2))

    def activation_deriv(self, x):
        t = np.tanh(x)**2
        return 1.0 - t

    def b_deriv(self, x1, x2):
        return self.activation_deriv(self.inp(x1, x2))
  
    def w1_deriv(self, x1, x2):
        return self.activation_deriv(self.inp(x1, x2)) * x1

    def w2_deriv(self, x1, x2):
        return self.activation_deriv(self.inp(x1, x2)) * x2

