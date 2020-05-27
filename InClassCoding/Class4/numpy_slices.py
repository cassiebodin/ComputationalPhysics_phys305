import numpy as np
import matplotlib.pyplot as plt


# some examples with numpy
# numpy is a basic scientific library for python

# basic array definition
a = np.array([0,1,2,3,4,5,6,7,8,9])
print (type(a))

#  [start index : stop index : step]
#  the first index is 0
#  the stop index is not included
#  - means count from the end of the array
#  no element is a default

a = np.array([0,1,2,3,4,5,6,7,8,9])

print (type(a))

print (a[0])

print (a[9])

print (a[2:5])

print (a[1:10:2])

print (a[-3])

print (a[-3:3])

print (a[-3:3:-1])

print (a[5:])

print (a[:-1])
