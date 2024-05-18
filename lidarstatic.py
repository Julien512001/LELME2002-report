import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def variance(x, mean):
    var = 0
    for i in range(len(x)):
        var += (x[i] - mean)**2
    var = var/len(x)
    return var

xreal = [0.35, 1.68, 1.0]
yreal = [0.2, 0.2, 2.81]
theta = [90.0, 90.0, 270.0]



rad = np.radians(theta)



xmes1 = [0.358, 0.36, 0.35, 0.358, 0.355]
ymes1 = [0.203, 0.2, 0.199, 0.203, 0.2]
thetames1 = [92.34, 92.25, 92.34, 92.37, 92.43]
radmes1 = np.radians(thetames1)

xmes2 = [1.687, 1.683, 1.684, 1.687, 1.679]
ymes2 = [0.204, 0.209, 0.206, 0.204, 0.21]
thetames2 = [90.98, 90.92, 90.97, 90.99, 91.04]
radmes2 = np.radians(thetames2)

xmes3 = [1.01, 1.01, 1.01, 1.01, 1.0]
ymes3 = [2.815, 2.82, 2.814, 2.814, 2.817]
thetames3 = [268.37, 268.44, 268.39, 268.41, 268.28]
radmes3 = np.radians(thetames3)

varx1 = variance(xmes1, xreal[0])
stdx1 = np.sqrt(varx1)
vary1 = variance(ymes1, yreal[0])
stdy1 = np.sqrt(vary1)
vartheta1 = variance(thetames1, theta[0])
stdtheta1 = np.sqrt(vartheta1)

varx2 = variance(xmes2, xreal[1])
stdx2 = np.sqrt(varx2)
vary2 = variance(ymes2, yreal[1])
stdy2 = np.sqrt(vary2)
vartheta2 = variance(thetames2, theta[1])
stdtheta2 = np.sqrt(vartheta2)

varx3 = variance(xmes3, xreal[2])
stdx3 = np.sqrt(varx3)
vary3 = variance(ymes3, yreal[2])
stdy3 = np.sqrt(vary3)
vartheta3 = variance(thetames3, theta[2])
stdtheta3 = np.sqrt(vartheta3)

print("stdx1 = {}".format(stdx1))
print("stdy1 = {}".format(stdy1))
print("stdtheta1 = {}".format(stdtheta1))

print("stdx2 = {}".format(stdx2))
print("stdy2 = {}".format(stdy2))
print("stdtheta2 = {}".format(stdtheta2))

print("stdx3 = {}".format(stdx3))
print("stdy3 = {}".format(stdy3))
print("stdtheta3 = {}\n".format(stdtheta3))
"""
stddist1 = np.sqrt(stdx1**2 + stdy1**2)
print(stddist1)
stddist2 = np.sqrt(stdx2**2 + stdy2**2)
print(stddist2)
stddist3 = np.sqrt(stdx3**2 + stdy3**2)
print(stddist3)
"""
couleurs = ['b', 'r', 'g']  # Couleurs sympas, vous pouvez les ajuster selon vos préférences

plt.figure()
for i in range(len(xreal)):
    plt.scatter(xreal[i],yreal[i], s=50, color=couleurs[i])
    plt.text(xreal[i] + 0.1, yreal[i], f"Position {i+1}", fontsize=12, ha='left', va='bottom')
    plt.quiver(xreal[i], yreal[i], np.cos(rad[i]), np.sin(rad[i]), angles='xy', scale_units='xy', scale=5, color='red', label='Orientation')
