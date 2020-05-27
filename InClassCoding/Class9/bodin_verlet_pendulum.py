#Cassandra Bodin
#Phys 305
#verlet method for a pendulum

import matplotlib.pyplot as plt

theta=0.05
w = 0
a = -9.8*theta
t=0
h = 1e-2

#define plot value as lists
th1,w1,acc1, time=[],[],[],[]

while (t<10):
    theta += w*h +(.5)*a*h**2
    a1 = -9.8*theta
    w += (h/2)*(a1+a)
#plot using
    th1.append(theta)
    time.append(t)

    t+=h
    a=a1
    print (theta, w, a)

#initiate graph    
plt.plot(time,th1)
plt.show()
