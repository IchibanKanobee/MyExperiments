import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.rayleigh(size=30)

ax = sns.distplot(data)

vals = np.array([rec.get_height() for rec in ax.patches])
norm = plt.Normalize(vals.min(), vals.max())
colors = plt.cm.YlGnBu(norm(vals))

for rec, col in zip(ax.patches, colors):
    rec.set_color(col)

plt.show()
