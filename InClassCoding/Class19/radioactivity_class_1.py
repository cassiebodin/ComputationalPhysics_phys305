import random
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('multipage.pdf')

N0 = 1000
N = N0
# in seconds
halftau = 693000.
lam = math.log(2)/halftau
h = 10
prob = 1 - math.exp(-lam*h)
print ('prob =',prob)

# your code goes here
# you are making a geiger counter
# if there is a decay, yarr is 1, otherwise it is 0
# tarr is the time array
time = 693000
t = 0
tarr = np.arange(0,time,h)
yarr = np.zeros(tarr.size)
Narr = np.zeros(tarr.size)
random.seed()

for i in range(tarr.size):
   for nuc in range(N):
      r = random.random()
      if (r < prob):
         yarr[i] = 1
         N -= 1
         break
      else:
         yarr[i] = 0
   Narr[i] = N
print (N0, N)

fig, ax = plt.subplots()

#ax.plot(time, amplitude, color='red', marker='.', linestyle='none')
ax.plot (tarr, yarr, 'b')
ax.set(title='title', xlabel='x axis', ylabel='y axis')

plt.show()

