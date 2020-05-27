import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


random.seed()
x = np.array([])
y = np.array([])
vx = np.array([])
vy = np.array([])
v = np.array([])
ncol = np.array([])
dvx = np.array([])
vxarrall = np.array([])
varrall = np.array([])
length = 5


nballs = 25
# init the balls
vmax = 0.0
for i in range(nballs):
      xoff = int(i/5) + 0.5
      yoff = i%5 + 0.5
      x = np.append(x, (random.random()*0.005 + xoff))
      y = np.append(y, (random.random()*0.005 + yoff))
      #print (xoff, yoff)

      ncol = np.append(ncol,0)
      #vx = np.append(vx,vmax*(2*random.random() - 1))
      #vy = np.append(vy,vmax*(2*random.random() - 1))
      theta = 2*np.pi*random.random()
      vx = np.append(vx,vmax*math.cos(theta))
      vy = np.append(vy,vmax*math.sin(theta))
      v = np.sqrt(vx**2 + vy**2)
      v2 = vx**2 + vy**2
      dvx = np.append(dvx,0)

# note mass = 1, so fx is really ax = fx/m
fxarr = np.zeros((nballs,2))
fyarr = np.zeros((nballs,2))

print (x.size)
print (v.size)
print (v)
print (v2)

xarr = np.zeros((1,nballs),float)
xarr = np.append(xarr,[x],axis=0)
xarr = np.delete(xarr,0,0)
yarr = np.zeros((1,nballs),float)
yarr = np.append(yarr,[y],axis=0)
yarr = np.delete(yarr,0,0)
vxarr = np.zeros((1,nballs),float)
vxarr = np.append(vxarr,[vx],axis=0)
vxarr = np.delete(vxarr,0,0)
vyarr = np.zeros((1,nballs),float)
vyarr = np.append(vyarr,[vy],axis=0)
vyarr = np.delete(vyarr,0,0)
varr = np.zeros((1,nballs),float)
varr = np.append(varr,[v],axis=0)
varr = np.delete(varr,0,0)
v2arr = np.zeros((1,nballs),float)
v2arr = np.append(v2arr,[v2],axis=0)
v2arr = np.delete(v2arr,0,0)
dvxarr = np.zeros((1,nballs),float)
dvxarr = np.append(dvxarr,[dvx],axis=0)
dvxarr = np.delete(dvxarr,0,0)
dvxarr = np.zeros((1,nballs),float)
dvxarr = np.append(dvxarr,[dvx],axis=0)
dvxarr = np.delete(dvxarr,0,0)
tarr = np.zeros(1)

print (tarr.shape)
print (xarr.shape)
print (varr.shape)

t = 0
time = 50
count = 0
h = 0.01
steps = time/h + 1
print ('steps = ',steps)
r2cut = 9.


while (t < time):

      fxarr = np.zeros((nballs,2),float)
      fyarr = np.zeros((nballs,2),float)
      ax = np.zeros((nballs),float)#********************
      ay = np.zeros((nballs),float)#*********************
      ax1 = np.zeros((nballs),float)#********************
      ay1 = np.zeros((nballs),float)#*********************

      print(fxarr.shape,fyarr.shape)

      # loop over pairs of balls
      for i in range(nballs-1):
            for j in range(i+1,nballs):
              #if (i == j): exit()
              dx = x[i] - x[j]
              dy = y[i] - y[j]
              # need this snippet because the walls are not reflecting
              if (abs(dx) > length/2):
                    if dx >= 0.:
                          dx = dx - length
                    else:
                          dx = dx + length
              #print ('dx ',dx,x[i],x[j])
              if (abs(dy) > length/2):
                     if dy >= 0.:
                           dy = dy - length
                     else:
                           dy = dy + length

              r2 = dx**2 + dy**2
              r = math.sqrt(r2)
              # include these in the force calculation
              if (r2 < r2cut):
                    if (r == 0.):  r = 1e-6
