#Cassandra Bodin
#Phys 305
#Homework 4
#2/12 at midnight
#run using "python hwk4_bodin.py"

#Problem 1: Newton's Law of cooling dT/dt=-K(T(t)-T_out). Given T(0)=85 T_out=25 K=.1. Find T after 15 min using Euler,Runge Kutta 2, Runge Kutta 4.make log-log plots for each.

#Note real answer given by T(t)=T_out+(T(0)-T_out)e**(-K*t). For t=15 T(15)=38.3878096089
def Problem1():
#import libraries
    import numpy as np
    import matplotlib.pyplot as plt

    
    print("Euler")
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
        Ttrue = 38.39

#step size 1
        h = 1e-1
#loop for euler method
        for t in np.arange(0,15,h):
            T+=h*f(T,t)
#graph using value from loop
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print("for step size h=", h," After 15 sec T =",T)
        
#step size 2
        h = 1e-2
        T = 85
#loop for euler method
        for t in np.arange(0,15,h):
            T+=h*f(T,t)
#graph using value from loop
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print("for step size h=", h," After 15 sec T =",T)
        
#step size 3
        h = 1e-3
        T = 85
#loop for euler method
        for t in np.arange(0,15,h):
            T+=h*f(T,t)
#graph using value from loop
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print("for step size h=", h," After 15 sec T =",T)

#step size 4
        h = 1e-4
        T = 85
#loop for euler method
        for t in np.arange(0,15,h):
            T+=h*f(T,t)
#graph using value from loop
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print("for step size h=", h," After 15 sec T =",T)

#step size 5
        h = 1e-5
        T = 85
#loop for euler method
        for t in np.arange(0,15,h):
            T+=h*f(T,t)
#graph using value from loop
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
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

        #plt.show()
    
    Euler1()
    
    print("Runge-Kutta 2")

    def RKii1():
        import numpy as np
        import matplotlib.pyplot as plt

        def f(T,t):
            return (-K*(T-T_out))

        T = 85
        T_out = 25
        K=.1
        t=0
        Ttrue = 38.39

#set up parameters for graph
        xarr = [] 
        yarr =[]

#time step 1
        h=1e-1
#loop for rungekutta2
        while (t<15):
            k1=h*f(T,t)
            k2=h*f(T+k1/2,t+h/2)
            T+=k2
            t+=h
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print ("for step size h=", h," After 15 sec T =",T)

#time step 2
        h=1e-2
        T=85
        t=0
#loop for rungekutta2
        while (t<15):
            k1=h*f(T,t)
            k2=h*f(T+k1/2,t+h/2)
            T+=k2
            t+=h
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print ("for step size h=", h," After 15 sec T =",T)

#time step 3
        h=1e-3
        T=85
        t=0
#loop for rungekutta2
        while (t<15):
            k1=h*f(T,t)
            k2=h*f(T+k1/2,t+h/2)
            T+=k2
            t+=h
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print ("for step size h=", h," After 15 sec T =",T)

#time step 4
        h=1e-4
        T=85
        t=0
#loop for rungekutta2
        while (t<15):
            k1=h*f(T,t)
            k2=h*f(T+k1/2,t+h/2)
            T+=k2
            t+=h
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print ("for step size h=", h," After 15 sec T =",T)

#time step 5
        h=1e-5
        T=85
        t=0
#loop for rungekutta2
        while (t<15):
            k1=h*f(T,t)
            k2=h*f(T+k1/2,t+h/2)
            T+=k2
            t+=h
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print ("for step size h=", h," After 15 sec T =",T)


#now plot
        fig, ax = plt.subplots()

        #ax.plot (xarr,yarr,'red',linestyle='-', marker=',') #uncomment to see regular plot

        #plot using a log scale
        ax.loglog(xarr,yarr,'red',linestyle='-', marker=',')

        ax.set(title='Rkii1', xlabel='log(h)', ylabel='log(T)')


        #other way? 
        #ax.set_yscale('log')
        #ax.set_xscale('log')

        #add a grid
        ax.grid()

        fig.savefig('Rkii1.png')  # uncomment to save plot

        #plt.show()
        
    RKii1()
    
    print("Runge-Kutta 4")

    def RKiv1():
        import numpy as np
        import matplotlib.pyplot as plt

        def f(T,t):
            return (-K*(T-T_out))

        T = 85
        T_out = 25
        K=.1
        t=0
        Ttrue = 38.39

