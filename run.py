import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("ERDA 3c - Sheet1.csv", delimiter=",")

plt.scatter(data[:,1], data[:,2])
plt.show()