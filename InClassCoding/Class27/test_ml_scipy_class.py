import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.stats import norm
import matplotlib.colors as colors
from mpl_toolkits import mplot3d

xdata = np.array([0.89,0.03,0.50,0.36,0.49])
#a = -1
#print (np.sum( np.log(1. + a*(xdata-0.5))))
#exit()

def negLogLikelihood(params, xdata): # the negative log likelohood-function
    a = params[0]
    lnl = -np.sum(np.log(1. + a*(xdata - 0.5)))
    return lnl


# minimize the negative log-Likelihood

result = minimize(negLogLikelihood,  # function to minimize
                  x0=-np.ones(1),     # start value
                  args=(xdata,),     # additional arguments for function
                  method='Powell',   # minimization method, see docs
                  )
# result is a scipy optimize result object, the fit parameters 
# are stored in result.x
print(result.x)
print(type(result.x))

ichoose = 0
if (ichoose == 0):
    fig, ax = plt.subplots(1,2)

    ax[0].hist(xdata, bins=20, range=(0,1), histtype='step', color='b')
    ax[0].set(title='xdata', xlabel='xdata', ylabel='number')

    avalues = np.linspace(-1.,1.,100)
    lvalues = np.zeros([100])
    for i in range(100):
        lvalues[i] = np.sum(np.log(1.0 + avalues[i]*(xdata-0.5)))
    ax[1].plot(avalues,lvalues,'r-')
    ax[1].set(title='log likelihood', xlabel='adata', ylabel='log likelihood')

    fig.tight_layout()
    plt.show()

else:
    exit()                         
