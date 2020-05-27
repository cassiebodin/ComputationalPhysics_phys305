import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits import mplot3d

# Constants
m = 10         # number of grid points on a side 
zdata = np.zeros([m,m],float)
#zdata = np.random.rand(10,10)
print(type(zdata))

for i in range(m):
    for j in range(m):
        zdata[i,j] = float(i*j)

fig, ax = plt.subplots()
x = np.arange(0,10)
y = np.arange(0,10)
xdata, ydata = np.meshgrid(x,y)
ax = plt.axes(projection='3d')
surf = ax.plot_surface(xdata, ydata, zdata, rstride=1, cstride=1,
                cmap='jet', edgecolor='none')
fig.colorbar(surf, ax=ax)
ax.set_title('surface')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()
