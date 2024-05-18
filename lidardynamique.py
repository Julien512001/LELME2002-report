import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dflid1 = pd.read_csv('lid_robpos1.txt', delimiter=',')

dfodo = pd.read_csv('odo_robpos1.txt', delimiter=',')

x1, y1 = 0.35, 0.2
x2, y2 = 0.35, 2.0




xlid1 = dflid1.iloc[:, 0].values.astype(float)
ylid1 = dflid1.iloc[:, 1].values.astype(float)
thetalid1 = dflid1.iloc[:, 2].values.astype(float)
radlid1 = np.radians(thetalid1)


print(xlid1[-1])
print(ylid1[-1])

error_x = xlid1[-1] - x2
error_y = ylid1[-1] - y2
error_dist = np.sqrt(error_x*error_x + error_y*error_y)

print("e_x : {}, e_y : {}, e_dist : {}".format(error_x, error_y, error_dist))

plt.figure()
plt.scatter(ylid1, thetalid1)

plt.figure()
plt.scatter(xlid1,ylid1, color="red", label='LiDar')
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
plt.legend()
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