import matplotlib.pyplot as plt
import numpy as np

# m is the number of space steps
m = 50
dcoeff=4.25e-4
length=0.2
# h is the time step
h = 1e-2
a = length / m
c = dcoeff * h / a**2

temp_high = 100.
temp_start = 20.

temp = np.zeros([m],float)
#print (temp.shape)
temp[0] = temp_high
temp[1:] = temp_start

tempprime = np.zeros([m],float)
tempprime[0] = temp_high
tempprime[1:] = temp_start

xarr = np.linspace(0,length,m)
yarr = np.zeros(m,float)
#print (y.shape)

snapshot = np.array ([0.01,0.1,0.5,2,10,50,100,500])

t = 0.
t_stop = 501.
epsilon = 1e-6

fig, ax = plt.subplots()

while t < t_stop:

    # put the code here for calculating the new temperature, tempprime, 
    # in terms of the old temperature - see slide 11
    for i in range(1,m-1):
        tempprime[i]=temp[i]+ c*(temp[i+1]+temp[i-1]-2*temp[i])
        i+=1
    tempprime[m-1]=tempprime[m-2]

    t += h
    temp, tempprime = tempprime, temp

    for i in range(8):
        if (abs(t - snapshot[i]) < epsilon):
            yarr = tempprime
            ax.plot(xarr,yarr,'b')

plt.title("solving heat equation")
plt.xlabel("position along rod")
plt.ylabel("temperature")
plt.text(0.1,60,'for times 0.01,0.1,0.5,2,10,50,100 s')
plt.savefig("heat_example.png")
plt.show()



