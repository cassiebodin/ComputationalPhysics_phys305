# examples of functions

#  this is a basic function definition
def KE(mass, velocity):
    KE = 0.5 * mass * velocity * velocity
    mass = 100.
    return KE

# pay attention to the value of mass
# note the value of mass is not changed
mass = 10.
velocity = 2.
x = KE(mass,velocity)
print mass, velocity, x
print ""

# using default values is useful since it can be called with fewer arguments
def KE2(mass = 1., velocity = 2.):
    KE2 = 0.5 * mass * velocity * velocity
    return KE2

print KE2()
print KE2(10.)
print KE2(10.,4.)
print ""

# lists can be returned from functions 
def myfun(a,mylist=[]):
    mylist.append(a)
    return mylist

print myfun(1.)
print myfun(3.14)
print myfun(6.28)
mylist2 = myfun(10.2)
print mylist2
print ""




