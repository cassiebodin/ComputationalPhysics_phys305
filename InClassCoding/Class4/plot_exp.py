import matplotlib.pyplot as plt
import numpy as np

# example simple plot

# these are numpy arrays
#x   = np.arange(0, 5, 0.1)
x = np.linspace(0.,10.,100)
y   = np.exp(x)

fig, ax = plt.subplots()

#ax.plot(time, amplitude, color='red', marker='.', linestyle='none')
ax.plot (x, np.log(y), 'r')

ax.set(title='exponential', xlabel='x axis', ylabel='y axis')

# not needed, is just a useful flair
ax.grid()

fig.savefig("sine.png")

plt.show()
