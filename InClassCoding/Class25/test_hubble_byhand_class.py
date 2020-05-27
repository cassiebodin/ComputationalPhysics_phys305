#! /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(x,m,b):
# this is the function to fit
    return m*x+b
 
x = np.array([0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.45, 0.5, 0.5, 0.63, \
0.8, 0.9, 0.9, 0.9, 0.9, 1.0, 1.1, 1.1, 1.4, 1.7, 2., 2., 2., 2.])
y = np.array([170,290,-130,-70,-185,-220,200,290,270,200, \
300,-30,650,150,500,920,450,500,500,960,500,850,800,1090])
yerr = np.full(24,.01)
#print (x.shape)
#print (y.shape)
#print (yerr.shape)

s1 = 0
sx = 0
sy = 0
sx2 = 0
sy2 = 0
sxy = 0


for i in range(x.size):
    s1+=1/yerr[i]**2
    sx+=x[i]/yerr[i]**2
    sy+=y[i]/yerr[i]**2
    sx2+=x[i]**2/yerr[i]**2
    sy2+=y[i]**2/yerr[i]**2
    sxy+=(x[i]*y[i])/yerr[i]**2
# form the necessary sums here
# once you have the sums, fill in 
# combinations for Delta, slope, intercept and errors below

delta = s1*sx2-sx*sx
# use the correct combinations of the sums here
a0 = (1/delta)*((sx2*sy)-(sx*sxy))
a1 = (1/delta)*((s1*sxy)-(sx*sy))
a0err = (1/delta)*sx2
a1err = (1/delta)*s1
print ("a0 is:",a0,"with uncertainty:", a0err,"a0 is:",a1,"with uncertainty:", a1err)

nobs = 24
stdev = 1
yexp = func(x,a1,a0)
r = y - yexp
chisq = np.sum((r/stdev)**2)
df = nobs - 2
print("chisq",chisq,"df",df)

fig, ax = plt.subplots()
ax.errorbar(x,y,yerr=yerr, fmt = 'o', label='"data"')
ax.plot(x,yexp,label='fit')
ax.set(title='hubble', xlabel='x axis', ylabel='yaxis')
ax.grid()

plt.legend()
plt.show()
