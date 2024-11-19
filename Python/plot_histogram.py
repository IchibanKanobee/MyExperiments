import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle



a = [[1,1,2],[3,3,3,3,4],[2,2,2,5,5]]


f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)

text = "1 - Airplane, 2 - Piano"
plt.xlabel('True Labels')


ax1.hist(a[0])
ax2.hist(a[1])
ax3.hist(a[2])

extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)

plt.show()