# calculate the force in the x and y directions
                    fijx = 24 * ( (2./r**13) - (1/r**7) ) * (dx/r)
                    fijy = 24 * ( (2./r**13) - (1/r**7) ) * (dy/r)
# add these forces to fxarr[i,0], fyarr[i,0], fxarr[j,0], fyarr[j,0]
                    fxarr[i,0]+=fijx
                    fyarr[i,0]+=fijy
                    fxarr[j,0]+=-fijx
                    fyarr[j,0]+=-fijy

      #print(fxarr.shape,fyarr.shape)

     # print(fxarr[:,0])

# after all the forces are summed, update the position using the
# velocity verlet method ********************************************************************************************
      for i in range(nballs-1):
            for j in range(i+1,nballs):
                    print()
                    ax[i]= fxarr[i,0]
                    ax[j]= fxarr[j,0]
                    ay[i]= fyarr[i,0]
                    ay[j]= fyarr[j,0]

                    x[i]+=vx[i]*h +(.5)*ax[i]*h**2
                    x[j]+=vx[j]*h +(.5)*ax[j]*h**2
                    y[i]+=vy[i]*h +(.5)*ay[i]*h**2
                    y[j]+=vy[j]*h +(.5)*ay[j]*h**2

                    ax1[i]+= fxarr[i,0]
                    ax1[i]+= fxarr[i,0]
                    ay1[j]+= fyarr[j,0]
                    ay1[j]+= fyarr[j,0]

                    vx[i]+=(h/2)*(ax1[i]+ax[i])
                    vx[j]+=(h/2)*(ax1[j]+ax[j])
                    vy[i]+=(h/2)*(ay1[i]+ay[i])
                    vy[j]+=(h/2)*(ay1[j]+ay[j])

#*******************************************************************************************************************
# after the positions are updated, apply the periodic boundary conditions
                    if x[i] or x[j] < 0:
                          vx[i] = vx[i]
                          x[i] = length
                          x[j] = length

                    if x[i] or x[j] > length:
                          vx[i] = vx[i]
                          x[i] = 0.
                          x[j] = 0.

                    if y[i] or y[j] < 0:
                          vy[i] = vy[i]
                          y[i] = length
                          y[j] = length

                    if y[i] or y[j] > length:
                          vy[i] = vy[i]
                          y[i] = 0.
                          y[j] = 0.
# note i have included the code already to update the velocities
# you do not have to do that
      print(x)
      # now update velocities
      # note the positions have already been updated
      # so we have to go through it again to find the newer (i+1) values of f, then v

      for i in range(nballs-1):
            for j in range(i+1,nballs):
              dx = x[i] - x[j]
              dy = y[i] - y[j]
              # need this because the walls are not reflecting                                                                                       
              if (abs(dx) > length/2):
                    if dx >= 0.:
                          dx = dx - length
                    else:
                          dx = dx + length
              if (abs(dy) > length/2):
                     if dy >= 0.:
                           dy = dy - length
                     else:
                           dy = dy + length
              r2 = dx**2 + dy**2
              r = math.sqrt(r2)
              if (r2 < r2cut):
              # include or not in the force calculation                                                                                              
                    if (r == 0.):  r = 1e-6
                    fijx = 24 * ( (2./r**13) - (1/r**7) ) * (dx/r)
                    fijy = 24 * ( (2./r**13) - (1/r**7) ) * (dy/r)
                    # index 1 means newer, index 0 means older
                    fxarr[i,1] = fxarr[i,1] + fijx
                    fyarr[i,1] = fyarr[i,1] + fijy
                    fxarr[j,1] = fxarr[j,1] - fijx
                    fyarr[j,1] = fyarr[j,1] - fijy

      # forces are updated                                                           # now update the velocity                                      
      # now update the velocities                          
      for i in range(nballs):
            vx[i] = vx[i] + (h/2)*(fxarr[i,1] + fxarr[i,0])
            vy[i] = vy[i] + (h/2)*(fyarr[i,1] + fyarr[i,0])
            if vx[i]>10:
                  print (i,vx[i],vy[i],fxarr[i,1],fyarr[i,1])


      xarr = np.append(xarr,[x], axis=0)
      yarr = np.append(yarr,[y], axis=0)
      vxarr = np.append(vxarr,[vx], axis=0)
      vyarr = np.append(vyarr,[vy], axis=0)
      varr = np.append(varr,[v], axis=0)
      v2arr = np.append(v2arr,[v2], axis=0)
      dvxarr = np.append(dvxarr,[dvx],axis=0)
      if (t > 5 and count%10 == 0):
          vxarrall = np.append(vxarrall,vx)
          varrall = np.append(varrall,v)

      count += 1  
      t = t+h
      tarr = np.append(tarr,t)

