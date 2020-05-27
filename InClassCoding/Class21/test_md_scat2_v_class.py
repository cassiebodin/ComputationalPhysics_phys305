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

length = 10
nballs = 100
# init
vmax = 1
for i in range(nballs):
      x = np.append(x,random.random()*10.)
      y = np.append(y,random.random()*10.)
      #vx = np.append(vx,vmax*(2*random.random() - 1))
      #vy = np.append(vy,vmax*(2*random.random() - 1))
      theta = 2*np.pi*random.random()
      vx = np.append(vx,vmax*math.cos(theta))
      vy = np.append(vy,vmax*math.sin(theta))
      v = np.sqrt(vx**2 + vy**2)
      v2 = vx**2 + vy**2


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

print (xarr.shape)

t = 0
time = 200
count = 0
h = 0.1
eps2 = 0.1
steps = time/h + 1
print (steps)


while (t < time):
      
      for i in range(nballs):
            x[i] = x[i] + vx[i]*h
            y[i] = y[i] + vy[i]*h
            if x[i] < 0:
               x[i] = 0.
               vx[i] = -vx[i]
            if x[i] > length:
               x[i] = length
               vx[i] = -vx[i]
            if y[i] < 0:
               y[i] = 0.
               vy[i] = -vy[i]
            if y[i] > length:
               y[i] = length
               vy[i] = -vy[i]

      for i in range(nballs-1):
            for j in range (i+1,nballs):
                if ((x[i] - x[j])**2 + (y[i]-y[j])**2) < eps2:
                    # scatter
                    vx_cm = 0.5*(vx[i] + vx[j])
                    vy_cm = 0.5*(vy[i] + vy[j])
                    u1x = vx[i] - vx_cm
                    u1y = vy[i] - vy_cm
                    umag = math.sqrt(u1x**2 + u1y**2)
                    theta = 2*np.pi*random.random()
                    vx[i] = math.cos(theta)* umag + vx_cm
                    vx[j] = -math.cos(theta)* umag + vx_cm
                    vy[i] = math.sin(theta)* umag + vy_cm
                    vy[j] = -math.sin(theta)* umag + vy_cm

# calculate v[i], v[j], v2[i], v2[j]
# then play with the code to convince yourself you are seeing the
# maxwell-boltzmann speed distribution
                    v[i] = np.sqrt(vx[i]**2+vy[i]**2)
                    v[j] = np.sqrt(vx[j]**2+vy[j]**2)
                    v2[i] = vx[i]**2+vy[i]**2
                    v2[j] =vx[j]**2+vy[j]**2


      xarr = np.append(xarr,[x], axis=0)
      yarr = np.append(yarr,[y], axis=0)
      vxarr = np.append(vxarr,[vx], axis=0)
      vyarr = np.append(vyarr,[vy], axis=0)
      varr = np.append(varr,[v], axis=0)
      v2arr = np.append(v2arr,[v2], axis=0)

      count += 1  
      t = t+h

print (count)
print (xarr.shape)

test = []
ichoose = 1
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
            ax.set_xlim(0., 10.)
            ax.set_ylim(0., 10.)
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
      ax[0].hist(vxarr[2000,:], bins=50, range=(-10,10), histtype='step', color='b')
      ax[0].set(title='title', xlabel='vx', ylabel='number')               
      ax[0].grid()

      print(np.mean(varr[2000,:]))
      print(np.mean(varr[2000,:])/1.128)
      #ax[1].hist(varr[0,:], bins=50,range=(0,25),  histtype='step', color='r')
      ax[1].hist(varr[2000,:], bins=50,range=(0,5),  histtype='step', color='b')
      ax[1].set(title='title', xlabel='speed', ylabel='number')
      ax[1].grid()

      plt.show()
