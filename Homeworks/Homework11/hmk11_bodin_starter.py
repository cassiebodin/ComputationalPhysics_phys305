#Cassandra Bodin
#Phys 305
#Homework 11

#run using "python hmk11_bodin.py"


#Problem 1: hard scattering, calculate temp and pressure of the gas in the simulation. (Use kT instead of T). Use results in ideal gas law (PV=nkT) and comment. due for 2 different temps. P=pressure V=volume n=amount-of-gas k=boltz-const and T=temp
#used test_md_scat2.py as template

def Problem1():
    import math
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    import random
    import math


    random.seed()
    h = 0.01
    x = np.array([])
    y = np.array([])
    vx = np.array([])
    vy = np.array([])
    v = np.array([])

    nballs = 10
    length = 10

#variables for calculating Pressure and Temp using ideal gas law
    A=length * length #area
    k=1.38e-23 #boltzmann constant(m^2*kg*s^-1*K^-1)
    V=A #in this case we are working in 2D so volume is replaced by area
    N=nballs #amount of gas is the amount of balls
    m=1 #chose mass of atom=1 for simplicities sake (ie assuming hydrogen)
    
# init
    vmax = 10
    for i in range(nballs):
        x = np.append(x,random.random()*10.)
        y = np.append(y,random.random()*10.)
        vx = np.append(vx,vmax*(2*random.random() - 1))
        vy = np.append(vy,vmax*(2*random.random() - 1))

    xarr = np.zeros((1,nballs),float)
    xarr = np.append(xarr,[x],axis=0)
    xarr = np.delete(xarr,0,0)
    yarr = np.zeros((1,nballs),float)
    yarr = np.append(xarr,[x],axis=0)
    yarr = np.delete(xarr,0,0)
    vxarr = np.zeros((1,nballs),float)
    vxarr = np.append(vxarr,[x],axis=0)
    vxarr = np.delete(vxarr,0,0)
    vyarr = np.zeros((1,nballs),float)
    vyarr = np.append(vyarr,[x],axis=0)
    vyarr = np.delete(vyarr,0,0)

    t = 0
    time = 10
    count = 0
    eps2 = 0.1

    while (t < time):
      
        for i in range(nballs):
            x[i] = x[i] + vx[i]*h
            y[i] = y[i] + vy[i]*h
            if x[i] < 0:
                x[i] = 0.
                vx[i] = -vx[i]
            if x[i] > length:
                x[i] = length
                vx[i] = -vx[i]
            if y[i] < 0:
                y[i] = 0.
                vy[i] = -vy[i]
            if y[i] > length:
                y[i] = length
                vy[i] = -vy[i]

        for i in range(nballs-1):
            for j in range (i+1,nballs):
                if ((x[i]-x[j])**2 + (y[i]-y[j])**2) < eps2:
                    # scatter
                    vx_cm = 0.5*(vx[i] + vx[j])
                    vy_cm = 0.5*(vy[i] + vy[j])
                    u1x = vx[i] - vx_cm
                    u1y = vy[i] - vy_cm
                    umag = math.sqrt(u1x**2 + u1y**2)
                    theta = 2*np.pi*random.random()
                    vx[i] = math.cos(theta)* umag + vx_cm
                    vx[j] = -math.cos(theta)* umag + vx_cm
                    vy[i] = math.sin(theta)* umag + vy_cm
                    vy[j] = -math.sin(theta)* umag + vy_cm

        v2=vx**2+vy**2
        xarr = np.append(xarr,[x], axis=0)
        yarr = np.append(yarr,[y], axis=0)
        count += 1  
        t = t+h

#calculate Temperature and Pressure
    print("*___________________________________________________*")
    #use this equation <E>=<.5*m*v2>=3*.5*k*T
    T=((1/3)*m*np.average(v2))/k 
    kT = k*T
    print("The Temperature is:", T)
    print("kT is equal to:", kT)
    
    P= (N*k*T)/V
    print ("The Pressure is:", P)
    print("*___________________________________________________*")

#stuff for graphing
    test = []
    fig, ax = plt.subplots()
    xdata = np.zeros(nballs)
    ydata = np.zeros(nballs)
    for i in range(nballs):
        lntest = ax.plot([], [], 'ro', animated=True)[0]
        test.append(lntest)
    print (test)

    def init():
        ax.set_xlim(0., 10.)
        ax.set_ylim(0., 10.)
        for line in test:
            line.set_data([],[])
        return test

    def update(frame):
        for i in range(nballs):
            xdata[i] = xarr[frame,i]
            ydata[i] = yarr[frame,i]
        nlines = 0
        for line in test:
            line.set_data(xdata[nlines], ydata[nlines])
            nlines += 1
        return test

    ani = FuncAnimation(fig, update, frames=xarr.size, interval=50, init_func=init, blit=True)
    plt.show()

