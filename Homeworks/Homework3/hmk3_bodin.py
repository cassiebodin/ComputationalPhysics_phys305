#Cassandra Bodin
#Phys 305
#Homework 3
#due 2/5

#Problem 1: P(v)=C*v**2*math.exp((-M*v**2)/(2*k*T)). The integral from[o,inf] of P(v)=1. C is normalization const, M is mass of molecule, k is Boltz const, T is temp. Use Simpsons Rule to find C in terms of M,k,T. Note (will need to do a straight forward variable change to do this numerically

#used bodin_integration.py as a reference for Simpson's rule

def Maxwell():
    import numpy as np
    import math

    def P(z):
# since P(v) = 1 (probability) pulled the C out so we can find it using 1/A
# v=z*math.sqrt((2*k*T)/M) declared function so we can pull out the variables,replace wherever there was a v before. now a function of P(z)
        return (z**2*(math.exp((-z**2)))) #without constants M,k,T

#define start values and bounds for the function
    n = 1000 #number of slices
    a = 0 #starting point
    b = 100 #ending point as ->infinity
    h = (b-a)/n #slice size
    x = list() #list of x values
    Px = list() #list of P(x) values
    i= 0 #starting point for i
    while i<=n:#calculate values of x and P(x)
        x.append(a+i*h)
        Px.append(P(x[i]))
        i+=1
    A = 0
    i=0
    while i<=n: #loop to find expression parts
        if i ==0 or i ==n: #1st part
            A+= Px[i]
        elif i %2!= 0: #2nd part
            A+= 4*Px[i]
        else: #otherwise 3rd part
            A+= 2*Px[i]
        i+=1
    A = A*(h/3) # Simpson's rule
    print ("C =1/(",A,"*(2kT/M))")
Maxwell()#uncomment to call function

#A should be about 0.443113462726379
#A we got 0.44311346272637886

#Problem 2: Gaussian probability function p(x) = math.exp((x-mu)**2/((-2)*sigma**2))/math.sqrt(2*math.pi*sigma). mu = 0 , sigma = 1. Integrate using trapezoidal rule between [-1,1], [-2,2], [-3,3], [-5,5]

def Gaussian():
    import math
    import numpy as np
    def p(x):
        return (math.exp((x)**2/(-2))/math.sqrt(2*math.pi))
    def trap(a,b):
        n = 1000
        h = abs(float(b-a)/n)
        x = 0.
        A =.5*p(a)+.5*p(b)
        for i in range(0,n):
            A +=p(a +i*h)
        A*=h
        return A
    print(trap(-1,1))
    print(trap(-2,2))
    print(trap(-3,3))
    print(trap(-5,5))
    #print(trap(-10,10)) # for abs(a, b)>5


Gaussian()#uncomment to call function

#outputs [0.683173272272287,0.9547154120179498,0.9973267152542261,0.9999994414401643]

#Problem 3: T_approx= 2*math.pi*math.sqrt(L/g). Integrate T = 4math.sqrt(L/g)inegral(0,2math.pi)dphi/math.sqrt(1-k**2*math.sin(phi/2)**2) for theta_0 from [0,60]. Put resulting T in a table, with T/T_approx for ea theta_0
def Pendulum():
    import numpy as np
    import math

    def T(phi):
        return ((4*math.sqrt(1/9.8))*1/(1-(k**2)*(math.sin(phi/2)**2)))
    L = 1
    g = 9.8
#theta is from 0-60degrees so choose a value s to be that range of numbers
    for s in range(0,61,10):
        theta = s*math.pi/180 #convert to radians
        k = math.sin(theta/2)
        n = 1000 #number of slices
        a = 0 #starting point
        b = math.pi/2 #ending point 
        h = (b-a)/n #slice size

        phi = list() #list of phi values
        Tphi = list() #list of T(phi) values
        i= 0 #starting point for i
        while i<=n: #calculate values of phi and T(phi)
            phi.append(a+i*h)
            Tphi.append(T(phi[i]))
            i+=1
        A = 0
        i=0
        while i<=n: #loop to find expression parts
            if i ==0 or i ==n: #1st part
                A+= Tphi[i]
            elif i %2!= 0: #2nd part
                A+= 4*Tphi[i]
            else: #otherwise 3rd part
                A+= 2*Tphi[i]
            i+=1
        A = A*(h/3) # Simpson's rule
        print("period=",A)
