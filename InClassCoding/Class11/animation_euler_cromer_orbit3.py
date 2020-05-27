import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#xarr = np.array([-.4, -.3, -.2, -.1, 0, .1, .2, .3, .4, .5])
#yarr = np.array([-.4, -.3, -.2, -.1, 0, .1, .2, .3, .4, .5])

g = 9.8
G = 6.674e-11
GMs = 4*(math.pi**2)
m_sun = 1.989e30

ecc_earth = 0.0167
semimajor_earth = 1.00000011 
a_earth = semimajor_earth
perihelion_earth = a_earth*(1-ecc_earth)
m_earth = 9.72e24

ecc_jup = 0.0489
semimajor_jup = 5.2044
a_jup = semimajor_jup
perihelion_jup = a_jup*(1-ecc_jup)
m_jup = 1.8982e27



vp_earth = math.sqrt(GMs) * math.sqrt((1+ecc_earth) / (a_earth*(1-ecc_earth)) * (1+(m_earth/m_sun)))
vx = 0
vy = vp_earth
x = -perihelion_earth
y = 0 

vp_jup = math.sqrt(GMs) * math.sqrt((1+ecc_jup) / (a_jup*(1-ecc_jup)) * (1+(m_jup/m_sun)))
vx2 = 0
vy2 = vp_jup
x2 = -perihelion_jup
y2 = 0

# years
h = 1e-2
t_final = 10
t_initial = 0
t = t_initial
count = 0

xarr = np.array([])
yarr = np.array([])
xarr = np.append(xarr,x)
yarr = np.append(yarr,y)
r = math.sqrt(x**2 + y**2)
v = math.sqrt(vx**2 + vy**2)

xarr2 = np.array([])
yarr2 = np.array([])
xarr2 = np.append(xarr2,x2)
yarr2 = np.append(yarr2,y2)
r2 = math.sqrt(x2**2 + y2**2)
v2 = math.sqrt(vx2**2 + vy2**2)

while (t < t_final):

      r = math.sqrt(x**2 + y**2)
      r2 = math.sqrt(x2**2 + y2**2)
      rrel = math.sqrt( (x-x2)**2 + (y-y2)**2)
      
      # complete the next four lines of code
      # vx, vy is jupiter
      # vx2, vy2 is earth
      vx = vx +h*(-GMs*x/r**3- GMs*(m_jup/m_sun)*(x-x2)/r2**3)
      vy = vy+h*(-GMs*y/r**3- GMs*(m_jup/m_sun)*(y-y2)/r2**3)
      vx2 = vx2 +h*(-GMs*x2/r2**3- GMs*(m_jup/m_sun)*(x2-x)/r**3)
      vy2 = vy2 +h*(-GMs*y2/r2**3 - GMs*(m_jup/m_sun)*(y2-y)/r**3)

      x = x + vx*h
      y = y + vy*h
      x2 = x2 + vx2*h
      y2 = y2 + vy2*h

      #if (count%200 == 0 ):                                                                                                         
      xarr = np.append(xarr,x)
      yarr = np.append(yarr,y)
      xarr2 = np.append(xarr2,x2)
      yarr2 = np.append(yarr2,y2)
      count += 1
  
      t = t+h

print (xarr.size)

fig, ax = plt.subplots()
xdata, ydata = [], []
xdata2, ydata2 = [], []
xdata3, ydata3 = [], []
xdata4, ydata4 = [], []

ln1, = plt.plot([], [], 'ro', animated=True)
ln2, = plt.plot([], [], 'b', animated=True)
ln3, = plt.plot([], [], 'ro', animated=True)
ln4, = plt.plot([], [], 'g', animated=True)
print (type(xdata))

def init():
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)
    return ln1, ln2, ln3, ln4

def update(frame):
    #print (type(frame))
    xdata2.append(xarr[frame])
    ydata2.append(yarr[frame]) 
    xdata = xarr[frame]
    ydata = yarr[frame]

    xdata4.append(xarr2[frame])
    ydata4.append(yarr2[frame])
    xdata3 = xarr2[frame]
    ydata3 = yarr2[frame]

    #ydata = yarr(frame)
    #xdata.append(frame)
    #ydata.append(np.sin(frame))
    ln1.set_data(xdata, ydata)
    ln2.set_data(xdata2, ydata2)
    ln3.set_data(xdata3, ydata3)
    ln4.set_data(xdata4, ydata4)
    return ln1, ln2, ln3, ln4

ani = FuncAnimation(fig, update, frames=xarr.size, interval=50, init_func=init, blit=True)
plt.show()