#set up parameters for graph
        xarr = [] 
        yarr =[]

#time step 1
        h=1e-1
#loop for rungekutta4
        while (t<15):
            k1=h*f(T,t)
            k2=h*f(T+k1/2,t+h/2)
            k3=h*f(T+k2/2,t+h/2)
            k4=h*f(T+k3,t+h)
            T+=k4
            t+=h
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print ("for step size h=", h," After 15 sec T =",T)

#time step 2
        h=1e-2
        T=85
        t=0
#loop for rungekutta4
        while (t<15):
            k1=h*f(T,t)
            k2=h*f(T+k1/2,t+h/2)
            k3=h*f(T+k2/2,t+h/2)
            k4=h*f(T+k3,t+h)
            T+=k4
            t+=h
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print ("for step size h=", h," After 15 sec T =",T)

#time step 3
        h=1e-3
        T=85
        t=0
#loop for rungekutta4
        while (t<15):
            k1=h*f(T,t)
            k2=h*f(T+k1/2,t+h/2)
            k3=h*f(T+k2/2,t+h/2)
            k4=h*f(T+k3,t+h)
            T+=k4
            t+=h
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print ("for step size h=", h," After 15 sec T =",T)

#time step 4
        h=1e-4
        T=85
        t=0
#loop for rungekutta4
        while (t<15):
            k1=h*f(T,t)
            k2=h*f(T+k1/2,t+h/2)
            k3=h*f(T+k2/2,t+h/2)
            k4=h*f(T+k3,t+h)
            T+=k4
            t+=h
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print ("for step size h=", h," After 15 sec T =",T)

#time step 5
        h=1e-5
        T=85
        t=0
#loop for rungekutta4
        while (t<15):
            k1=h*f(T,t)
            k2=h*f(T+k1/2,t+h/2)
            k3=h*f(T+k2/2,t+h/2)
            k4=h*f(T+k3,t+h)
            T+=k4
            t+=h
        xarr.append(h)
        yarr.append(abs(T-Ttrue))
        print ("for step size h=", h," After 15 sec T =",T)

#now plot
        fig, ax = plt.subplots()

        #ax.plot (xarr,yarr,'red',linestyle='-', marker=',') #uncomment to see regular plot

        #plot using a log scale
        ax.loglog(xarr,yarr,'red',linestyle='-', marker=',')

        ax.set(title='RKiv1', xlabel='log(h)', ylabel='log(T)')


        #other way? 
        #ax.set_yscale('log')
        #ax.set_xscale('log')

        #add a grid
        ax.grid()

        fig.savefig('Rkii1.png')  # uncomment to save plot

        #plt.show()
        
    RKiv1()
#plot the graphs
    plt.show('all')
Problem1() #uncomment to call problem 1




#Problem 2: Radioactive decay dN/dt=N/tau, t_half=tau*np.log(2) -->tau=t_half/np.log(2). t_half=5730. 80bc-now is about 2098yrs
def Problem2():
    def RKii2():
        import numpy as np

        def f(N,t):
            return (-N/(5730/np.log(2)))

#initial values
        t1 = 0
        t2 = 2098
        t_half = 5730
        h=1e-2
        N1 = 100

        t = t1
        N=N1


        while (t<t2):
            k1=h*f(N,t)
            k2=h*f(N+k1/2,t+h/2)
            N+=k2
            t+=h
        print("the fraction of the nucleus after 2098yrs is:",N/N1)
                
    RKii2()
Problem2()#uncomment to call function




#Problem 3:Use Runge-kutta method for falling body w/ quadratic drag and w/o drag
#y1=30, v=0, vterm=11

def Problem3():

