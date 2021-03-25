import numpy as np
import matplotlib.pyplot as plt

data1 = np.genfromtxt("ERDA 3c - Sheet1.csv", delimiter=",")
data2 = np.genfromtxt("cities south holland.csv", delimiter=",")

plt.scatter(data1[:,1], data1[:,2], label="Parks")
plt.scatter(data2[:,1], data2[:,2], label="Cities")

plt.scatter([52.0186, 52.1763], [4.3782, 4.5282], label="Delft, Leiden")

plt.legend()
plt.show()