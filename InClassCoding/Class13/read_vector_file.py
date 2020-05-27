import numpy as np
import math


f = open('vector_data.txt','r')

# read one line
# only sometimes will you use this
line1 = f.readline().split()
line2 = f.readline().split()
print(line1,line2)

for i in range(len(line1)):
    line1[i]=float(line1[i])
print(line1)

for s in range(len(line2)):
    line2[s]=float(line2[s])
print(line2)


f.close()

print(np.cross(line1,line2))

# print some things