#for no drag
    def nodrag():
        import numpy as np

        def f(v,t):
            return -9.8
        def g(y,t):
            return v

        t1 =0.
        h= 1e-5

        v=0
        t=t1
        y1=0
        y=30

        while (y>y1):
            k1=h*f(v,t)
            k2=h*f(v+k1/2,t+h/2)
            v+=k2

            k3=h*g(y,t)
            k4=h*g(y+k3/2,t+h/2)
            y+=k4
            t+=h
        print ("Without drag: at y =",y,"t =", t-h)
    nodrag()

#for quadratic drag
    def drag():
        import numpy as np

        def f(v,t):
#dv/dt=-g+(g/vterm**2)*v(t)**2
            return -9.8 +(9.8/11**2)*v**2
        def g(y,t):
            return v

        t1 =0.
        h= 1e-5

        v=0
        t=t1
        y1=0
        y=30

        while (y>y1):
            k1=h*f(v,t)
            k2=h*f(v+k1/2,t+h/2)
            v+=k2

            k3=h*g(y,t)
            k4=h*g(y+k3/2,t+h/2)
            y+=k4
            t+=h
        print ("With drag: at y =",y,"t =", t-h)
    drag()
Problem3() #to call function uncomment




#Problem 4: Baseball. v0=50, theta =35, vterm=42, x0=0, y0=2. Use Euler method to make a plot of trajectory of ball until y=0. 
def Problem4():
#import libraries
    import numpy as np
    import matplotlib.pyplot as plt

    def nodrag():
#for x dv_y/dt=-g+(g/vterm**2)*v*vx
        #vx1v*np.cos(theta) theta =35 v=50
        def fx(vx,t):
            return 0
#for y dv_x/dt=-g+(g/vterm**2)*v*vy
        def fy(vy,t):
            return -9.8 

#for dx/dt
        def gx(x,t):
            return vx
#for dy/dt
        def gy(y,t):
            return vy

        t1 =0.
        h= 1e-2

        vx1=40.9576
        vy1=28.6788
        y1=2
        x1=0
        
        t = t1
        vx = vx1
        vy = vy1
        x=x1
        y=y1

#set up parameters for graph
        xarr,yarr = [],[]

#Euler method for vx, x
        while (y>0):
            vx+=h*fx(vx,t)
            x+=h*gx(x,t)
  
            vy+=h*fy(vy,t)
            y+=h*gy(y,t)
            t+=h

            xarr.append(x)
            yarr.append(y)
        print("for baseball without drag",x,y,t)

        fig, ax = plt.subplots()

        ax.plot (xarr,yarr,'red',linestyle='-', marker=',')

        ax.set(title='Baseball-nodrag', xlabel='x', ylabel='y')


        #add a grid
        ax.grid()

        fig.savefig('baseball nodrag.png')  # uncomment to save plot

        #plt.show()
    
    nodrag()

#euler method for drag
    def drag():
#for x dv_y/dt=-g+(g/vterm**2)*v*vx
        #vx1v*np.cos(theta) theta =35 v=50
        def fx(vx,t):
            return (9.8/11**2)*((vx**2+vy**2)**(1/2))*vx
#for y dv_x/dt=-g+(g/vterm**2)*v*vy
        def fy(vy,t):
            return -9.8 +(9.8/11**2)*((vx**2+vy**2)**(1/2))*vy

#for dx/dt
        def gx(x,t):
            return vx
#for dy/dt
        def gy(y,t):
            return vy

        t1 =0.
        h= 1e-2

        vx1=40.9576
        vy1=28.6788
        y1=2
        x1=0
        
        t = t1
        vx = vx1
        vy = vy1
        x=x1
        y=y1

#set up parameters for graph
        xarr,yarr = [],[]

#Euler method for vx, x
        while (y>0):
            vx+=h*fx(vx,t)
            x+=h*gx(x,t)
  
            vy+=h*fy(vy,t)
            y+=h*gy(y,t)
            t+=h

            xarr.append(x)
            yarr.append(y)
        print("for baseball with drag",x,y,t)


        fig, ax = plt.subplots()

        ax.plot (xarr,yarr,'red',linestyle='-', marker=',')

        ax.set(title='Baseball - drag', xlabel='x', ylabel='y')


        #add a grid
        ax.grid()

        fig.savefig('baseball drag.png')  # uncomment to save plot
        
        #plt.show()
    drag()

    plt.show()

Problem4()
