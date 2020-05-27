x = input("enter a number: ")
print x
x = x + 1
print x
x = input("enter a number: ")
print x
x = x + " thanks"
print x

# the use of raw_input is recommended over input
# raw_input interprets all input as a string
# and then you must convert it into the type you need

y = raw_input('Enter your age ')
print y
print y*2
iy = int(y)
print iy*2

# a more sophisticated version of raw_input
while True:
    strPedestal = raw_input('Enter the pedestal as an integer: ')
    ### error handling for input type
    try:
        ### convert string into integer 
        intPedestal = int(strPedestal)
        break
    ### jumps here if the string was not an integer
    except ValueError:
        print("\nYou entered an invalid input. Your input must be an integer.")
print "the pedestal is ",intPedestal

"""
the try: and except: blocks are used to test for exceptions and handle
them
"""
