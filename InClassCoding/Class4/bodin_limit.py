#Cassandra Bodin
#Phys305
#HW1 Problem 3
#run using "python bodin_limit.py"

import math
import numpy as np


for x in range(-900,0,40):#used this to find the minimum positive value
#for x in range(36,709,20): #uncomment this out and comment out other for loop to find max value
    x+=1
    y = math.exp(x)
    print(y)

#There is no minimum negative value for this function
#I couldn't figure out how to get it to just output a max and min value.I tried using if else statements and return y and then using max() min() but I couldn't get it to work. This at least got a number after I played with it for a while. 




