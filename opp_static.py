import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


xR = 0.35
yR = 0.2

x = np.array([1.36, 0.95, 0.9])
y = np.array([0.48, 1.49, 2.03])

xreal = np.array([1.4, 1.03, 1.01])
yreal = np.array([0.44, 1.48, 2.0])



dist_real = np.sqrt((xreal-xR)**2 + (yreal-yR)**2)
error = np.sqrt((xreal-x)**2 + (yreal-y)**2)
print("error : {}".format(error))

plt.figure()
plt.plot(dist_real, error, color='blue')
plt.scatter(dist_real, error, color='red')
plt.grid()
plt.xlabel("distance to opponent $[m]$")
plt.ylabel("error $[m]$")

plt.figure()
plt.scatter(x,y, label="position avec le LiDar")
plt.scatter(xreal, yreal, label="position réelle")
plt.scatter(xR, yR, label="robot", s=100, c='b')

plt.legend()
plt.xlim([0.0, 2.0])
plt.ylim([0.0, 3.0])
plt.gca().set_aspect(1)
plt.xlabel("$x[m]$")
plt.ylabel("$y[m]$")
plt.grid()
plt.show()