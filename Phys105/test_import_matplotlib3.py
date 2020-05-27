import math
import random
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.animation as animation
import numpy as np


# some examples with matplotlib
# see https://matplotlib.org/users/examples_index.html

fig, ax = plt.subplots()
ax.set_xlim(0, 200)
ax.set_ylim(-20, 20)


def update(frame):
    x.append(frame)
    y.append(np.sin(frame))
    ln.set_data(x, y)
    return ln,


nwalkers = 2
nsteps = 200

# initialize
x = np.zeros(nwalkers)
y = np.zeros(nwalkers)
random.seed()

for i in range(nwalkers):

     for j in range(nsteps):
         x[i] += 1
         if random.random() > 0.5:
             y[i] += 1.
         else:
             y[i] += -1.


#print np.average(x)
#print np.average(y)
#print np.std(y)
#print y
  
# now histogram y

ani = animation.FuncAnimation(fig, update, , 
                              init_func=init)
plt.show()




