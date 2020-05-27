# examples of for loops
# note the :
# note that blocks of code are determined by line indentation

for i in range(10):
    print (i)    
print ("")

for i in range (5,10):
    print (i)
print ("")

for i in range(0,10,2):
    print (i)
print ("")

# [] is a python list
for i in ["green","eggs",1,2,3]:
    print (i)
print ("")

# note continue and break have the same use as in c

for i in ["green","eggs",1,2,3]:
    if (i == 1): break
    print (i)
print ("")

for i in ["green","eggs",1,2,3]:
    if (i == "eggs"): continue                                                 
    print (i) 
