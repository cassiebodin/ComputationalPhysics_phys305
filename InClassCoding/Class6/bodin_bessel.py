#Cassandra Bodin
#Phys 305
#Hw 2
# run as "python bodin_bessel.py"

import numpy as np
import math
    
   
def j(x):
    return (np.sin(x)/x**2)-(np.cos(x)/x)

i=0
a=1.
b=1.
while (abs((b-a))<1e-6):
    i+=1
    mid = (a+b)/2
    if ((j(a)*j(mid))< 0):
        a=a
        b= mid
    else:
        a = mid
        b=b

print(a)