#Problem1()

#print("________________________________________________________________")

#Problem2: hard scattering, add gravitational force down on ea particle using verlet or rungekutta2, check for collisions,reflect off boundaries. nballs=100, h=.005. vinit=1, g=1 
#measure temp for height less than 2 and greater than 2. make histogram of the heights once equilibrium has been reached. compare to result for isothermalatmo (n=exp(-mgh/kT)
#used test_md_scat2.py as template

def Problem2():
    import math
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    import random
    import math


    random.seed()
    h = 0.005
    x = np.array([])
    y = np.array([])
    vx = np.array([])
    vy = np.array([])
    v = np.array([])


    nballs = 100
    length = 10
    g=1
    vinit=1

#variables for calculating Pressure and Temp using ideal gas law
    A=length * length #area
    k=1.38e-23 #boltzmann constant
    V=A #in this case we are working in 2D so volume is replaced by area
    N=nballs #amount of gas is the amount of balls
    m=1 #chose mass of atom=1 for simplicities sake (ie assuming hydrogen)
    
# init
    vmax = 1
    for i in range(nballs):
        x = np.append(x,random.random()*10.)
        y = np.append(y,random.random()*10.)
        vx = np.append(vx,vmax*(2*random.random() - 1))
        vy = np.append(vy,vmax*(2*random.random() - 1))

    xarr = np.zeros((1,nballs),float)
    xarr = np.append(xarr,[x],axis=0)
    xarr = np.delete(xarr,0,0)
    yarr = np.zeros((1,nballs),float)
    yarr = np.append(xarr,[x],axis=0)
    yarr = np.delete(xarr,0,0)
    vxarr = np.zeros((1,nballs),float)
    vxarr = np.append(vxarr,[x],axis=0)
    vxarr = np.delete(vxarr,0,0)
    vyarr = np.zeros((1,nballs),float)
    vyarr = np.append(vyarr,[x],axis=0)
    vyarr = np.delete(vyarr,0,0)
    print (xarr.shape)

    t = 0
    time = 10
    count = 0
    eps2 = 0.1

    while (t < time):
        ay = np.zeros((nballs),float)#*********************
        ay1 = np.zeros((nballs),float)#*********************

        for i in range(nballs):
            x[i] = x[i] + vx[i]*h
            y[i] = y[i] + vy[i]*h

#verlet method **************************************************************
            ay[i]= -g

            y[i]+=vy[i]*h +(.5)*ay[i]*h**2

            ay1[i]+= -g

            vy[i]+=(h/2)*(ay1[i]+ay[i])
#***************************************************************************

            if x[i] < 0:
                x[i] = 0.
                vx[i] = -vx[i]
            if x[i] > length:
                x[i] = length
                vx[i] = -vx[i]
            if y[i] < 0:
                y[i] = 0.
                vy[i] = -vy[i]
            if y[i] > length:
                y[i] = length
                vy[i] = -vy[i]

        for i in range(nballs-1):
            for j in range (i+1,nballs):
                if ((x[i]-x[j])**2 + (y[i]-y[j])**2) < eps2:
                    # scatter
                    vx_cm = 0.5*(vx[i] + vx[j])
                    vy_cm = 0.5*(vy[i] + vy[j])
                    u1x = vx[i] - vx_cm
                    u1y = vy[i] - vy_cm
                    umag = math.sqrt(u1x**2 + u1y**2)
                    theta = 2*np.pi*random.random()
                    vx[i] = math.cos(theta)* umag + vx_cm
                    vx[j] = -math.cos(theta)* umag + vx_cm
                    vy[i] = math.sin(theta)* umag + vy_cm
                    vy[j] = -math.sin(theta)* umag + vy_cm

#find v2 for above y=2 and below y=2 *****************************************
    if y[i] or y[j] > 2:
        v2_above=(np.average(vx))**2+(np.average(vy))**2
    elif y[i] or y[j] < 2:
        v2_below=(np.average(vx))**2+(np.average(vy))**2
#****************************************************************************

#append data
        xarr = np.append(xarr,[x], axis=0)
        yarr = np.append(yarr,[y], axis=0)
        count += 1  
        t = t+h

    print (xarr.shape)

