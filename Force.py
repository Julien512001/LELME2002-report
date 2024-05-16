import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('force.txt', delimiter=',')
df1 = pd.read_csv('Force_obs.txt', delimiter=',')


x = df.iloc[:, 0].values.astype(float)
y = df.iloc[:, 1].values.astype(float)
t = df.iloc[:, 2].values.astype(float)
Fx = df.iloc[:,3].values.astype(float)
Fy = df.iloc[:, 4].values.astype(float)

x1 = df1.iloc[:, 0].values.astype(float)
y1 = df1.iloc[:, 1].values.astype(float)
t1 = df1.iloc[:, 2].values.astype(float)
Fx1 = df1.iloc[:,3].values.astype(float)
Fy1 = df1.iloc[:, 4].values.astype(float)

F1 = np.sqrt(Fx1*Fx1 + Fy1*Fy1)

dist_depart = np.sqrt(x1[0]**2 + y[0]**2)

dist_array = np.sqrt(x1*x1 + y1*y1) - dist_depart

plt.figure()
plt.plot(y, Fy, label='Force')
plt.axvline(x=1.7, color='red', linestyle='dashed', label='$\sigma_0$')
plt.xlabel("$y [m]$")
plt.ylabel("Force")
plt.grid()
plt.legend()

plt.figure()
plt.plot(t1, F1, label='Force')
plt.xlabel("$t [s]$")
plt.ylabel("Force")
plt.grid()
plt.legend()

plt.figure()
plt.scatter(x1,y1, color="yellow")
circle = plt.Circle((1.5, 1.5), radius=0.2, color='red', fill=True)
plt.gca().add_artist(circle)
plt.text(1.5 + 0.125, 1.5, 'opponent', verticalalignment='center')
plt.xlim([0.0, 2.0])
plt.ylim([0.0, 3.0])
plt.gca().set_aspect(1)
plt.xlabel("$x[m]$")
plt.ylabel("$y[m]$")
plt.grid()



plt.show()