#Cassandra Bodin
#Phys305
#Homework 12

#run using "Python hmk12_bodin.py"


#Problem 1:measure gamma, gamma error, chi_2.
#What does the value gamma tell us about our universe? if gamma=1 then steadily expanding

def Problem1():
#! /usr/bin/python3

    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.optimize import curve_fit
    from scipy.stats import chi2
    import scipy.special as special

    # this is the function to fit
    # add a return statement to return the value of the line fit at value x
    def func(x,m,b):
# this is the function to fit
        return m*x+b

#to read the data file perlmutter.dat and read z
    f= open("perlmutter.dat", "r")
    z= np.array([])
    m= np.array([])
    merr= np.array([])
    for line in f:
        s=line.split()
        z=np.append(z,float(s[0]))
        m=np.append(m,float(s[1]))
        merr=np.append(merr,float(s[2]))
    f.close
    #print (z)
    #print (m)
    #print(merr)

    z=np.log10(z)

    #  your calls to the curve_fit method go here.
    #  supply a func for the line fit above
    #  the curve_fit method returns arguments popt and pcov
    start = (1,1)
    popt,pcov = curve_fit(func,z,m, sigma=merr, p0=start, absolute_sigma=True)

    print('popt = ',popt)
    print('pcov = ',np.sqrt(pcov))
    print("gamma =", popt[:1]/5)
    print("sigma =", np.sqrt(pcov[0,0]))

    mexp=func(z,*popt)
    #print(mexp)

    df=z.size -2
    #print ("ndof is: ", df)
    chi_sq=0
    for i in range(z.size):
        chi_sq+=(m[i]-mexp[i])**2/(merr[i]**2)
        i+=1
    print("chi_sq is: ",chi_sq)
    p_val = 1-chi2.cdf(chi_sq,df,loc=0,scale=1)

    fig, ax = plt.subplots()
    ax.errorbar(z,m,yerr=merr, fmt = 'o', label='"data"')
    ax.plot(z,mexp,label='fit')
    ax.set(title='title', xlabel='x axis', ylabel='yaxis')
    ax.grid()

    ax.plot(z, func(z,*popt), 'b')
    plt.savefig('hmk12_expanding_universe.png')
    plt.legend()
    plt.show()
Problem1()


#print("________________________________________________________________________")

#Problem 3: generate a histogram of 100numbers according to a Gaussian distribution.
#mu=100, std=5

def Problem3():
    import numpy as np
    import random
    import matplotlib.pyplot as plt

    random.seed()
    mu,sigma = 100,5
    s=np.random.normal(mu,sigma,1000)
    
    mu_graph= np.mean(s)
    sigma_graph= np.std(s,ddof=1)
    print ("Mean is ", mu_graph)
    print("Standard Deviation is ", sigma_graph)

    count,bins,ignores = plt.hist(s,30,density=True)
    plt.plot(bins,1/(sigma*np.sqrt(2*np.pi))*np.exp(- (bins-mu)**2/(2*sigma**2)), linewidth=2, color='b')
    plt.savefig('hmk12_gausian.png')
    plt.show()
Problem3()
