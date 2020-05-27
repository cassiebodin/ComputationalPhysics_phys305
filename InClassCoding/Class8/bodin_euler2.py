#Cassandra Bodin
#Phys305
#Lecture 8 problem 1
#euler method

import numpy as np

def f(T1, T_o, K1):
    return (-K1*(T1-T_o))

T = 85
T_out = 25
Tf=75
K=.1
t=0
h=1e-4


while (T>Tf):
    T+=h*f(T,T_out,K)
    t+=h
print(t)


    
