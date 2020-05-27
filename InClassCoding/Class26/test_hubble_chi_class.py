#! /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2
import scipy.special as special

def func(x,m,b):
# this is the function to fit
    return m*x+b
 
x = np.array([0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.45, 0.5, 0.5, 0.63, \
0.8, 0.9, 0.9, 0.9, 0.9, 1.0, 1.1, 1.1, 1.4, 1.7, 2., 2., 2., 2.])
y = np.array([170,290,-130,-70,-185,-220,200,290,270,200, \
300,-30,650,150,500,920,450,500,500,960,500,850,800,1090])
#yerr = y*0.1
# note!!  i made these errors up just for this problem
yerr = np.ones(x.size)*100
print (x.shape)
print (y.shape)
print (yerr.shape)

# Fit the curve
start = (1,1)
popt, pcov = curve_fit(func,x,y, sigma = yerr, p0 = start, absolute_sigma=True)
print('popt = ',popt)
print('pcov = ',pcov)

yexp = func(x,*popt)
# 
#  add code here to calculate ndof, chi**2, p-value
#  hint: to calculate the p-value use 1-cdf and look at scipy stats.chi2
#
ndof=x.size-2
print("number of degrees of freedom is:",ndof)
chi_sq=0
for i in range(x.size):
    chi_sq+=(y[i]-yexp[i])**2/(yerr[i]**2)
    i+=1
print ("chi_sq is: ",chi_sq)
p_val=1-chi2.cdf(chi_sq,ndof,loc=0,scale=1)
print ("p_val is", p_val)




fig, ax = plt.subplots()
ax.errorbar(x,y,yerr=yerr, fmt = 'o', label='"data"')
ax.plot(x,yexp,label='fit')
ax.set(title='title', xlabel='distance (Mpc)', ylabel='velocity (km/s)')
ax.grid()

plt.legend()
plt.show()
