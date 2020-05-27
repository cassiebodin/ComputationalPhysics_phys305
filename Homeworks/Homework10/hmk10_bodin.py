#Cassandra Bodin
#Phys305
#Homework 10

#run with "python hmk10_bodin.py"


#Problem 1: 2 dice, 1 red and 1 blue, each with 6 sides (1-6 dots per side). throw both dice money += -1, if red>blue then money = +2.3, else money+=0
#test_random.py

def Problem1():

    import numpy as np
    import random
    import math
    import matplotlib as plt

    random.seed()

    R_sides = 6
    B_sides = 6
    numTrials = 100 #10 #20 #50 #100 #1000 #change depending on how many trials you want
    money_0 =10 # start with $10
    money = money_0
    win = 2.3 #2.3 #1.5 #3 #changing the money changes the likelihood of winning
    loose = 1

    for trial in range(numTrials+1):
        print ("money before trial ", trial, "  was: $" + "{:.2f}".format( money))
        R=random.randint(1,6) #choose a random number from 1-6 for the red die, print result
        print("R is ",R)

        B=random.randint(1,6)#choose a random number from 1-6 for the blue die, print result
        print("B is ",B)

#if else statements for winning or loosing money (win then +1.3, loose the -1)
        if (R>B):
            money += (win-loose)
        elif (R<=B):
            money+= -loose
        trial+=1
#for kicks and giggles....
        if money>0:
            print("ROLL THOSE DICE!!!!!")
        elif money == 0:
            print ("All fun and games until you've run out of money")
        elif money<0:
            print("You're going into a hole you cant climb out of...")
#if else statements that tell you if you made a profit or not
    if (money>money_0):
        print("You made a profit")
    elif (money<money_0):
        print("You lost money")
    elif (money==money_0):
        print("You broke even")
#print how much money you end up with
    print("total money = $ " + "{:.2f}".format( money))
Problem1()

#print("___________________________________________________________________")

#Problem 2: hit or miss methos for I= integral (0,2) of (np.sin(1/(x(2-x)))**2 dx
#hit_or_miss.py as base code
def Problem2():

    import numpy as np
    import random
    import math
    import matplotlib.pyplot as plt

#define the function
    def f(x):
        return (np.sin(1/(x*(2-x)))**2)

#intitial values
    fmax = 1 #max value of a sine function is 1
    a = 0
    b=2
    Ntotal = 1000
    Nunder=0

#values for graphing
    xarr=[]
    yarr=[]
    fxarr=np.linspace(0,2,1000)
    fyarr=np.array([f(x) for x in fxarr])

#for loop for hit or miss method
    for i in range(Ntotal):
        r1 = random.random()
        r2 = random.random()
        x = a + r1*(b-a)
        y=r2*fmax
        xarr.append(x)
        yarr.append(y)

        if  y < f(x):
            Nunder+=1
#find I and print values
    I=(Nunder/Ntotal)*(b-a)*fmax
    print(I)

#plot both dots from x and y values and plot of the function
    fig,ax=plt.subplots()
    ax.plot(xarr,yarr,'b.')
    ax.plot(fxarr,fyarr,'r')
    ax.set(title='Hit-or-Miss', xlabel='xarr', ylabel='yarr')
    ax.grid()
    plt.savefig("HitorMiss.png")
    plt.show()
                    
Problem2()

#print("___________________________________________________________________")

#Problem 3:random walk starting at the center of  a circle. Find number of steps it takes to escape circle
#ran_walk_2d_class.py

def Problem3():
    import matplotlib.pyplot as plt
    import numpy as np
    import random
    import math

    random.seed()
    ntrials = 10
    nwalks = 10
    nsteps = 100000
    MFP = .1 #mean free path
    r_circle= 10 #radius of circle
    d = np.array([])
    d2 = np.array([])

    ichoose = 0

    if ichoose == 0:
        fig, ax = plt.subplots()
    else:
        fig, ax = plt.subplots(1,2)

    for iwalk in range(nwalks):

        xpos = 0
        ypos = 0
        rpos = 0
        nstep = np.array([])
        xarr = np.array([])
        yarr = np.array([])
        nstep = np.append(nstep,0)
        xarr = np.append(xarr,xpos)
        yarr = np.append(yarr,ypos)

        count = 1 
        xpos = 0
        ypos = 0
        d2pos = 0
 
        for step in range(nsteps):

#generate theta between 0 and 2pi
            theta = 2*np.pi*random.random()

            xpoint= MFP * np.cos(theta)
            ypoint= MFP * np.sin(theta)

#normalize these so the length of the step is 1
            xnorm = xpoint/ np.sqrt(xpoint**2+ypoint**2)
            ynorm = ypoint/ np.sqrt(xpoint**2+ypoint**2)

#add xnorm to xpos, ynorm to ypos
            xpos +=xnorm
            ypos +=ynorm
            
            r=np.sqrt(xpos**2 + ypos**2)

            count += 1
            xarr = np.append(xarr,xpos) #append xpos to the xarr array
            yarr = np.append(yarr,ypos) #append ypos to the yarr array
            nstep = np.append(nstep,count) #append count to the nstep array

#conditions for reaching the edge of the circle
            if r >=r_circle:
                break
            else:
                continue

        if ichoose == 0:
            ax.plot(xarr,yarr,'r')

        d = np.append(d,xpos)
        d2 = np.append(d2,(xpos**2+ypos**2))
           
#print the average amount of steps it takes to reach the edge of the circle
    print("the average number of steps is "+"{:.0f}".format( np.average(nstep)))

#graph it just because it lpoks cool
    if ichoose == 0:
        circle = plt.Circle((0, 0), 10)
        ax.set(title='title', xlabel='steps', ylabel='distance')
        ax.set_xlim(-15.,15.)
        ax.set_ylim(-15.,15.)
        ax.add_artist(circle)
        ax.grid()
        plt.savefig("circlewalks.png")
        plt.show()
    elif ichoose == 1:
        ax[0].hist(d, bins=50, range=(-15.,15.), histtype='step')      
        ax[0].set(title='title', xlabel='xpos', ylabel='number')               
        ax[0].grid()

        print (np.mean(d2))
        ax[1].hist(d2, bins=50, range=(0.,1000.), histtype='step')
        ax[1].set(title='title', xlabel='displacement**2', ylabel='number')
        ax[1].grid()

        plt.savefig("circlewalks.png")
        plt.show()
Problem3()
