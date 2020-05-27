def Problem1():
#import libraries
    import numpy as np
    import matplotlib.pyplot as plt

#euler method
    def Euler1():
        def f(T,t):
            return (-K*(T-T_out))

#initial parameters
        T = 85
        T_out = 25
        K=.1
        t=0
#set up parameters for graph
        xarr = [] 
        yarr =[]

#step size 1
        h = 1e-1
        
        for t in np.arange(0,15,h):
#rest of loop for euler method
            T+=h*f(T,t)
#piece of loop for graphing
        xarr.append(h)
        yarr.append(T)
        print("for step size h=", h," After 15 sec T =",T)
        
        h = 1e-2
        T = 85
        for t in np.arange(0,15,h):
#rest of loop for euler method
            T+=h*f(T,t)
#piece of loop for graphing
        xarr.append(h)
        yarr.append(T)
        print("for step size h=", h," After 15 sec T =",T)
        
        h = 1e-3
        T = 85
        for t in np.arange(0,15,h):
#rest of loop for euler method
            T+=h*f(T,t)
#piece of loop for graphing
        xarr.append(h)
        yarr.append(T)
        print("for step size h=", h," After 15 sec T =",T)

        h = 1e-4
        T = 85
        for t in np.arange(0,15,h):
#rest of loop for euler method
            T+=h*f(T,t)
#piece of loop for graphing
        xarr.append(h)
        yarr.append(T)
        print("for step size h=", h," After 15 sec T =",T)

        h = 1e-5
        T = 85
        for t in np.arange(0,15,h):
#rest of loop for euler method
            T+=h*f(T,t)
#piece of loop for graphing
        xarr.append(h)
        yarr.append(T)
        print("for step size h=", h," After 15 sec T =",T)


#now plot
        fig, ax = plt.subplots()

        #ax.plot (xarr,yarr,'red',linestyle='-', marker=',')
        #set both to a log scale
        ax.loglog(xarr,yarr,'red',linestyle='-', marker=',')

        ax.set(title='Euler', xlabel='log(h)', ylabel='log(T)')


        #other way? 
        #ax.set_yscale('log')
        #ax.set_xscale('log')

        #add a grid
        ax.grid()

        fig.savefig('euler1.png')  # uncomment to save plot

        plt.show()
    
    Euler1()
    

Problem1()
