import matplotlib.pyplot as plt
import numpy as np

# example simple plot

# these are numpy arrays
#x   = np.arange(0, 5, 0.1)

def f(x):
    return  3*x**5+20*x**4-10*x**3-240*x**2-250*x+200
i=0
a=0.
b=2.

while (abs((b-a)) > 1e-6):
    i += 1
    mid = (a+b)/2
    if ((f(a)*f(mid))< 0):
        a=a
        b= mid
    else:
        a = mid
        b=b

print(a)
