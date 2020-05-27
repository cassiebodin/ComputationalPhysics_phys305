# use the math library
import math

# here we define three functions
def hello():
    name = input ("enter your name: ")
    print ('hello',name)

def square(x):
    value = x*x
    return value

def sinsquare(x):
    value = math.sin(x) * math.sin(x)
    print (value)
    return value

def odd_even():
    for i in range (1,11):
        if i%2 == 0: 
            print(i, 'even')
        else: 
            print(i, 'odd')


# and then call the functions
hello()
value = 0.
print (square(4.))
sinsquare(math.pi/6.)
odd_even()
print (value)
