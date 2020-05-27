import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


random.seed()

kT = 0
T = 0
H = 0
N = 20
J = 1
ntrials = 1000
spins = np.random.random((N,N))
shape = (N,N)
spins = np.random.choice([-1, 1], size=shape)
#spins = np.ones((N,N))
print (spins)
#spins = np.zeros((N,N), int)
#spins = np.ones((N,N), int)
zarr1 = np.zeros((N,N,3), int)
zarr2 = np.zeros((N,N,3), int)
zarr3 = np.zeros((N,N,3), int)
zarr4 = np.zeros((N,N,3), int)
 
spindx = np.zeros((2,2), int)


for itrial in range(ntrials):

      etotal = 0
      mtotal = 0
      i = random.randint(0,N-1)
      j = random.randint(0,N-1)
#      for i in range(N):
#            for j in range(N):
                  # handle the boundary conditions   
      if (i > 0 and i < N-1 and j > 0 and j < N-1):
            spindx [0,0] = i-1
            spindx [1,0] = i+1
            spindx [0,1] = j-1
            spindx [1,1] = j+1
      elif (i == 0 and j == 0):
            spindx [0,0] = N-1
            spindx [1,0] = i+1
            spindx [0,1] = N-1
            spindx [1,1] = j+1
      elif (i == 0 and j == N-1):
            spindx [0,0] = N-1
            spindx [1,0] = i+1
            spindx [0,1] = j-1
            spindx [1,1] = 0
      elif (i == N-1 and j == 0):
            spindx [0,0] = i-1
            spindx [1,0] = 0
            spindx [0,1] = N-1
            spindx [1,1] = j+1
      elif (i == N-1 and j == N-1):
            spindx [0,0] = i-1
            spindx [1,0] = 0
            spindx [0,1] = j-1
            spindx [1,1] = 0
      elif (i == 0 and (j > 0 and j < N-1)):
            spindx [0,0] = N-1
            spindx [1,0] = i+1
            spindx [0,1] = j-1
            spindx [1,1] = j+1
      elif (i == N-1 and (j > 0 and j < N-1)):
            spindx [0,0] = i-1
            spindx [1,0] = 0
            spindx [0,1] = j-1
            spindx [1,1] = j+1
      elif (j == 0 and (i > 0 and i < N-1)):
            spindx [0,0] = i-1
            spindx [1,0] = i+1
            spindx [0,1] = N-1
            spindx [1,1] = j+1
      elif (j == N-1 and (i > 0 and i < N-1)):
            spindx [0,0] = i-1
            spindx [1,0] = i+1
            spindx [0,1] = j-1
            spindx [1,1] = 0
      else:
            continue

#
#     add the metropolis algorithm for the ising model here
#     the steps are given in the lecture notes
#
      print(spins[i,j])

      ebefore=-J*spins[i,j]*(spins[i,spindx[1,1]]+spins[i,spindx[0,1]]+spins[spindx[1,0],j]+spins[spindx[0,0],j])
      eafter= -J*(-spins[i,j])*(spins[i,spindx[1,1]]+spins[i,spindx[0,1]]+spins[spindx[1,0],j]+spins[spindx[0,0],j])

      if eafter<ebefore:
            spins[i,j]=-spins[i,j]
      elif eafter>ebefore:
            spins[i,j]=spins[i,j]
            r=random.random()
            if r <= np.exp(-(eafter-ebefore)/(kT)):
                  spins[i,j]=-spins[i,j]
            elif r > np.exp(-(eafter-ebefore)/(kT)):
                  continue
      
      print(ebefore)
      print(eafter)
      print(spins[i,j])

      if (itrial == 0):
        print (itrial)
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

