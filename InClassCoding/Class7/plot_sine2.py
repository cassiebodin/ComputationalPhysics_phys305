import math
import matplotlib.pyplot as plt
import numpy as np

# example 4 simple plots

x = np.linspace(0.,10.,100)
y   = np.sin(x)

fig, ax = plt.subplots(2,2)
x = np.linspace(0.,10.,100)
y = np.sin(x)
ax[0,0].plot (x, y, 'b')
ax[0,0].set(title='title', xlabel='x axis', ylabel='y axis')
ax[0,0].grid()

y=np.array([])
x = np.arange(0,10,0.1)
for i in x:
    y = np.append(y,math.sin(i))
ax[0,1].plot (x, y, 'b')
ax[0,1].set(title='title', xlabel='x axis', ylabel='y axis')
ax[0,1].grid()


x=[]
y=[]
for i in range(0,100):
    x.append(i/10.)
    y.append(math.sin(i/10.))

x = np.array(x)
y= np.array(y)
ax[1,0].plot (x, y, 'b')
ax[1,0].set(title='title', xlabel='x axis', ylabel='y axis')
ax[1,0].grid()

x=[]
y=[]
xx = 0.
h = 0.1
while (xx < 10.):
    x.append(xx)
    y.append(math.sin(xx))
    xx = xx + h

x = np.array(x)
y= np.array(y)
ax[1,1].plot (x, y, 'b')
ax[1,1].set(title='title', xlabel='x axis', ylabel='y axis')
ax[1,1].grid()

#fig.savefig("sine.png")

plt.tight_layout()

plt.show()
