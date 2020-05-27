#Cassandra Bodin
#Phys305
#run using "python bodin_duplicates.py"

#program that takes a string and find number of duplicare letters

mystring = input("input a phrase here: ")
counted = []

for i in mystring:
    if (mystring.count(i)>1) and (not i in counted):
        
        print(mystring.count(i), i)
        
    counted.append(i)

