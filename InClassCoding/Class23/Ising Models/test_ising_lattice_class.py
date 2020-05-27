import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

random.seed()

kT = 0.1
T = 0
H = 0
N = 20
J = 1
ntrials = 100

# create an (N,N) numpy array called spins
# in each element put a 1 or -1   
# don't do this by hand (ie spins[0,0]=-1, ...)
# play also putting all spin up or all spin down at the lattice sites
spins = np.random.random((N,N))
shape = (N,N)
spins = np.random.choice([-1, 1], size=shape)

zarr1 = np.zeros((N,N,3), int)
zarr2 = np.zeros((N,N,3), int)
zarr3 = np.zeros((N,N,3), int)
zarr4 = np.zeros((N,N,3), int)
 

for itrial in range(ntrials):

      if (itrial == 0):
        # where we set the RGB for each pixel
        # spin up is red, spin down is blue
        zarr1[spins>0] = [255,0,0]
        zarr1[spins<0] = [0,0,255]
        #print (zarr1)
      if (itrial == int(ntrials*0.333)):
        print (itrial)
        zarr2[spins>0] = [255,0,0]
        zarr2[spins<0] = [0,0,255]
      if (itrial == int(ntrials*0.666)):
        print (itrial)
        zarr3[spins>0] = [255,0,0]
        zarr3[spins<0] = [0,0,255]
      if (itrial == (ntrials-10)):
        print (itrial)
        zarr4[spins>0] = [255,0,0]
        zarr4[spins<0] = [0,0,255]

ichoose = 0
if ichoose == 0:

      fig, ax = plt.subplots(2,2)
      #print (zarr1)
      ax[0,0].imshow(zarr1,interpolation='none')
      ax[0,0].set_title('imshow')
      ax[0,0].set_xlabel('x axis')
      ax[0,0].set_ylabel('y axis')

      ax[0,1].imshow(zarr2,interpolation='none')
      #print (zarr2)
      ax[0,1].set_title('imshow')
      ax[0,1].set_xlabel('x axis')
      ax[0,1].set_ylabel('y axis')

      ax[1,0].imshow(zarr3,interpolation='none')
      print (zarr3)
      ax[1,0].set_title('imshow')
      ax[1,0].set_xlabel('x axis')
      ax[1,0].set_ylabel('y axis')

      ax[1,1].imshow(zarr4,interpolation='none')
      #print (zarr4)
      ax[1,1].set_title('imshow')
      ax[1,1].set_xlabel('x axis')
      ax[1,1].set_ylabel('y axis')

      plt.tight_layout()
      plt.show()

