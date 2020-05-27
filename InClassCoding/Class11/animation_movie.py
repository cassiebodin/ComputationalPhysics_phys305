import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#xarr = np.array([-.4, -.3, -.2, -.1, 0, .1, .2, .3, .4, .5])
#yarr = np.array([-.4, -.3, -.2, -.1, 0, .1, .2, .3, .4, .5])

g = 9.8
GMs = 4*(math.pi**2)
ecc_earth = 0.0167
semimajor_earth = 1.00000011 
a = semimajor_earth
perihelion_earth = a*(1-ecc_earth)
m_earth = 9.72e24
m_sun = 1.989e30
vp_earth = math.sqrt(GMs) * math.sqrt((1+ecc_earth) / (a*(1-ecc_earth)) * (1+(m_earth/m_sun)))
vx = 0
vy = vp_earth
x = -perihelion_earth
y = 0 

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

while (t < t_final):
      
      vx = vx - GMs * x * h / r**3 
      x = x + vx*h
      vy = vy - GMs * y * h / r**3
      y = y + vy*h
      r = math.sqrt(x**2 + y**2)
      v = math.sqrt(vx**2 + vy**2)

      #if (count%200 == 0 ):                                                                                                         
      xarr = np.append(xarr,x)
      yarr = np.append(yarr,y)
      count += 1
  
      t = t+h

print (xarr.size)

fig, ax = plt.subplots()
xdata, ydata = [], []
x2data, y2data = [], []
ln1, = plt.plot([], [], 'ro', animated=True)
ln2, = plt.plot([], [], 'b', animated=True)
print (type(xdata))

def init():
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    return ln1,ln2

def update(frame):
    #print (type(frame))
    x2data.append(xarr[frame])
    y2data.append(yarr[frame]) 
    xdata = xarr[frame]
    ydata = yarr[frame]

    #ydata = yarr(frame)
    #xdata.append(frame)
    #ydata.append(np.sin(frame))
    ln1.set_data(xdata, ydata)
    ln2.set_data(x2data, y2data)
    return ln1, ln2

ani = FuncAnimation(fig, update, frames=xarr.size, interval=50, init_func=init, blit=True)
 
#make the movie
from matplotlib.animation import FFMpegWriter
writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save("movie.mp4", writer=writer)
   
plt.show()

