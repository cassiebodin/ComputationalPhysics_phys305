#Cassandra Bodin
#Phys 305
#HW1 due 1/22
# run code using "python hmk1_bodin.py" or run each problem's individual code using the given program names

#used geeksforgeeks.org and codesdope.com as a reference when writing code

#PROBLEM 1 : write a program that finds prime numbers [1,30]
#run code by "python bodin_prime.py"

#starting point
start = 1
#ending point
end =  30
print("prime numbers between 1 and 30")
#for a number (num) in the range [1,30]
for num in range(start,end +1):
    count = 0
#i is a number between 2 and num divided by 2 +1. If num is divisible by i or 2 then the loop breaks and it isn't prime. 
    for i in range (2,num//2 +1):
        if (num %i == 0):
            count = count +1
            break
#If it isn't divisible by i or 2 then it prints the value of num. Num should be prime
    if (count == 0 and num !=1):
        print("%d" %num)



print("_________________________________________________")

#PROBLEM 2 : write a progtam that 1) sorts a list from max-min values
#            2)shows how to sorta numpy array from max to min values
#            3) creates a function that sorts 5 items from max to min using selection sort
#run code by "python bodin_sort.py"

#import numpy and label it as np
import numpy as np

#Part 1: sorts a list from max - min values (descending order)

#make an arbitrary list of values called 'list' and write as an array
list = [1,8,6,5,3]
print("my first list" ,list)
#use list.sort to sort them in ascending order, add reverse=true to change to descending order
list.sort(reverse = True)
print("my sorted first list",list)

# Part 2: uses a numpy array to sort a list from max- min (descending order)

#make a new list, this time a numpy array
new_list = np.array([2,8,6,9,1,3])
print("my second list:" ,new_list)
#sort the list in ascending order
sorted_new_list = np.sort(new_list)
#to get in descending order have to reverse it
reverse_new_list = sorted_new_list[::-1]
print("my sorted second list:", reverse_new_list)

#Part 3: sorts 5 items from max to min using selection sort

#make a new array with 5 elements
newer_list = [12,5,4,1,23]
print("my third list:", newer_list)
#use a while loop to cycle through the elements in the array
i=0
while i<len(newer_list):
    #finds smallest element in what is left of the list
    small = min(newer_list[i:])
    #finds the index of the smallest element in what is left of the list
    index_of_small = newer_list.index(small)
    #swaps the smallest element with the first element in what is left in the list
    newer_list[i],newer_list[index_of_small] = newer_list[index_of_small],newer_list[i]
    i = i+1
#reverse the list so it is from max to min instead of min to max
reverse_newer_list = newer_list[::-1]
print("my sorted third list", reverse_newer_list)

print("_________________________________________________")
#Problem 3 : write a program to explore the range of numbers that can be represented by a float. Find largest (+) number, smallest (-) number, and smallest (+) number
#run code by "python bodin_limit.py"

#import math library
import math


for x in range(-900,0,40):#used this to find the minimum positive value
#for x in range(36,709,20): #uncomment this out and comment out other for loop to find max value
    x+=1
    y = math.exp(x)
    print(y)

#There is no minimum negative value for this function
#I couldn't figure out how to get it to just output a max and min value.I tried using if else statements and return y and then using max() min() but I couldn't get it to work. This at least got a number after I played with it for a while. #import math and numpy libraries


print("_________________________________________________")
#Problem 4 : Write a program that inputs a user value x then calculates the taylor series of sin(x). Continue until taylor - sin(x) <1e-10
#run code by "python bodin_taylor_sin.py"

#import math library
import math

#name a value x that the user inputs
x = float(input (" Enter a  value for x: "))
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

#note: values entered that are too big will result in the overflow error: int too large to convert to a float. This happens at about +16or-16


