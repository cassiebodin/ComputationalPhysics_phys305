#Cassandra Bodin
#Phys 305
#run using "python bodin_newton_raphson.py"

#function = exp(-x) +x -2

import math
import numpy as np

x = 2
i=0
def f(x):
    return math.exp(-x) + x -2 
def f_1(x):
    return -math.exp(-x)+ 1 #np.gradient(f) ????

while (f(x) > 10**-8):
    x = x - (f(x)/f_1(x))
    i+=1
    print(x)    
