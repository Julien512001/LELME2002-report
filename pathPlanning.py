import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Le robot va en (1.7, 2.2)

dflid1 = pd.read_csv('path.txt', delimiter=',')


xlid1 = dflid1.iloc[::300, 0].values.astype(float)
ylid1 = dflid1.iloc[::300, 1].values.astype(float)
thetalid1 = dflid1.iloc[::300, 2].values.astype(float)
radlid1 = np.radians(thetalid1)

xlid1 = xlid1[xlid1 != 0.0]
ylid1 = ylid1[ylid1 != 0.0]
radlid1 = radlid1[radlid1 != 0.0]

plt.scatter(xlid1,ylid1, color="yellow")

plt.scatter(xlid1[0], ylid1[0], s=100, color="blue")
plt.scatter(xlid1[-1], ylid1[-1], s=100, color="blue")
circle = plt.Circle((1.5, 1.5), radius=0.125, color='red', fill=True)
plt.gca().add_artist(circle)
plt.text(1.5 + 0.125, 1.5, 'opponent', verticalalignment='center')


"""
plt.scatter(xodo,yodo, color="blue", alpha=0.01)
#plt.quiver(xodo, yodo, np.cos(radodo), np.sin(radodo), angles='xy', scale_units='xy', scale=1000, color='red', label='Orientation')
"""
plt.xlim([0.0, 2.0])
plt.ylim([0.0, 3.0])
plt.gca().set_aspect(1)
plt.xlabel("$x[m]$")
plt.ylabel("$y[m]$")
plt.grid()



plt.show()