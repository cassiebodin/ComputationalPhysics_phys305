import math
import numpy as np
import matplotlib.pyplot as plt

def energy(warg, thetarg):
      E = 0.5 * mass * length**2 * (warg**2 + g/length*thetarg**2)
      return E

g = 9.8
length = 1.
mass = 1.
h = 1e-2
print ('stepsize is ', h)

theta_0 = 0.35
omega_0 = 0.
theta = theta_0
omega = omega_0

t_init = 0.
t_final = 10.
t = t_init
count = 0

xarr = np.array([])
yarr = np.array([])
yarr2 = np.array([])
xarr = np.append(xarr,t)
yarr = np.append(yarr,theta)
yarr2 = np.append(yarr2,energy(omega, theta))

while (t < t_final):
      omega_i = omega
      omega = omega - g*length*theta*h
      theta = theta + omega_i*h
      #theta = theta + omega*h
      t = t + h
      #if (count%200 == 0 ):
      yarr = np.append(yarr,theta)
      xarr = np.append(xarr,t)
      yarr2 = np.append(yarr2,energy(omega, theta))
      count += 1

#now plot
fig, ax = plt.subplots(1,2)

ax[0].plot (xarr, yarr, 'b')
ax[0].set(title='title', xlabel='x axis', ylabel='y axis')
ax[0].grid()

ax[1].plot (xarr, yarr2, 'b')
ax[1].set(title='title', xlabel='x axis', ylabel='y axis')
ax[1].grid()

plt.show()

