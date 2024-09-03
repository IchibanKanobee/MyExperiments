import matplotlib.pyplot as plt
import numpy as np

def loss(reg, truth):
    count = reg.size
    sum = 0
    for i in range (count):
        sum += (reg[i] - truth[i]) * (reg[i] - truth[i])
    sum = sum / count
#    print "loss = " + str(sum)
    return sum


def dif_loss_a(a, x, b, y):
    count = x.size
    sum = 0

    for i in range(count):
        sum += 2 * (a * x[i] + b - y[i]) * x[i]

    sum = sum / count
    print "diff_loss_a = " + str(sum)
    return sum


def dif_loss_b(a, x, b, y):
    count = x.size
    sum = 0

    for i in range(count):
        sum += 2 * (a * x[i] + b - y[i])

    sum = sum / count
    print "diff_loss_b = " + str(sum)
    return sum


def set_y(a, x, b):
    count = x.size
    y = np.zeros(shape = (count,))
    for i in range (count):
        y[i] = a * x[i] + b
    return y

count = 200
random_range = 20

step_a = 0.000001
step_b = 1.0

iter = 100000

a = 0.35
b = 37

x = np.arange(count)
y = np.zeros(shape = (count,))

for i in range(count):
    y[i] = a * x[i] + b + np.random.uniform(- count / 20, count / 20)



a_reg = np.random.uniform(- count / 20, count / 20)
b_reg = np.random.uniform(- count / 2, count / 2)

print a_reg, b_reg

y_reg = set_y(a_reg, x, b_reg)
print y_reg



hl, = plt.plot([], [])
plt.axis([0, count, 0, 100])
plt.scatter(x, y)
hl.set_xdata(x)
hl.set_ydata(y_reg)
plt.draw()

l = loss(y_reg, y)
for i in range(iter):
    a_reg = a_reg - dif_loss_a(a_reg, x, b_reg, y) * step_a
    b_reg = b_reg - dif_loss_b(a_reg, x, b_reg, y) * step_b
    print a_reg, b_reg
    y_reg = set_y(a_reg, x, b_reg)
#    for j in range(count):
#        print "y[" + str(j) + "] = " + str(y_reg[i])

    l = loss(y_reg, y)
    print "loss = " + str(l)

#    hl.set_xdata(x)
    hl.set_ydata(y_reg)
    plt.draw()

i = 1
