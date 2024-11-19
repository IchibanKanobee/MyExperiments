import pandas as pd
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(46)
import seaborn as sns

# create data
a = np.random.rayleigh(20, size=1000)
b = 80*np.sin(np.sqrt((a+1)/20.*np.pi/2.))
df = pd.DataFrame({"age" : a,  "weight" : b})

# calculate age density and mean weight
bins = np.arange(0,100,10)
groups = df.groupby([pd.cut(df.age, bins),'weight' ])
df2 = groups.size().reset_index(["age","weight"])

df3 = df2.groupby("age")[0].sum()
df4 = df2.groupby("age")["weight"].mean()

df6 = pd.concat([df3,df4], axis=1)
df6["density"] = df6[0]/np.sum(df6[0].fillna(0).values*np.diff(bins))

# prepare colors
norm=plt.Normalize(np.nanmin(df6["weight"].values), 
                   np.nanmax(df6["weight"].values))
colors = plt.cm.plasma(norm(df6["weight"].fillna(0).values))

# create figure and axes
fig, ax = plt.subplots()
# bar plot
ax.bar(bins[:-1],df6.fillna(0)["density"], width=10, color=colors, align="edge")
# KDE plot
sns.kdeplot(df["age"], ax=ax, color="k", lw=2)

#create colorbar
sm = plt.cm.ScalarMappable(cmap="plasma", norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, label="weight")

#annotate axes
ax.set_ylabel("density")
ax.set_xlabel("age")
plt.show()
