import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dflid1 = pd.read_csv('lidar_diag.txt', delimiter=',')

x1, y1 = 0.35, 0.2
x2, y2 = 1.7, 2.0

xRend = 1.7
yRend = 2.0

xlid1 = dflid1.iloc[:, 0].values.astype(float)
ylid1 = dflid1.iloc[:, 1].values.astype(float)
thetalid1 = dflid1.iloc[:, 2].values.astype(float)

xlid1 = xlid1[xlid1 != 0.0]
ylid1 = ylid1[ylid1 != 0.0]
thetalid1 = thetalid1[thetalid1 != 0.0]

xlid1 = xlid1[::300]
ylid1 = ylid1[::300]
thetalid1 = thetalid1[::300]

print(xlid1.shape, ylid1.shape, thetalid1.shape)

print(xlid1[-1])
print(ylid1[-1])

error_x = xlid1[-1] - xRend
error_y = ylid1[-1] - yRend
error_dist = np.sqrt(error_x*error_x + error_y*error_y)


print("e_x : {}, e_y : {}, e_dist : {}".format(error_x, error_y, error_dist))

xlid1 = dflid1.iloc[::300, 0].values.astype(float)
ylid1 = dflid1.iloc[::300, 1].values.astype(float)
thetalid1 = dflid1.iloc[::300, 2].values.astype(float)
radlid1 = np.radians(thetalid1)






plt.figure()
plt.scatter(ylid1, thetalid1)


plt.figure()
plt.scatter(xlid1,ylid1, color="red", label = "LiDar")
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



plt.show()