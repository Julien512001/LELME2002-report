import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df2 = pd.read_csv('odo_crapaud.txt', delimiter=',')

xRend = 1.73
yRend = 0.2

def plot(df):
    plt.figure()
    # Extraction des valeurs des deux colonnes dans des tableaux NumPy
    x = df.iloc[::50, 0].values.astype(float)
    y = df.iloc[::50, 1].values.astype(float)
    theta = df.iloc[::50, 2].values.astype(float)

    error_x = x[-1] - xRend
    error_y = y[-1] - yRend
    ratio_x = xRend/x[-1] *100
    ratio_y = yRend/y[-1] *100


    print("e_x : {}, e_y : {}, ratio : {}".format(error_x,  error_y, ratio_x, ratio_y))
    rad = np.radians(theta)

    plt.scatter(x,y, color='yellow', label='odométrie')

    #plt.quiver(x, y, np.cos(rad), np.sin(rad), angles='xy', scale_units='xy', scale=1000, color='red')
        
    # Ajouter une légende


    plt.gca().set_aspect(1)

plot(df2)
x1, y1 = 0.35, 0.2
x2, y2 = 1.73, 0.2
plt.plot([x1, x2], [y1, y2], color='blue', label='trajectoire réelle')
plt.scatter([x1, x2], [y1, y2], color='red')
plt.xlabel("$x[m]$")
plt.ylabel("$y[m]$")
plt.legend()
plt.xlim([0.0, 2.30])
plt.ylim([0.0, 1.0])

plt.show()