#calculate Temperature ******************************************************
    T_above=.5*m*(v2_above)
    T_below=.5*m*(v2_below)
    
    kT_above = k*T_above
    kT_below = k*T_below
    print("The Temperature above 2 is:", T_above)
    print("kT is equal to:", kT_above)
    print("The Temperature below 2 is:", T_below)
    print("kT is equal to:", kT_below)

#****************************************************************************

#stuff for graphing
    test = []
    fig, ax = plt.subplots(1,2)
    xdata = np.zeros(nballs)
    ydata = np.zeros(nballs)
    for i in range(nballs):
        lntest = ax[0].plot([], [], 'ro', animated=True)[0]
        test.append(lntest)

#ln0, = plt.plot([], [], 'ro', animated=True)
#ln1, = plt.plot([], [], 'bo', animated=True)
#ln2, = plt.plot([], [], 'go', animated=True)
#ln3, = plt.plot([], [], 'co', animated=True)
#ln4, = plt.plot([], [], 'mo', animated=True)
#print (type(ln0))
    print (test)

    def init():
        ax[0].set_xlim(0., 10.)
        ax[0].set_ylim(0., 10.)
        for line in test:
            line.set_data([],[])
        return test

    def update(frame):
    #print (type(frame))
        for i in range(nballs):
            xdata[i] = xarr[frame,i]
            ydata[i] = yarr[frame,i]
#    ln0.set_data(xdata[0], ydata[0])
#    ln1.set_data(xdata[1], ydata[1])
#    ln2.set_data(xdata[2], ydata[2])
#    ln3.set_data(xdata[3], ydata[3])
#    ln4.set_data(xdata[4], ydata[4])
#    return ln0, ln1, ln2, ln3, ln4
        nlines = 0
        for line in test:
            line.set_data(xdata[nlines], ydata[nlines])
            nlines += 1
        return test
    
    ax[1].hist(yarr[0,:], bins=50, range=(-10,10), histtype='step', color='r')      
    ax[1].hist(yarr[int(steps)-10,:], bins=50, range=(-10,10), histtype='step', color='b')
    ax[1].set(title='title', xlabel='y', ylabel='number')               
    ax[1].grid()

    ani = FuncAnimation(fig, update, frames=xarr.size, interval=50, init_func=init, blit=True)
    plt.show()

Problem2()

#print("________________________________________________________________")

#Problem 3: Complete Lennard Jones inclass problem from L23. Try several values for vmax. Calculate kT using avg of v**2
#Think about how you might characterize melting in this problem.
#used test_md_lennard2_class as template

def Problem3():
    import math
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    import random


    random.seed()
    x = np.array([])
    y = np.array([])
    vx = np.array([])
    vy = np.array([])
    v = np.array([])
    ncol = np.array([])
    dvx = np.array([])
    vxarrall = np.array([])
    varrall = np.array([])
    length = 5


    nballs = 25
# init the balls
    vmax = 0.0
    for i in range(nballs):
        xoff = int(i/5) + 0.5
        yoff = i%5 + 0.5
        x = np.append(x, (random.random()*0.005 + xoff))
        y = np.append(y, (random.random()*0.005 + yoff))
      #print (xoff, yoff)

        ncol = np.append(ncol,0)
      #vx = np.append(vx,vmax*(2*random.random() - 1))
      #vy = np.append(vy,vmax*(2*random.random() - 1))
        theta = 2*np.pi*random.random()
        vx = np.append(vx,vmax*math.cos(theta))
        vy = np.append(vy,vmax*math.sin(theta))
        v = np.sqrt(vx**2 + vy**2)
        v2 = vx**2 + vy**2
        dvx = np.append(dvx,0)