Pendulum()



#Problem 4: write a program to calculate integral [0,2] of x**5+2*x**2 using mid,trap, simp. Make a table of the results for each method using bins 2,4,6,16..2^20. What is the analytical result of integral?
#make plot of log(abs(observed-correct)) vs log(number of intervals) for ea method
#use plot to deduce power of the step size the error scales as. error~stepsize**p where p is the power that we find via slope of the line

def problem4():
#import the libraries that might be useful for this program
    import numpy as np
    import math
    import matplotlib.pyplot as plt

#define the function
    def f(x):
        return x**5+2*x**2
#number of bins
    n= 1000
#range [0,2]
    a = 0.
    b = 2.
#define h
    h = abs(float(b-a)/n)
#starting point of x
    x = 0.
 #correct value of A
    correct = 16.
#midpoint rule
    def Mid():
        A = 0.
        for i in range(0,n):
            x=i*h
            x_1=(i+1)*h
            A += h*(f((x+x_1)/2))            
        print(A)
#graph it
        #r = np.linspace(0.,2.,h)
        #s = abs(A-correct)

        #fig, ax = plt.subplots()

#ax.plot(time, amplitude, color='red', marker='.', linestyle='none')
        #ax.plot (np.log(r), np.log(s), 'b')

        #ax.set(title='midpoint', xlabel='number of bins', ylabel='abs(result-correct)')

# not needed, is just a useful flair
        #ax.grid()

        #fig.savefig("mid.png")

        #plt.show()
    Mid()

#trapezoidal rule
    def Trap():
            
        h = abs(float(b-a)/n)
        x = 0.
        Area =.5*f(a)+.5*f(b)
        for i in range(0,n):
            Area +=f(a +i*h)
        Area*=h
        print(Area)
#graph
        #r = np.linspace(0.,2.,h)
        #s = abs(Area-correct)

        #fig, ax = plt.subplots()

#ax.plot(time, amplitude, color='red', marker='.', linestyle='none')
        #ax.plot (np.log(r), np.log(s), 'b')

        #ax.set(title='midpoint', xlabel='number of bins', ylabel='abs(result-correct)')

# not needed, is just a useful flair
        #ax.grid()

        #fig.savefig("trap.png")

        #plt.show()

    Trap()
#simpson's rule
   
    def Simp():
        h = (b-a)/n
        x = list()
        fx = list()
        i= 0
        while i<=n:
            x.append(a+i*h)
            fx.append(f(x[i]))
            i+=1
        result = 0
        i=0
        while i<=n:
            if i ==0 or i ==n:
                result+= fx[i]
            elif i %2!= 0:
                result+= 4*fx[i]
            else:
                result+= 2*fx[i]
            i+=1
        result = result*(h/3)
        print (result)
#graph
        #r = np.linspace(0.,2.,h)
        #s = abs(Area-correct)

        #fig, ax = plt.subplots()

#ax.plot(time, amplitude, color='red', marker='.', linestyle='none')
        #ax.plot (np.log(r), np.log(s), 'b')

        #ax.set(title='midpoint', xlabel='number of bins', ylabel='abs(result-correct)')

# not needed, is just a useful flair
        #ax.grid()

        #fig.savefig("trap.png")

        #plt.show()
    Simp()
problem4()

#outputs [15.999985333338003,16.000029333328, 16.000000000021334]
#actual = 16

#couldn't figure out how to do the graphing portion. If you comment out that text it gives the outputs above(currently done in code). When you uncomment it it breaks.
