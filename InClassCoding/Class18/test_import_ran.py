import math
import random
import numpy as np
import matplotlib.pyplot as plt

# some examples with random

# no argument uses current time as seed
random.seed()
arr = [] 
print (type(arr))
for i  in range(5):
    x = random.random()
    arr.append(x)
print (arr)
print (' ')

arr = []
random.seed(41)
for i  in range(5):
    x = random.random()
    arr.append(x)
print (arr)
print (' ')

arr = []
random.seed(41)
for i  in range(5):
    x = random.random()
    arr.append(x)
print (arr)
print (' ')

arr = []
for i in range(5):
    x = random.uniform(-1.,1.)
    arr.append(x)
print (arr)
print (' ')

arr = []
for i in range(5):
    x = random.randint(0,10)
    arr.append(x)
print (arr)
print (' ')    

arr = []
for i in range(5):
    x = random.gauss(10.,2.)
    arr.append(x)
print (arr)
print (' ')

