#Cassandra Bodin
#Phys 305
# in class problem lecture 6

#calculate integral of f(x) = x**2 from [0,10] using LHR, Mid-Rule, Trap-Rule, Simp-Rule

import numpy as np

def f(x):
    return x**2
n = 1000
a = 0.
b = 10.
h = abs(float(b-a)/n)
x = 0.

#left hand rule
def LHR():
    A = 0.
    for i in range(0,n):
        x=i*h
        A += h*f(x)
        
    print (A)
LHR()

#midpoint rule
def Mid():
    A = 0.
    for i in range(0,n):
        x=i*h
        x_1=(i+1)*h
        A += h*(f((x+x_1)/2))
    print (A)

Mid()

def Trap():
    A = 0.
    for i in range(0,n):
        x=i*h
        x_1= (i-1)*h
        A += h * (f(x_1)+f(x))/2
    print(A)
Trap()

def Simp():
    A = 0.
    x = list()
    fx = list()
    i= 0
    while i<=n:
        x.append(a+i*h)
        fx.append(f(x[i]))
        i+=1
    result = 0
    i=0
    while i<=n:
        if i ==0 or i ==n:
            result+= fx[i]
        elif i %2!= 0:
            result+= 4*fx[i]
        else:
            result+= 2*fx[i]
        i+=1
    result = result*(h/3)
    print (result)
Simp()
