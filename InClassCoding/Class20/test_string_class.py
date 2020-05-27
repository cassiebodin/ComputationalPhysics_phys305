import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


rho = 0.01;   
T = 40.
c = math.sqrt(T/rho)
# space spacing 
a = 5
time = 50
# time spacing
h = 0.01
L = 2
asize = int((L/h)+1)
ratio = (c*c*h*h)/(a*a)

print ('c = ',c)
print ('cprime = ',(a*a)/(h*h))
print ('want c < cprime')
print ('asize is ',asize)

# 3 = past, present, future
y = np.zeros((asize,3), float)
print (y.shape)
x = np.linspace(0,L,asize)
print (x.shape)
print (x)

# initialize the position at the present time
y[:,1] = 0.5*np.sin(np.pi*x/L)
#print (y[:, 1])


for i in range(asize):
    if i == 0: 
        y[i,2] = 0
    elif i == 200:
        y[i,2] = 0
    else:
# initialize the position at a future time
        y[i,2] = y[i,1] + (ratio/2)*(y[i+1,1] + y[i-1,1] - 2*y[i,1])
# done initialize

y[:, 0] = np.copy(y[:, 2])
#print (y[:,0])
#print (y[:,1])
#print (y[:,2])

yarr = np.zeros( (1,asize) ) 
yarr[0, :] = np.copy(y[:, 2])
print (yarr.shape)
idx = 1

count = 0
timesteps = int(time/h)
print (timesteps)
for j in range(timesteps):
    y[:, 0] = np.copy(y[:, 1])
    y[:, 1] = np.copy(y[:, 2])
    for i in range(asize):
       if i == 0:
         y[i,2] = 0
       elif i == 200:
         y[i,2] = 0
       else:
# put the position at a future time here
        y[i,2] = 2*y[i,1]-y[i,0]+ ratio*(y[i+1,1]+y[i-1,1]-2*y[i,1])
    count += 1
    if (count%50 == 0):
       idx += 1
       temp = y[:, 2]
       yarr = np.append(yarr, [y[:, 2]], axis=0)    
       #print (y[:, 2])

fig, ax = plt.subplots()
xdata, ydata = [], []
ln1, = plt.plot([], [], 'b', animated=True)
print (type(xdata))
  
def init():
    ax.set_xlim(0., 2.)
    ax.set_ylim(-1.,1.) 
    return ln1,

def update(frame):
    #print (frame)
    xdata = x
    ydata = yarr[frame, :]
    ln1.set_data(xdata, ydata)
    return ln1,

print ('idx = ',idx)
print (yarr.shape)

ani = FuncAnimation(fig, update, frames=int(idx), interval=50, init_func=init, blit=True)
plt.title("solving wave equation")
plt.xlabel("position along string")
plt.ylabel("displacement")
plt.show()

