import random
import math
import numpy as np
import matplotlib.pyplot as plt

N0 = 1000
N = N0
# in seconds
halftau = 693000.
lam = math.log(2)/halftau
tau = 1/lam
h = 10
prob = 1 - math.exp(-lam*h)
print (halftau, tau, lam)
print ('prob =',prob)

time= 0
t = np.array([])
t=np.append(t,time)
for i in range(2000):
    time=random.expovariate(lam)
##
## put your code to generate a randome number according to the exponential here
## you will want to append the result to the numpy array t
    t = np.append(t,time)

fig, ax = plt.subplots()

ax.hist(t, bins=100, histtype='step')      
ax.set(title='title', xlabel='time', ylabel='number')               
ax.grid()

plt.show()

