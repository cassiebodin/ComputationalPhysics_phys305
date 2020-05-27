#Cassandra Bodin
#Phys 305
#Lecture 9: Runge Kutta 2
#run with " bodin_rungekutta.py

import numpy as np
import matplotlib.pyplot as plt

def f(v,t):
    return -9.8
def g(y,t):
    return v
t1 =0.
t2 = 10.
h= 1e-4

v=0
t=t1
y1=0
y=30

while (y>y1):
    k1=h*f(v,t)
    k2=h*f(v+k1/2,t+h/2)
    v+=k2

    k3=h*g(y,t)
    k4=h*g(y+k3/2,t+h/2)
    y+=k4
    t+=h
print ("at y =",y,"t =", t-h)

