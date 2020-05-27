#! /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# this is the function to fit
# add a return statement to return the value of the line fit at value x
def func(x,m,b):
    return m*x+b

 
x = np.array([0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.45, 0.5, 0.5, 0.63, \
0.8, 0.9, 0.9, 0.9, 0.9, 1.0, 1.1, 1.1, 1.4, 1.7, 2., 2., 2., 2.])
y = np.array([170,290,-130,-70,-185,-220,200,290,270,200, \
300,-30,650,150,500,920,450,500,500,960,500,850,800,1090])
yerr = np.full(24,.01)
print (x.shape)
print (y.shape)
print (yerr.shape)

#  your calls to the curve_fit method go here.
#  supply a func for the line fit above
#  the curve_fit method returns arguments popt and pcov
popt,pcov = curve_fit(func,x,y, sigma=yerr, absolute_sigma=True)#**************************

print('popt = ',popt)
print('pcov = ',np.sqrt(pcov))#**************************

nobs = 24
stdev = 1
yexp = func(x,*popt)
r = y - yexp
chisq = np.sum((r/stdev)**2)
df = nobs - 2
print("chisq",chisq,"df",df)

fig, ax = plt.subplots()
ax.errorbar(x,y,yerr=yerr, fmt = 'o', label='"data"')
ax.plot(x,yexp,label='fit')
ax.set(title='title', xlabel='x axis', ylabel='yaxis')
ax.grid()

plt.plot(x, func(x,*popt), 'b')#**************************
plt.legend()
plt.show()
