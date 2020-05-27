import matplotlib.pyplot as plt
import numpy as np
import random


random.seed()
ntrials = 1000
nwalks = 1000
nsteps = 500
d = np.array([])
d2 = np.array([])

ichoose = 4
if ichoose == 0:
   fig, ax = plt.subplots()
else: 
   fig, ax = plt.subplots(1,2)


for iwalk in range(nwalks):
   xpos = 0
   xpos2 = 0
   nstep = np.array([])
   xarr = np.array([])
   nstep = np.append(nstep,0)
   xarr = np.append(xarr,xpos)
   count = 1 
   for step in range(nsteps):
      r=random.random() #generate a random number
      if (r<0.5): #if r<0.5 then move left
         xpos+=-1
      elif (r>=0.5):#if r>0.5 then move right
         xpos+=1
#
      xpos2 += 1
      xarr = np.append(xarr,xpos)
      nstep = np.append(nstep,count)
      count += 1
   if ichoose == 0:
      ax.plot(nstep,xarr,'r')

   d = np.append(d,xpos)
   d2 = np.append(d2,xpos*xpos)

if ichoose == 0:

   ax.set(title='title', xlabel='steps', ylabel='distance')
   ax.set_ylim(-50,50)
   ax.grid()
   plt.show()

else:

   ax[0].hist(d, bins=50, range=(-50,50), histtype='step')      
   ax[0].set(title='title', xlabel='displacement', ylabel='number')               
   ax[0].grid()

   print (np.mean(d2))
   ax[1].hist(d2, bins=50,range=(0,2000),  histtype='step')
   ax[1].set(title='title', xlabel='displacement**2', ylabel='number')
   ax[1].grid()

   plt.show()
