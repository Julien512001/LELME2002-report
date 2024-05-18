import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def variance(x, mean):
    var = 0
    for i in range(len(x)):
        var += (x[i] - mean)**2
    var = var/len(x)
    return var

xR = 0.35
yR = 0.2

xRend = 0.35
yRend = 2.0



xOpp = 1.7
yOpp = 0.36


df = pd.read_csv('lid_opppos2.txt', delimiter=',')
df1 = pd.read_csv('lid_opppos1.txt', delimiter=',')

x = df.iloc[:, 0].values.astype(float)
y = df.iloc[:, 1].values.astype(float)

x1 = df1.iloc[:, 0].values.astype(float)
y1 = df1.iloc[:, 1].values.astype(float)

x = x[x != 0.0]
y = y[y != 0.0]

x1 = x1[x1 != 0.0]
y1 = y1[y1 != 0.0]

trajectoire_x = np.linspace(xR, xRend, len(x1))
trajectoire_y = np.linspace(yR, yRend, len(y1))

dist_rob_opp = np.sqrt((trajectoire_x-xOpp)**2 + (trajectoire_y-yOpp)**2)

std_x = np.sqrt(variance(x1, xOpp))
std_y = np.sqrt(variance(y1, yOpp))

print(std_x)
print(std_y)

std_x = np.sqrt(np.var(x1))
std_y = np.sqrt(np.var(y1))

print(std_x, std_y)
"""
plt.figure()
plt.scatter(x,y, label='opponent')
plt.scatter(xR, yR, label="robot", s=100, c='b')
plt.xlim([0.0, 2.0])
plt.ylim([0.0, 3.0])
plt.xlabel("$x[m]$")
plt.ylabel("$y[m]$")
plt.grid()
plt.gca().set_aspect(1)
"""

"""
error = np.sqrt((x1-xOpp)**2 + (y1 - yOpp)**2)
dist = np.sqrt((trajectoire_x-xOpp)**2 + (trajectoire_y-yOpp)**2)
plt.figure()
plt.scatter(dist, error)
plt.axhline(y=0.04, color='r', linestyle='--', label='y = 4')
"""

plt.figure()
plt.plot([xR, xRend], [yR, yRend], color='blue', label='trajectoire réelle')
plt.scatter([xR, xRend], [yR, yRend], color='red')
plt.scatter(xOpp, yOpp, color='red', s=60)
plt.scatter(x1,y1, label='opponent', alpha=0.1, c='b')
plt.scatter(x1[-1],y1[-1], label='opponent', alpha=1, c='r')
plt.scatter(x1[0],y1[0], label='opponent', alpha=1, c='r')


plt.xlim([1.6, 1.8])
plt.ylim([0.34, 0.46])
plt.xlabel("$x[m]$")
plt.ylabel("$y[m]$")
plt.grid()
plt.gca().set_aspect(1)

plt.figure()
plt.plot(trajectoire_y,np.sqrt((x1- xOpp)**2 + (y1 - yOpp)**2))


plt.show()