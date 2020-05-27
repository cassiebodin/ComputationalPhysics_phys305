import math
import random
import numpy as np
import datetime
import matplotlib.pyplot as plt

# some examples with random
for i  in range(5):
    x = random.random()
    print x
print ""

for i in range(5):
    x = random.uniform(-1.,1.)
    print x
print ""

for i in range(5):
    x = random.gauss(10.,2.)
    print x
print ""    
