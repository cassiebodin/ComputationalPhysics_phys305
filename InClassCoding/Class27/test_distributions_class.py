import math
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import norm
from scipy.stats import chi2

random.seed()


nevt = 100
binoarr = np.array([])
poisarr = np.array([])
gausarr = np.array([])
chi2arr = np.array([])

n=5
p=.4
mu=.6
df=55



# binomial
binoarr= binom.rvs(n,p,loc=0,size=nevt,random_state=None)


# poisson
poisarr= poisson.rvs(mu,loc=0,size=nevt,random_state=None)

# gaussian
gausarr=norm.rvs(loc=0,size=nevt,random_state=None)

# chi2
chi2arr= chi2.rvs(df,loc=0,size=nevt,random_state=None)

ichoose = 0
if ichoose == 0:

      fig, ax = plt.subplots(2,2)
      #print (zarr1)
      ax[0,0].hist(binoarr, bins=20, range=(0,10), histtype='step', color='b')
      ax[0,0].set(title='binomial', xlabel='x', ylabel='number') 

      ax[0,1].hist(poisarr, bins=20, range=(0,10), histtype='step', color='b')
      ax[0,1].set(title='poisson', xlabel='x', ylabel='number')

      ax[1,0].hist(gausarr, bins=20, range=(0,10), histtype='step', color='b')
      ax[1,0].set(title='gaussian', xlabel='x', ylabel='number')

      ax[1,1].hist(chi2arr, bins=20, range=(-10,10), histtype='step', color='b')
      ax[1,1].set(title='chi2', xlabel='x', ylabel='number')

      plt.tight_layout()
      plt.show()

