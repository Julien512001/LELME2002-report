import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('lid_opppos2.txt', delimiter=',')

x = df.iloc[:, 0].values.astype(float)
y = df.iloc[:, 1].values.astype(float)

plt.scatter(x,y)

plt.xlim([0.0, 2.0])
plt.ylim([0.0, 3.0])
plt.gca().set_aspect(1)
plt.show()