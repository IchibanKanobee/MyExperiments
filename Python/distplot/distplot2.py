import numpy as np
import matplotlib.pyplot as plt

data = np.random.rayleigh(size=30)

hist, edges = np.histogram(data)

norm = plt.Normalize(hist.min(), hist.max())
colors = plt.cm.YlGnBu(norm(hist)) 

fig, ax = plt.subplots()
ax.bar(edges[:-1], hist, np.diff(edges), color=colors, ec="k", align="edge")

plt.show()
