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

#time = 24*60*60
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

choose = 1
if choose == 0:
   ax.plot (tarr[0:2000], yarr[0:2000], 'b')
   ax.set(title='title', xlabel='time', ylabel='number')
   plt.show()
else:
   ax.plot (tarr, Narr, 'b')
   ax.set(title='title', xlabel='time', ylabel='number')               
   ax.grid()
   plt.show()

pp.close()
