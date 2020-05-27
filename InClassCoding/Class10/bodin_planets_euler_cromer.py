import math
import numpy as np
import matplotlib.pyplot as plt

def energy(varg, rarg):
      rarg = rarg * 1.496e11
      varg = varg * 1.496e11 / 3.154e7
      E = 0.5 * m_earth * varg**2 - G * m_sun * m_earth / rarg 
      return E

g = 9.8
G = 6.67e-11
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
h = 1e-3
t_final = 2
t_initial = 0
t = t_initial
count = 0

xarr = np.array([])
xarr2 = np.array([])
yarr = np.array([])
yarr2 = np.array([])
xarr = np.append(xarr,x)
yarr = np.append(yarr,y)
r = math.sqrt(x**2 + y**2)
v = math.sqrt(vx**2 + vy**2)

xarr2 = np.append(xarr2, t)
yarr2 = np.append(yarr2,energy(v,r))

while (t<10):
    
    vx +=(- GMs * x * h / r**2 )
    x += vx*h
    vy +=( - GMs * y * h / r**2)
    y += vy*h
    r = math.sqrt(x**2 + y**2)
    v = math.sqrt(vx**2 + vy**2)


      #if (count%200 == 0 ):                                                                                                         
    xarr = np.append(xarr,x)
    yarr = np.append(yarr,y)
    xarr2 = np.append(xarr2,t)
    yarr2 = np.append(yarr2,energy(v,r))
    count += 1
  
    t +=h
 
#now plot
fig, ax = plt.subplots()

ax.plot (xarr, yarr, 'b')
ax.set(title='earth orbit', xlabel='x axis', ylabel='y axis')
ax.grid()

#ax.plot (xarr2, yarr2, 'b')
#ax.set(title='title', xlabel='x axis', ylabel='y axis')
#ax.grid()

plt.show()
