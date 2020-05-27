#Cassandra Bodin
#Phys 305
#Hw1 Problem 2
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
