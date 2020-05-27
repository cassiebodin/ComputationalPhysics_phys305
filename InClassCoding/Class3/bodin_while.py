#Cassandra Bodin
#phys 305
# run as "python bodin_while.py"

#
n= 0.
epsilon=1.
sum = 0.

#while loop that sets sum = 1. + epsilon ; epsilon = 1, 1/2, 1/4, 1/8, ...
#continue loop until sum = 1.

while sum != 1.:
    epsilon = (1./2**(n))
    sum= 1.+ epsilon
    n= n+1
#print loop index, epsilon, and sum
    #print("%s %s %s" %(n,epsilon,sum))
    print(n,sum,epsilon)
print("")
