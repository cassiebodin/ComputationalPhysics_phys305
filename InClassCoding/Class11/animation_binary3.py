import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#xarr = np.array([-.4, -.3, -.2, -.1, 0, .1, .2, .3, .4, .5])
#yarr = np.array([-.4, -.3, -.2, -.1, 0, .1, .2, .3, .4, .5])

sec = 3.154e7
au = 1.496e11
# normally G in m**3 / kg / s**
# in units au**3 / year**2
G = 6.674e-11*sec*sec/au/au/au
#G = 6.674e-11
GMs = 4.*((math.pi)**2)
m_sun = 1.989e30
m1 = m_sun
m2 = 2*m_sun
mcm = m1+m2


a = 1
a1 = m2 * a / (m1+m2) 
a2 = m1 * a / (m1+m2)
mu = m1*m2/(m1+m2)
print (a, a1, a2, mu)

e = 0.0
e1 = e
e2 = e
per1 = a1*(1 - e1)
per2 = a2*(1 - e2)
print (per1, per2)

#vmu = math.sqrt( G * (m1 + m2) * (1+e) / (a * (1-e)))
#vp1 = (m2/mu)*vmu
#vp2 = (m2/mu)*vmu
#print (vmu, vp1, vp2)

vp1 = math.sqrt(G * (m1+m2) * (1+e) / (a1 * (1-e)))
vp2 = math.sqrt(G * (m1+m2) * (1+e) / (a2 * (1-e)))

x1 = -per1
y1 = 0
x2 = per2
y2 = 0
r1 = math.sqrt(x1**2 + y1**2)
r2 = math.sqrt(x2**2 + y2**2)

vx1 = 0
vy1 = -vp1
vx2 = 0
vy2 = vp2

xcm = (m1*x1 + m2*x2)/mcm
x1 = x1 - xcm
x2 = x2 - xcm
print (x1, x2, xcm)
r1 = math.sqrt(x1**2 + y1**2)
r2 = math.sqrt(x2**2 + y2**2)

# years
h = 1e-3
t_final = 1
t_initial = 0
t = t_initial
count = 0

xarr1 = np.array([])
yarr1 = np.array([])
xarr1 = np.append(xarr1,x1)
yarr1 = np.append(yarr1,y1)

xarr2 = np.array([])
yarr2 = np.array([])
xarr2 = np.append(xarr2,x2)
yarr2 = np.append(yarr2,y2)

while (t < t_final):
      

      vx1 = vx1 - G * (m1+m2) * x1 * h / r1**3 
      x1 = x1 + vx1*h
      vy1 = vy1 - G * (m1+m2) * y1 * h / r1**3
      y1 = y1 + vy1*h

      
      vx2 = vx2 - G * (m1+m2) * x2 * h / r2**3
      x2 = x2 + vx2*h
      vy2 = vy2 - G * (m1+m2) * y2 * h / r2**3
      y2 = y2 + vy2*h

      r1 = math.sqrt(x1**2 + y1**2)
      r2 = math.sqrt(x2**2 + y2**2)
#      print (G*m1)
#      print (r, x1, y1, vx1, vy1)
#      print (r, x2, y2, vx2, vy2)
#      c = input()

      #if (count%200 == 0 ):                                                                                                         
      xarr1 = np.append(xarr1,x1)
      yarr1 = np.append(yarr1,y1)
      xarr2 = np.append(xarr2,x2)
      yarr2 = np.append(yarr2,y2)
      count += 1
  
      t = t+h

print (xarr1.size)

fig, ax = plt.subplots()
xdata1, ydata1 = [], []
xdata1b, ydata1b = [], []
xdata2, ydata2 = [], []
xdata2b, ydata2b = [], []

ln1b, = plt.plot([], [], 'ro', animated=True)
ln1, = plt.plot([], [], 'b', animated=True)
ln2b, = plt.plot([], [], 'ro', animated=True)
ln2, = plt.plot([], [], 'g', animated=True)

print (type(xdata1))

def init():
    ax.set_xlim(-2., 2.)
    ax.set_ylim(-2., 2.)
    return ln1, ln1b, ln2, ln2b

def update(frame):
    #print (type(frame))
    xdata1.append(xarr1[frame])
    ydata1.append(yarr1[frame]) 
    xdata1b = xarr1[frame]
    ydata1b = yarr1[frame]

    xdata2.append(xarr2[frame])
    ydata2.append(yarr2[frame])
    xdata2b = xarr2[frame]
    ydata2b = yarr2[frame]

    #ydata = yarr(frame)
    #xdata.append(frame)
    #ydata.append(np.sin(frame))
    ln1.set_data(xdata1, ydata1)
    ln1b.set_data(xdata1b, ydata1b)

    ln2.set_data(xdata2, ydata2)
    ln2b.set_data(xdata2b, ydata2b)

    return ln1, ln1b, ln2, ln2b

ani = FuncAnimation(fig, update, frames=xarr1.size, interval=20, init_func=init, blit=True)
plt.show()