print (count)
print (xarr.shape)
print (tarr.shape)
print (ncol)
# mean ke = kt
kt = np.mean(v2arr[int(steps)-10,:])/2.
print ('kt = ',kt)
vol = 100
print ('vol = ',vol)
area = 10
print ('area = ',area)
dvxsum = 0
timetotal = 0
for i in range(200):
        dvxsum = dvxsum + np.sum(dvxarr[int(steps/2)+i,:])
        #print (dvxarr[int(steps/2)+i,1:20])
        #print (xarr[int(steps/2)+i,1:20])
        timetotal = timetotal+h
print (dvxsum, timetotal)
pressure = dvxsum/timetotal/area
print ('pressure = ',pressure)
print ('pv =',pressure*vol)
print ('nt = ',nballs*kt)


test = []
ichoose = 0
if ichoose == 0:

      fig, ax = plt.subplots()
      xdata = np.zeros(nballs)
      ydata = np.zeros(nballs)
      for i in range(nballs):
            lntest = ax.plot([], [], 'ro', animated=True)[0]
            test.append(lntest)

#ln0, = plt.plot([], [], 'ro', animated=True)
#ln1, = plt.plot([], [], 'bo', animated=True)
#ln2, = plt.plot([], [], 'go', animated=True)
#ln3, = plt.plot([], [], 'co', animated=True)
#ln4, = plt.plot([], [], 'mo', animated=True)
#print (type(ln0))
      print (test)

      def init():
            ax.set_xlim(0., length)
            ax.set_ylim(0., length)
            for line in test:
                  line.set_data([],[])
            return test

      def update(frame):
    #print (type(frame))
            for i in range(nballs):
                  xdata[i] = xarr[frame,i]
                  ydata[i] = yarr[frame,i]
#    ln0.set_data(xdata[0], ydata[0])
#    ln1.set_data(xdata[1], ydata[1])
#    ln2.set_data(xdata[2], ydata[2])
#    ln3.set_data(xdata[3], ydata[3])
#    ln4.set_data(xdata[4], ydata[4])
#    return ln0, ln1, ln2, ln3, ln4
                  nlines = 0
                  for line in test:
                        line.set_data(xdata[nlines], ydata[nlines])
                        nlines += 1
            return test

      ani = FuncAnimation(fig, update, frames=xarr.size, interval=50, init_func=init, blit=True)
      plt.show()

else:
      fig, ax = plt.subplots(1,2)
      ax[0].hist(vxarr[0,:], bins=50, range=(-10,10), histtype='step', color='r')      
      ax[0].hist(vxarr[int(steps)-10,:], bins=50, range=(-10,10), histtype='step', color='b')
      ax[0].set(title='title', xlabel='vx', ylabel='number')               
      ax[0].grid()

      print(np.mean(varr[int(steps)-10,:]))
      print(np.mean(varr[int(steps)-10,:])/1.128)
      #ax[1].hist(varr[0,:], bins=50,range=(0,25),  histtype='step', color='r')
      #ax[1].hist(varr[int(steps)-10,:], bins=50,range=(0,5),  histtype='step', color='b')
      ax[1].hist(varrall, bins=50,range=(0,5),  histtype='step', color='b') 
      ax[1].set(title='title', xlabel='speed', ylabel='number')
      ax[1].grid()

      plt.show()
