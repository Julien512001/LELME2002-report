import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df1 = pd.read_csv('odo_robpos1.txt', delimiter=',')
df2 = pd.read_csv('odo_robpos2.txt', delimiter=',')
df3 = pd.read_csv('odo_robpos3.txt', delimiter=',')

yRend = 2.0

def plot(df):
    plt.figure()
    # Extraction des valeurs des deux colonnes dans des tableaux NumPy
    x = df.iloc[:, 0].values.astype(float)
    y = df.iloc[:, 1].values.astype(float)
    theta = df.iloc[:, 2].values.astype(float)

    error = y[-1] - yRend
    print(error)
    rad = np.radians(theta)
    plt.scatter(x,y, color='yellow', label='odométrie')
    x1, y1 = 0.35, 0.2
    x2, y2 = 0.35, 2.0
    plt.plot([x1, x2], [y1, y2], color='blue', label='trajectoire réelle')
    plt.scatter([x1, x2], [y1, y2], color='red')
    plt.legend()

    plt.xlabel("$x[m]$")
    plt.ylabel("$y[m]$")

    plt.xlim([0.3, 0.4])
    plt.ylim([0.0, 3.0])
    plt.gca().set_aspect(1/10)

plot(df1)
plot(df2)
plot(df3)

plt.figure()
plt.bar([1, 2, 3], [-9.3, -6.8, 16.0], width=0.1, color='red')
plt.xlabel("distance to opponent $[m]$")
plt.ylabel("error $[m]$")

plt.show()