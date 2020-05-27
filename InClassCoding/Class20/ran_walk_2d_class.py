import matplotlib.pyplot as plt
import numpy as np
import random
import math

random.seed()
ntrials = 10
nwalks = 10
nsteps = 1000
d = np.array([])
d2 = np.array([])

ichoose = 0

if ichoose == 0:
   fig, ax = plt.subplots()
else:
   fig, ax = plt.subplots(1,2)

for iwalk in range(nwalks):

   xpos = 0
   ypos = 0
   rpos = 0
   nstep = np.array([])
   xarr = np.array([])
   yarr = np.array([])
   nstep = np.append(nstep,0)
   xarr = np.append(xarr,xpos)
   yarr = np.append(yarr,ypos)

   count = 1 
   xpos = 0
   ypos = 0
   d2pos = 0
 
   for step in range(nsteps):

#     generate an xpoint and ypoint between -1 and 1
      xpoint=2*random.random()-1
      ypoint=2*random.random()-1

#     normalize these so the length of the step is 1
      xnorm = xpoint/ np.sqrt(xpoint**2+ypoint**2)
      ynorm = ypoint/ np.sqrt(xpoint**2+ypoint**2)

#     add xnorm to xpos, ynorm to ypos
      xpos +=xnorm
      ypos +=ynorm

      count += 1
      xarr = np.append(xarr,xpos) #append xpos to the xarr array
      yarr = np.append(yarr,ypos) #append ypos to the yarr array
      nstep = np.append(nstep,count) #append count to the nstep array
   if ichoose == 0:
      ax.plot(xarr,yarr,'r')

   d = np.append(d,xpos)
   d2 = np.append(d2,(xpos**2+ypos**2))
   
    
if ichoose == 0:
   ax.set(title='title', xlabel='steps', ylabel='distance')
   ax.set_xlim(-50.,50.)
   ax.set_ylim(-50.,50.)
   ax.grid()
   plt.show()
elif ichoose == 1:
   ax[0].hist(d, bins=50, range=(-50.,50.), histtype='step')      
   ax[0].set(title='title', xlabel='xpos', ylabel='number')               
   ax[0].grid()

   print (np.mean(d2))
   ax[1].hist(d2, bins=50, range=(0.,1000.), histtype='step')
   ax[1].set(title='title', xlabel='displacement**2', ylabel='number')
   ax[1].grid()

   plt.show()
