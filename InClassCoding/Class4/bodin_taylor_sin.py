#Cassandra Bodin
#Phys305
#HW1 Problem 4
#run code by "python bodin_taylor_sin.py"

#import math library
import math

#name a value x that the user inputs
x = float(input (" Enter a value for x: "))
#set y = sin(x)
#round to the 10th decimal space
y= round(math.sin(x), 10)

print ("sin(x)=" ,y)

#beginning values
taylor = 0
n = 0

print("The values of the taylor series for sin(x) are:")
#while loop that will output the value of the taylor expantion for every iteration until it equals y
while (round(taylor,10) != y):
    #this is the sum for the taylor series of sin(x), += adds the previous values to the one from the current iteration
    taylor += (math.pow(-1,n)*math.pow(x,2*n+1))/(math.factorial(2*n+1))
    #n starts at 1 and increases by 1 every iteration
    n = n+1
    print (round(taylor,10))


