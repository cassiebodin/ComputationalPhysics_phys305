#Cassandra Bodin
#Phys305
#Lecture 8 problem 1
#euler method

import numpy as np
import matplotlib.pyplot as plt

def f(T):
    return (-K*(T-T_out))

T = 85
T_out = 25
K=.1
h=1e-5

for t in np.arange(0,15,h):
    T+=h*f(T)

x=np.linspace(0,15,h)
y=
print(T)



    
