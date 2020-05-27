mystring = raw_input("enter a string: ")
mylist=[]

# find the string length
length = len(mystring)

# do a for loop
for i in range(length):
    if (mystring.count(mystring[i]) > 1):
        
        #add to a list
        length2 = len(mylist)
        if length2 == 0:
             mylist.append(i)
             print mystring[i],mystring.count(mystring[i])
             continue
        # otherwise check if letter is already in list
        double = 0
        #print type(i)
        for j in range(length2):
          #print type(mylist[j])
          if mystring[i] == mystring[int(mylist[j])]:
             double += 1
        if double == 0:         
             mylist.append(i)
             print mystring[i],mystring.count(mystring[i])

