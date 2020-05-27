import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits import mplot3d

# Constants
m = 10         # number of points
Vtop = 1.0      # boundary conditions
Vbot = 0.0
Vleft = 0.0
Vright = 0.0
target = 1e-6   # Target accuracy

# Create arrays to hold potential values
phi = np.zeros([m+1,m+1],float)
phi[m,:] = Vtop
phi[0,:] = Vbot
phi[:,m] = Vright
phi[:,0] = Vleft
phiprime = np.zeros([m+1,m+1],float)
zdata = np.zeros([m+1,m+1],float)
print(phi.shape)
print (type(phi))
print (type(phiprime))

# Main loop
deltaV = 1.0
while deltaV>target:
    deltaV = 0.
    # Calculate new values phiprime of the potential
    # in terms of the old values phi

    for i in range(m+1):
        for j in range(m+1):
#boundary conditions
            phiprime[m,:] = Vtop
            phiprime[0,:] = Vbot
            phiprime[:,m] = Vright
            phiprime[:,0] = Vleft
    # calculate new values phiprime of the potential                               # in terms of the old values phi 
            if (i==m or i==0 or j==m or j==0):
                continue
            phiprime[i,j]= (1/4)*(phi[i+1,j]+phi[i-1,j]+phi[i,j+1]+phi[i,j-1])
    # calculate some difference to use for convergence
            deltaV += abs(phiprime[i,j]- phi[i,j])

    #print(deltaV)
    phi, phiprime = phiprime, phi

zdata = phiprime

np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
for i in range(m,-1,-1):
   print (zdata[i,:])

fig, ax = plt.subplots(1,2)
pcm = ax[0].pcolormesh(zdata, cmap='jet')
fig.colorbar(pcm, ax=ax[0])
ax[0].set_title('pcolormesh')
ax[0].set_xlabel('x axis')
ax[0].set_ylabel('y axis')

levels = 15
cf = ax[1].contourf(zdata, levels=levels,cmap='jet') 
fig.colorbar(pcm, ax=ax[1])
ax[1].set_title('contourf with levels')
ax[1].set_xlabel('x axis')
ax[1].set_ylabel('y axis')

fig.tight_layout()
plt.show()
