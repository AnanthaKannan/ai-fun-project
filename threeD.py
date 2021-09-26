# Import libraries
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
# https://www.geeksforgeeks.org/3d-scatter-plotting-in-python-using-matplotlib/
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


# Creating figure
fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")
# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
print(zdata)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

# show plot
plt.show()