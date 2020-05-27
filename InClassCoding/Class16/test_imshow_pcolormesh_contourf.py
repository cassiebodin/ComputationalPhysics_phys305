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

fig, ax = plt.subplots(2,2)
im = ax[0,0].imshow(zdata, cmap='jet') 
fig.colorbar(im, ax=ax[0,0])
ax[0,0].set_title('imshow')
ax[0,0].set_xlabel('x axis')
ax[0,0].set_ylabel('y axis')

pcm = ax[0,1].pcolormesh(zdata, cmap='jet')
fig.colorbar(pcm, ax=ax[0,1])
ax[0,1].set_title('pcolormesh')
ax[0,1].set_xlabel('x axis')
ax[0,1].set_ylabel('y axis')

pc = ax[1,0].pcolor(zdata, cmap='jet')
fig.colorbar(pc, ax=ax[1,0])
ax[1,0].set_title('pcolor')
ax[1,0].set_xlabel('x axis')
ax[1,0].set_ylabel('y axis')

levels = 15
cf = ax[1,1].contourf(zdata, levels=levels,cmap='jet') 
fig.colorbar(pcm, ax=ax[1,1])
ax[1,1].set_title('contourf with levels')
ax[1,1].set_xlabel('x axis')
ax[1,1].set_ylabel('y axis')

fig.tight_layout()
plt.show()


