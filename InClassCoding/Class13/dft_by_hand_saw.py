import numpy as np
import math
import matplotlib.pyplot as plt

f = open('saw_data.txt','r')

time = np.array([])
amplitude = np.array([])

for line in f:
  s = line.split()
  time = np.append(time,float(s[0]))
  amplitude = np.append(amplitude,float(s[1]))

print ('samples = ', np.size(time))
nsamples = np.size(time)
h = time[1]-time[0]
print ('h = ',h)
samplingf = nsamples / (nsamples*h)
print (samplingf, 1/h)

frequency = np.array([])
Y = np.zeros((nsamples,), dtype=complex)
for n in range(nsamples):
    frequency = np.append(frequency,n/(nsamples*h))
    for m in range(nsamples):
        Y[n] += amplitude[m]*np.exp((-2*np.pi*1j*m*n)/nsamples)


print (type(amplitude))
print (type(Y))

fig, ax = plt.subplots(2, 1)
ax[0].plot(frequency[0:100], Y.imag[0:100])
ax[0].set(title='title', xlabel='x axis', ylabel='y axis')
ax[0].grid()

ax[1].plot(frequency[0:100], Y.real[0:100])
ax[1].set(title='title', xlabel='x axis', ylabel='y axis')
ax[1].grid()

plt.show() 
