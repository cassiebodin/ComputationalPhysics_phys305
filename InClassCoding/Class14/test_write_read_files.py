import numpy as np
import math
import matplotlib.pyplot as plt

# example of write to a file
# example of read from a file

# open the file                                                                
"""f = open('lecture_data.txt','w')
xlist = [0.,1.,2.,3.,4.,5.]
ylist = [10.,11.,12.,13.,14.,15.]

n = len(xlist)
print (n)

for i in range(n):
    f.write(str(xlist[i])+' '+str(ylist[i])+"\n")
    #f.write('{0:.2f} {0:.2f} \n'.format(xlist[i],ylist[i]))
f.close()

# note there are more elegant ways to do the above
# can use csv writer and writerows and json"""

f = open('lecture15_data.txt','r')

# more often you will use this
x = np.array([])
y = np.array([])
mylist = []
for line in f:
  s = line.split()
  x = np.append(x,float(s[0]))
  y = np.append(y,float(s[1]))

f.close()

# print some things
print (x)
print (y)


#plot 
fig, ax = plt.subplots()
ax.plot (x, y, 'b')
ax.set(title='lecture15_data', xlabel='x axis', ylabel='y axis')
ax.grid()
#fig.savefig('satellite_orbit.png') #uncomment to save

plt.show()