# note mass = 1, so fx is really ax = fx/m
    fxarr = np.zeros((nballs,2))
    fyarr = np.zeros((nballs,2))

    print (x.size)
    print (v.size)
    print (v)
    print (v2)

    xarr = np.zeros((1,nballs),float)
    xarr = np.append(xarr,[x],axis=0)
    xarr = np.delete(xarr,0,0)
    yarr = np.zeros((1,nballs),float)
    yarr = np.append(yarr,[y],axis=0)
    yarr = np.delete(yarr,0,0)
    vxarr = np.zeros((1,nballs),float)
    vxarr = np.append(vxarr,[vx],axis=0)
    vxarr = np.delete(vxarr,0,0)
    vyarr = np.zeros((1,nballs),float)
    vyarr = np.append(vyarr,[vy],axis=0)
    vyarr = np.delete(vyarr,0,0)
    varr = np.zeros((1,nballs),float)
    varr = np.append(varr,[v],axis=0)
    varr = np.delete(varr,0,0)
    v2arr = np.zeros((1,nballs),float)
    v2arr = np.append(v2arr,[v2],axis=0)
    v2arr = np.delete(v2arr,0,0)
    dvxarr = np.zeros((1,nballs),float)
    dvxarr = np.append(dvxarr,[dvx],axis=0)
    dvxarr = np.delete(dvxarr,0,0)
    dvxarr = np.zeros((1,nballs),float)
    dvxarr = np.append(dvxarr,[dvx],axis=0)
    dvxarr = np.delete(dvxarr,0,0)
    tarr = np.zeros(1)

    print (tarr.shape)
    print (xarr.shape)
    print (varr.shape)

    t = 0
    time = 50
    count = 0
    h = 0.01
    steps = time/h + 1
    print ('steps = ',steps)
    r2cut = 9.


    while (t < time):

        ax = np.zeros((nballs),float)#********************
        ay = np.zeros((nballs),float)#*********************
        ax1 = np.zeros((nballs),float)#********************
        ay1 = np.zeros((nballs),float)#*********************
        fxarr = np.zeros((nballs,2))
        fyarr = np.zeros((nballs,2))
      # loop over pairs of balls
        for i in range(nballs-1):
            for j in range(i+1,nballs):
              #if (i == j): exit()
                dx = x[i] - x[j]
                dy = y[i] - y[j]
              # need this snippet because the walls are not reflecting
                if (abs(dx) > length/2):
                    if dx >= 0.:
                        dx = dx - length
                    else:
                        dx = dx + length
              #print ('dx ',dx,x[i],x[j])
                if (abs(dy) > length/2):
                    if dy >= 0.:
                        dy = dy - length
                    else:
                        dy = dy + length

                r2 = dx**2 + dy**2
                r = math.sqrt(r2)
              # include these in the force calculation
                if (r2 < r2cut):
# calculate the force in the x and y directions
                    fijx = 24 * ( (2./r**13) - (1/r**7) ) * (dx/r)
                    fijy = 24 * ( (2./r**13) - (1/r**7) ) * (dy/r)
# add these forces to fxarr[i,0], fyarr[i,0], fxarr[j,0], fyarr[j,0]
                    fxarr[i,0]+=fijx
                    fyarr[i,0]+=fijy
                    fxarr[j,0]+=-fijx
                    fyarr[j,0]+=-fijy


# after all the forces are summed, update the position using the
# velocity verlet method ***************************************************************************************************************************************
        for i in range(nballs-1):
            for j in range(i+1,nballs): 
                ax[i]= fxarr[i,0]
                ax[i]= fxarr[i,0]
                ay[j]= fyarr[j,0]
                ay[j]= fyarr[j,0]

                x[i]+=vx[i]*h +(.5)*ax[i]*h**2
                x[j]+=vx[j]*h +(.5)*ax[j]*h**2
                y[i]+=vy[i]*h +(.5)*ay[i]*h**2
                y[j]+=vy[j]*h +(.5)*ay[j]*h**2

                ax1[i]+= fxarr[i,0]
                ax1[i]+= fxarr[i,0]
                ay1[j]+= fyarr[j,0]
                ay1[j]+= fyarr[j,0]

                vx[i]+=(h/2)*(ax1[i]+ax[i])
                vx[j]+=(h/2)*(ax1[j]+ax[j])
                vy[i]+=(h/2)*(ay1[i]+ay[i])
                vy[j]+=(h/2)*(ay1[j]+ay[j])

# after the positions are updated, apply the periodic boundary conditions
                if x[i] or x[j] < 0:
                    vx[i] = vx[i]
                    x[i] = length
                    x[j] = length

                if x[i] or x[j] > length:
                    vx[i] = vx[i]
                    x[i] = 0.
                    x[j] = 0.

                if y[i] or y[j] < 0:
                    vy[i] = vy[i]
                    y[i] = length
                    y[j] = length

                if y[i] or y[j] > length:
                    vy[i] = vy[i]
                    y[i] = 0.
                    y[j] = 0.
