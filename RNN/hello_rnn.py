import numpy as np
from RNN import RNN

x = np.array([1,1])

rnn = RNN()
y = rnn.step(x)
print y
