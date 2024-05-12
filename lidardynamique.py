import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dflid1 = pd.read_csv('lid_robpos1.txt', delimiter=',')
dflid2 = pd.read_csv('lid_robpos2.txt', delimiter=',')
dflid3 = pd.read_csv('lid_robpos3.txt', delimiter=',')


dfodo = pd.read_csv('odo_robpos1.txt', delimiter=',')

x1, y1 = 0.35, 0.2
x2, y2 = 0.35, 2.0



xlid1 = dflid1.iloc[:, 0].values.astype(float)
ylid1 = dflid1.iloc[:, 1].values.astype(float)
thetalid1 = dflid1.iloc[:, 2].values.astype(float)
radlid1 = np.radians(thetalid1)

xlid2 = dflid2.iloc[:, 0].values.astype(float)
ylid2 = dflid2.iloc[:, 1].values.astype(float)
thetalid2 = dflid2.iloc[:, 2].values.astype(float)
radlid2 = np.radians(thetalid2)

xlid3 = dflid3.iloc[:, 0].values.astype(float)
ylid3 = dflid3.iloc[:, 1].values.astype(float)
thetalid3 = dflid3.iloc[:, 2].values.astype(float)
radlid3 = np.radians(thetalid3)


xodo = dfodo.iloc[:, 0].values.astype(float)
yodo = dfodo.iloc[:, 1].values.astype(float)
thetaodo = dfodo.iloc[:, 2].values.astype(float)
radodo = np.radians(thetaodo)

plt.scatter(xlid1,ylid1, color="red", alpha=0.1)
plt.plot([x1, x2], [y1, y2], color='blue', label='trajectoire réelle')
plt.scatter([x1, x2], [y1, y2], color='blue')
#plt.scatter(xlid2,ylid2, color="black", alpha=0.1)
#plt.scatter(xlid3,ylid3, color="yellow", alpha=0.1)
#plt.quiver(xlid, ylid, np.cos(radlid), np.sin(radlid), angles='xy', scale_units='xy', scale=1000, color='red', label='Orientation')

"""
plt.scatter(xodo,yodo, color="blue", alpha=0.01)
#plt.quiver(xodo, yodo, np.cos(radodo), np.sin(radodo), angles='xy', scale_units='xy', scale=1000, color='red', label='Orientation')
"""
plt.xlim([0.3, 0.4])
plt.ylim([0.0, 3.0])
plt.gca().set_aspect(1/10)
plt.xlabel("$x[m]$")
plt.ylabel("$y[m]$")
plt.grid()

"""
dist = np.sqrt(xlid2**2 + ylid2**2)
plt.figure()
plt.axhline(y=90, color='r', linestyle='--', label='y = 90')
plt.plot(dist, thetalid2)

dist = np.sqrt(xlid3**2 + ylid3**2)
plt.figure()
plt.axhline(y=90, color='r', linestyle='--', label='y = 90')
plt.plot(dist, thetalid3)
"""


plt.show()