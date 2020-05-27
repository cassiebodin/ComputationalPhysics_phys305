import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.stats import norm
import matplotlib.colors as colors
from mpl_toolkits import mplot3d


xdata = np.array([4,5,7,8,8,9,10,5,2,3,5,4,8,9])



def negLogLikelihood(params, xdata):
    # the negative log likelohood-function
    # add a calculation of the negative log likelihood here
    n = float(xdata.size)
    lnl = -np.sum(np.log(1. + n*(xdata - 0.5)))
    return lnl


# get poisson deviated random numbers
#data = np.random.poisson(2, 1000)

# minimize the negative log-Likelihood

result = minimize(negLogLikelihood,  # function to minimize
                  x0=np.ones(2),     # start value
                  args=(xdata,),     # additional arguments for function
                  method='Powell',   # minimization method, see docs
                  )
# result is a scipy optimize result object, the fit parameters 
# are stored in result.x
print(result.x)
print(type(result.x))

# plot poisson-deviation with fitted parameter

#x_plot = np.linspace(0, 20, 1000)

ichoose = 1
if (ichoose == 0):
    fig, ax = plt.subplots(2,2)

    xvalues = np.linspace(0,20,1000)
    ax[0,0].hist(xdata, bins=20, range=(0,20), histtype='step', color='b', density=True)
    ax[0,0].set(title='xdata', xlabel='xdata', ylabel='probability')

    ax[0,1].hist(xdata, bins=20, range=(0,20), histtype='step', color='b', density=True)
    ax[0,1].set(title='xdata', xlabel='xdata', ylabel='probability')
    ax[0,1].plot(xvalues,norm.pdf(xvalues,loc=5,scale=3),'r-')
    ax[0,1].plot(xvalues,norm.pdf(xvalues,loc=7,scale=3),'g-')

# correct result
    ax[1,0].hist(xdata, bins=20, range=(0,20), histtype='step', color='b', density=True)
    ax[1,0].set(title='xdata', xlabel='xdata', ylabel='probability')
    ax[1,0].plot(xvalues,norm.pdf(xvalues,loc=result.x[0],scale=result.x[1]),'r-')

# 2d plot
    x = np.linspace(5.5,7.,100)
    y = np.linspace (2.,3.5,100)
#xd, yd = np.meshgrid(x,y)
    z = np.zeros([100,100],float)

    n = float(xdata.size)
    for i in range(100):
        for j in range(100):
            z[i,j] = (n/2)*np.log(2*np.pi) + (n/2)*np.log(y[j]**2) + (1./2./y[j]**2)*np.sum( (xdata-x[i])**2 )

    pcm = ax[1,1].pcolormesh(x, y, z, cmap='jet')
    fig.colorbar(pcm, ax=ax[1,1])
    ax[1,1].set_title('pcolormesh')
    ax[1,1].set_xlabel('x axis')
    ax[1,1].set_ylabel('y axis')

    fig.tight_layout()
    plt.show()

else:
    fig, ax = plt.subplots()

# 2d plot                                                                                                                                                                         
    x = np.linspace(6.,6.4,100)
    y = np.linspace (2.2,2.6,100)
#xd, yd = np.meshgrid(x,y)                                                                                                                                                        
    z = np.zeros([100,100],float)

    n = float(xdata.size)
    for i in range(100):
        for j in range(100):
            z[i,j] = (n/2)*np.log(2*np.pi) + (n/2)*np.log(y[j]**2) + (1./2./y[j]**2)*np.sum( (xdata-x[i])**2 )

    pcm = ax.pcolormesh(x, y, z, cmap='jet')
    fig.colorbar(pcm, ax=ax)
    ax.set_title('pcolormesh')
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')

    fig.tight_layout()
    plt.show()