"""
for i in range(len(xmes1)):
    plt.scatter(xmes1[i],ymes1[i], s=10, color='black')
    #plt.quiver(xmes1[i], ymes1[i], np.cos(radmes1[i]), np.sin(radmes1[i]), angles='xy', scale_units='xy', scale=10, color='black', label='Orientation')
    plt.scatter(xmes2[i],ymes2[i], s=10, color='black')
    plt.quiver(xmes2[i], ymes2[i], np.cos(radmes2[i]), np.sin(radmes2[i]), angles='xy', scale_units='xy', scale=10, color='black', label='Orientation')
    plt.scatter(xmes3[i],ymes3[i], s=10, color='black')
    plt.quiver(xmes3[i], ymes3[i], np.cos(radmes3[i]), np.sin(radmes3[i]), angles='xy', scale_units='xy', scale=10, color='black', label='Orientation')
"""
#plt.xlim([0.34, 0.365])
#plt.ylim([0.19, 0.21])
plt.xlim([0.0, 2.0])
plt.ylim([0.0, 3.0])
plt.xlabel("$x [m]$")
plt.ylabel("$y [m]$")
plt.grid()
plt.gca().set_aspect(1)

"""
error_1x = np.mean(np.array(xmes1) - xreal[0])
error_1y = np.mean(np.array(ymes1) - yreal[0])
print("position 1 error {}, {}".format(error_1x, error_1y))

error_2x = np.mean(np.array(xmes2) - xreal[1])
error_2y = np.mean(np.array(ymes2) - yreal[1])
print("position 2 error {}, {}".format(error_2x, error_2y))

error_3x = np.mean(np.array(xmes3) - xreal[2])
error_3y = np.mean(np.array(ymes3) - yreal[2])
print("position 3 error {}, {}".format(error_3x, error_3y))q
"""

dist1 = np.sqrt((xreal[0] - np.array(xmes1))**2 + (yreal[0] - np.array(ymes1))**2)
error1 = np.mean(dist1)*1000

dist2 = np.sqrt((xreal[1] - np.array(xmes2))**2 + (yreal[1] - np.array(ymes2))**2)
error2 = np.mean(dist2)*1000

dist3 = np.sqrt((xreal[2] - np.array(xmes3))**2 + (yreal[2] - np.array(ymes3))**2)
error3 = np.mean(dist3)*1000

print("e_1 : {}, e_2 : {}, e_3 : {}".format(error1, error2, error3))

positions = ["Position 1", "Position 2", "Position 3"]

plt.figure()
plt.bar(positions, [error1, error2, error3], width=0.5, color=couleurs)
plt.xlabel('Positions')
plt.ylabel('distance error $[mm]$')

error_ang1 = np.mean(np.array(thetames1) - 90)
error_ang2 = np.mean(np.array(thetames2) - 90)
error_ang3 = np.mean(np.array(thetames3) - 270)

print("ang_1 : {}, ang_2 : {}, ang_3 : {}".format(error_ang1, error_ang2, error_ang3))

plt.figure()
plt.bar(positions, [error_ang1, error_ang2, error_ang3], width=0.5, color=couleurs)
plt.xlabel('Positions')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.ylabel('angle error $[^\circ]$')

plt.figure()
plt.quiver(np.zeros(len(radmes2)), np.zeros(len(radmes2)), np.cos(radmes2), np.sin(radmes2), angles='xy', scale_units='xy', scale=300, color='red', label='Orientation')



"""
std_x = [stdx1*1000, stdx2*1000, stdx3*1000]
std_y = [stdy1*1000, stdy2*1000, stdy3*1000]
std_dist = [stddist1*1000, stddist2*1000, stddist3*1000]
std_angle = [stdtheta1, stdtheta2, stdtheta3]

plt.figure()
plt.bar(positions, std_dist, width=0.5, color=couleurs)
plt.xlabel('Positions')
plt.ylabel('STD $[mm]$')

plt.figure()
plt.bar(positions, std_x, width=0.5, color=couleurs)
plt.xlabel('Positions')
plt.ylabel('STD_x $[mm]$')

plt.figure()
plt.bar(positions, std_y, width=0.5, color=couleurs)
plt.xlabel('Positions')
plt.ylabel('STD_y $[mm]$')

plt.figure()
plt.bar(positions, std_angle, width=0.5, color=couleurs)
plt.xlabel('Positions')
plt.ylabel('STD $[^\circ]$')
"""


# Affichage du graphique
plt.show()