# note i have included the code already to update the velocities
# you do not have to do that

      # now update velocities
      # note the positions have already been updated
      # so we have to go through it again to find the newer (i+1) values of f, then v

        for i in range(nballs-1):
            for j in range(i+1,nballs):
                dx = x[i] - x[j]
                dy = y[i] - y[j]
              # need this because the walls are not reflecting                                                                                       
                if (abs(dx) > length/2):
                    if dx >= 0.:
                        dx = dx - length
                    else:
                        dx = dx + length
                if (abs(dy) > length/2):
                    if dy >= 0.:
                        dy = dy - length
                    else:
                        dy = dy + length
                r2 = dx**2 + dy**2
                r = math.sqrt(r2)
                if (r2 < r2cut):
              # include or not in the force calculation                                                                                              
                    if (r2 == 0.):  r2 = 1e-4
                    fijx = 24 * ( (2./r**13) - (1/r**7) ) * (dx/r)
                    fijy = 24 * ( (2./r**13) - (1/r**7) ) * (dy/r)
                    # index 1 means newer, index 0 means older
                    fxarr[i,1] = fxarr[i,1] + fijx
                    fyarr[i,1] = fyarr[i,1] + fijy
                    fxarr[j,1] = fxarr[j,1] - fijx
                    fyarr[j,1] = fyarr[j,1] - fijy

      # forces are updated                                                           # now update the velocity                                      
      # now update the velocities                          
        for i in range(nballs):
            vx[i] = vx[i] + (h/2)*(fxarr[i,1] + fxarr[i,0])
            vy[i] = vy[i] + (h/2)*(fyarr[i,1] + fyarr[i,0])
            if vx[i]>10:
                print (i,vx[i],vy[i],fxarr[i,1],fyarr[i,1])


        xarr = np.append(xarr,[x], axis=0)
        yarr = np.append(yarr,[y], axis=0)
        vxarr = np.append(vxarr,[vx], axis=0)
        vyarr = np.append(vyarr,[vy], axis=0)
        varr = np.append(varr,[v], axis=0)
        v2arr = np.append(v2arr,[v2], axis=0)
        dvxarr = np.append(dvxarr,[dvx],axis=0)
        if (t > 5 and count%10 == 0):
            vxarrall = np.append(vxarrall,vx)
            varrall = np.append(varrall,v)

        count += 1  
        t = t+h
        tarr = np.append(tarr,t)

    print (count)
    print (xarr.shape)
    print (tarr.shape)
    print (ncol)
# mean ke = kt
    kt = np.mean(v2arr[int(steps)-10,:])/2.
    print ('kt = ',kt)
    vol = 100
    print ('vol = ',vol)
    area = 10
    print ('area = ',area)
    dvxsum = 0
    timetotal = 0
    for i in range(200):
        dvxsum = dvxsum + np.sum(dvxarr[int(steps/2)+i,:])
        timetotal = timetotal+h
    print (dvxsum, timetotal)
    pressure = dvxsum/timetotal/area
    print ('pressure = ',pressure)
    print ('pv =',pressure*vol)
    print ('nt = ',nballs*kt)


    test = []
    ichoose = 0
    if ichoose == 0:

        fig, ax = plt.subplots()
        xdata = np.zeros(nballs)
        ydata = np.zeros(nballs)
        for i in range(nballs):
            lntest = ax.plot([], [], 'ro', animated=True)[0]
            test.append(lntest)
    print (test)

    def init():
        ax.set_xlim(0., length)
        ax.set_ylim(0., length)
        for line in test:
            line.set_data([],[])
        return test

    def update(frame):
    #print (type(frame))
        for i in range(nballs):
            xdata[i] = xarr[frame,i]
            ydata[i] = yarr[frame,i]
            nlines = 0
            for line in test:
                line.set_data(xdata[nlines], ydata[nlines])
                nlines += 1
        return test

    ani = FuncAnimation(fig, update, frames=xarr.size, interval=50, init_func=init, blit=True)
    plt.show()


    fig, ax = plt.subplots(1,2)
    ax[0].hist(vxarr[0,:], bins=50, range=(-10,10), histtype='step', color='r')      
    ax[0].hist(vxarr[int(steps)-10,:], bins=50, range=(-10,10), histtype='step', color='b')
    ax[0].set(title='title', xlabel='vx', ylabel='number')               
    ax[0].grid()

    print(np.mean(varr[int(steps)-10,:]))
    print(np.mean(varr[int(steps)-10,:])/1.128)
      #ax[1].hist(varr[0,:], bins=50,range=(0,25),  histtype='step', color='r')
      #ax[1].hist(varr[int(steps)-10,:], bins=50,range=(0,5),  histtype='step', color='b')
    ax[1].hist(varrall, bins=50,range=(0,5),  histtype='step', color='b') 
    ax[1].set(title='title', xlabel='speed', ylabel='number')
    ax[1].grid()

    plt.show()

#Problem3()
