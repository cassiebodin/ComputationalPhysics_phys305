import random
import numpy as np
import math

d=10 #number of dimensions
total=10000 #number of iterations
inside = 0

for i in range(0,total):
    x1=random.random()
    x2=random.random()
    x3=random.random()
    x4=random.random()
    x5=random.random()
    x6=random.random()
    x7=random.random()
    x8=random.random()
    x9=random.random()
    x10=random.random()
    r=math.sqrt(x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2+x8**2+x9**2+x10**2)
    if r<= 1:
        inside+=1
volume= (2**d)*(inside/total)
print(volume)
