import math
import matplotlib.pyplot as plt
import numpy as np

# example 4 simple plots

T = 2.
omega = 2*math.pi/T
h = 1e-2
t = np.arange(0.,2.*T,h)
fac = 2/math.pi
y = np.zeros(np.size(t))
print (type(y))
print (np.size(y))
x = np.copy(t)


def sumsin(narg):
    global t
    global y
    #print (np.size(t))
    #print (np.size(y))
    for i in range(narg):
### add code here
       y +=(2/math.pi)*(((-1)**(i)/(i+1))*np.sin((i+1)*omega*t))
       i+=i
### add code here
    return

y = np.zeros(np.size(t)) 
sumsin(2)
y2 = np.copy(y)
y = np.zeros(np.size(t))
sumsin(4)
y4 = np.copy(y)
y = np.zeros(np.size(t))
sumsin(10)
y10 = np.copy(y)
y = np.zeros(np.size(t))
sumsin(20)
y20 = np.copy(y) 

fig, ax = plt.subplots(2,2)
ax[0,0].plot (x, y2, 'b')
ax[0,0].set(title='title', xlabel='x axis', ylabel='y axis')
ax[0,0].grid()


ax[0,1].plot (x, y4, 'b')
ax[0,1].set(title='title', xlabel='x axis', ylabel='y axis')
ax[0,1].grid()

ax[1,0].plot (x, y10, 'b')
ax[1,0].set(title='title', xlabel='x axis', ylabel='y axis')
ax[1,0].grid()

ax[1,1].plot (x, y20, 'b')
ax[1,1].set(title='title', xlabel='x axis', ylabel='y axis')
ax[1,1].grid()

#fig.savefig("sine.png")

plt.tight_layout()

plt.show()
