import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.stats import norm
import matplotlib.colors as colors
from mpl_toolkits import mplot3d


def P(xdata,avalues):
    return 1.+avalues*(xdata-.5)

xdata = np.array([0.89,0.03,0.50,0.36,0.49])
avalues = np.linspace(-1.,1.,100)
lvalues = np.zeros([100])

#  
# calculate the sum of the log likelihoods for each avalue
# put the result in lvalues
#
lval=0
psum=0
for i in range(xdata.size):
    psum=P(xdata[i],avalues)
    lvalues+= np.log(psum)
    #lvalues=np.append(lvalues,lval)
print(lvalues)

ichoose = 0
if (ichoose == 0):
    fig, ax = plt.subplots(1,2)

    ax[0].hist(xdata, bins=20, range=(0,1), histtype='step', color='b')
    ax[0].set(title='xdata', xlabel='xdata', ylabel='number')

    ax[1].plot(avalues,lvalues,'r-')
    ax[1].set(title='log likelihood', xlabel='adata', ylabel='log likelihood')

    fig.tight_layout()
    plt.show()

else:
    exit()                 
