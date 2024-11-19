import numpy as np

class RNN:
    def __init__(self):
        self.W_hh = np.array([0,0])
        self.W_xh = np.array([1,1])
        self.W_hy = np.array([1,0])
        self.h = 0

    def step(self, x):
        #update hidden state
        self.h = np.tanh(np.dot(self.W_hh, self.h) + np.dot(self.W_xh, x))
        print self.h
        #compute the output vector
        y = np.dot(self.W_hy, self.h)
        return y

