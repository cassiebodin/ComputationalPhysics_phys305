import math
import numpy as np
import matplotlib.pyplot as plt

# ...

ymax = 30.
y = ymax
xarr = np.array([])
yarr = np.array([])
xarr = np.append(xarr,0.)
yarr = np.append(yarr,y)
#print (xarr.size)
count = 0

while (y > 0):


      if (count%200 == 0 ):
            yarr = np.append(yarr,y)
            xarr = np.append(xarr,0.)
      count += 1
# ...

yarr = np.append(yarr,y)
xarr = np.append(xarr,0.)

#now plot
fig, ax = plt.subplots()

ax.plot (xarr, yarr, 'bo',linestyle='none')
ax.set(title='title', xlabel='x axis', ylabel='y axis')
ax.grid()

plt.show()
