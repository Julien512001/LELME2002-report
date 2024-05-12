import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dflid1 = pd.read_csv('lidar_diag.txt', delimiter=',')


dfodo = pd.read_csv('odo_robpos1.txt', delimiter=',')


x1, y1 = 0.35, 0.2
x2, y2 = 1.7, 2.0



xlid1 = dflid1.iloc[::300, 0].values.astype(float)
ylid1 = dflid1.iloc[::300, 1].values.astype(float)
thetalid1 = dflid1.iloc[::300, 2].values.astype(float)
radlid1 = np.radians(thetalid1)

xlid1 = xlid1[xlid1 != 0.0]
ylid1 = ylid1[ylid1 != 0.0]
radlid1 = radlid1[radlid1 != 0.0]

xodo = dfodo.iloc[:, 0].values.astype(float)
yodo = dfodo.iloc[:, 1].values.astype(float)
thetaodo = dfodo.iloc[:, 2].values.astype(float)
radodo = np.radians(thetaodo)


plt.scatter(xlid1,ylid1, color="red")
plt.plot([x1, x2], [y1, y2], color='blue', label='trajectoire réelle')
plt.scatter([x1, x2], [y1, y2], color='blue')

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