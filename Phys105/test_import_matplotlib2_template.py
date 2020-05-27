import math
import random
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np


# some examples with matplotlib
# see https://matplotlib.org/users/examples_index.html

nwalkers = 500
nsteps = 200

# initialize
x = np.zeros(nwalkers)
y = np.zeros(nwalkers)
random.seed()

# write python code 
# to loop over the number of walkers
# to loop over the number of steps
# fill the numpy array x with the step
# fill the numpy array y with a 1d random walk step

print np.average(x)
print np.average(y)
print np.std(y)
#print y
  
# now histogram y
n, bins, patches = plt.hist(y, bins=50, range=(-50.,50.), color='blue')
plt.xlabel('end position')
plt.ylabel('counts')
plt.show()




