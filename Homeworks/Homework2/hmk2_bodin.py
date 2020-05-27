#Cassandra Bodin
#Phys 305
#HW2 due 1/29
# run code using "python hmk2_bodin.py"

#Problem 1:use matplotlib to plot the data points of x in range [0,2] and y=exp(x) with the error bars of yerr=sqrt(y)
#run alternate program using "python bodin_plot.py"
def plotdata():
    #import the libraries numpy and matplotlib and rename them as np and plt
    import matplotlib.pyplot as plt
    import numpy as np

    # set x in the range from [0,2] with 50 steps
    x = np.linspace(0.,2.,50)
    y = np.exp(x)

    #create a figure and a set of subplots
    fig, ax = plt.subplots()

    #used abosulte value bars here so we get only real numbers, not really necessary for this problem but is a  good practice to use them 
    #make the errorbars blue with no marker or lines so we can see the individual values
    plt.errorbar (x, y, yerr = np.sqrt(abs(y)),color = 'blue',marker = "None", linestyle = 'None')

    #plots x and y in red with a regular dot and no line between them
    ax.plot (x, y, color = 'red',marker = ".", linestyle = 'None')

    #Add a title, and x and y axis labels
    ax.set(title='Exponential Plot', xlabel='x axis', ylabel='y axis')


    # ads a grid to the graph
    ax.grid()

    #saves the figure as exp.png
    fig.savefig("exp.png")

    #plt.show() #uncomment this if you wanted to show the plot
#plotdata() #to call program uncomment

#Problem 2:use bisector method to find the first 2 positive roots of bessel function j(x)=(np.sin(x)/x**2)-(np.cos(x)/x). Use convergence of <1e-6
#run alternate program using "python bodin_bessel.py"

#see plot_quintic.py for sample bisector method problem

def bessel():
    import numpy as np
    import math
    
    #define besel function
    def j(x):
        return (np.sin(x)/x**2)-(np.cos(x)/x)
    i=1
# first root lies somewhere between 1 and 5
    a=1.
    b=5.
# second root lies somewhere between 6 and 8
    c=6.
    d=8.
    #initiate the first while loop for the bisector method for the first root
    while (abs((b-a))>1e-6):
        i+=1
        #midpoint
        mid = (a+b)/2
        if ((j(a)*j(mid))< 0):
            a=a
            b= mid
        else:
            a = mid
            b=b
    print(a)
 #initiate the second while loop for the bisector method for the second root
    while (abs((d-c))>1e-6) and (a!=c):
        i+=1
        #midpoint
        mid = (c+d)/2
        if ((j(c)*j(mid))< 0):
            c=c
            d= mid
        else:
            c = mid
            d=d
    print(c)

#bessel() #uncomment to call program

#Problem 3:Calculate the position of L2. M = mass of Sun. m = mass of Earth. R = distance between center of sun and center of Earth (1AU). r = distance from center of sun to L2. G is gravitational const. w is angular velocity of Earth and satellite around the Sun. Equation is (G*M/r**2)+(G*m/((r-R)**2)) = w**2*r. Use Newton - Raphson method to find the distance r of L2. Use convergence of <1e-6. Use GM=4(np.pi)**2 and stay in AU. R = 1AU

#Note: Find Gm in AU
#see bodin_newton_raphson.py for sample newton-raphson problem

def lagrange():
    import math
    import numpy as np

    r = 2.
    GM = 4*(math.pi)**2
    Gm = 4 *(math.pi)**2*3*1e-6
    R = 1.
    w = 2*math.pi
#write as a function of r 
    def f(r):
        return ((1/r**2)+(3e-6/((r-1)**2)) - 1*r )
# find the first derivative of f(r)
    def f_1(r):
        return ((-2/r**3)-(3/(500000*(r-1)**3))-1)

#while loop to initiate newton-raphson method
    while (abs(f(r)) > 10**-6):
        r = r - (f(r)/f_1(r))
    print(r)    
lagrange() #uncomment to call program

#has this error still not sure how to fix ZeroDivisionError: float division by zero



#Problem 4: program calculates the submerged depth (H) of a spherical ball of density p_ball= .25gcm^-3 fl floating in water of density p_water=1 gcm^-3. radius (r)=10cm. H is in range [0cm,20cm]. Use Archimedes principle and root finding to solve.

#archimedes principle p_water*V_water*g = p_ball*V_ball*g
#V_ball = 4*pi*r**2/3
#V_water = pi*(3*r*(H**2)-H**3)/3
# substituting and rearranging H**3-3*r*(H**2)+4*p_ball*(r**3)

def float():
    import math
    import numpy as np

# my guess based on graphing the function for a root of H in range [0,20] is 7
    H = 7.
#starting point
    i=0.
#values of known variables
    p_ball= .25
    r=10.

#define the function 
    def f(H):
        return H**3-3*r*(H**2)+4*p_ball*(r**3) 
#1st derivative of the function
    def f_1(H):
        return 3*H*(H-2*r)
#while loop to initiate newton-raphson method
    while (f(H) < 1e-6):
        H = H - (f(H)/f_1(H))
        i+=1
        print(H)
#beak the while loop so it doesn't keep cycling
        break
  
#float() #uncomment to call program
