#Cassandra Bodin
#Phys 305
#Homework 5
#run by "python hmk5_bodin.py"

#Problem 1: modify test_euler_cromer_orbit.py to use the verlet method for MERCURY's orbit

def Problem1():
    import math
    import numpy as np
    import matplotlib.pyplot as plt

    def energy(varg, rarg):
        rarg = rarg * 1.496e11
        varg = varg * 1.496e11 / 3.154e7
        E = 0.5 * m_merc * varg**2 - G * m_sun * m_merc / rarg 
        return E

#variables given
    g = -3.7 #accel due to gravity on Mercury
    G = 6.67e-11 #gravitational const
    GMs = 4*(math.pi**2)
    ecc_merc = 0.2056 #eccentricity of mercury
    semimajor_merc = 0.387
    a = semimajor_merc
    perihelion_merc = a*(1-ecc_merc)
    m_merc = 3.3011e23 #mass of mercury in kg
    m_sun = 1.989e30 #in kg
    vp_merc = math.sqrt(GMs) * math.sqrt((1+ecc_merc) / (a*(1-ecc_merc)) * (1+(m_merc/m_sun)))

#initial values
    vx = 0
    vy = vp_merc
    x = -perihelion_merc
    y = 0 


# steps and time (in years)
    h = 1e-3
    t_final = 10
    t_initial = 0
    t = t_initial
    count = 0

#variables for graphing
    xarr = np.array([])
    xarr2 = np.array([])
    yarr = np.array([])
    yarr2 = np.array([])
    xarr = np.append(xarr,x)
    yarr = np.append(yarr,y)

#variable dependent variables
    r = math.sqrt(x**2 + y**2)
    v = math.sqrt(vx**2 + vy**2)



#more for graph
    xarr2 = np.append(xarr2, t)
    yarr2 = np.append(yarr2,energy(v,r))

#impliment verler method
    while (t < t_final):

#initial acceleration
        ax=(-GMs)*x/r**3
        ay=(-GMs)*y/r**3

#position values -> calculate r
        x += vx*h +(.5)*ax*h**2
        y += vy*h +(.5)*ay*h**2
        r = math.sqrt(x**2 + y**2)

#new acceleration values
        ax1 = (-GMs)*x/r**3
        ay1 = (-GMs)*y/r**3

#velocity values -> calculate v
        vx += (h/2)*(ax1+ax)
        vy +=(h/2)*(ay1+ay)
        v = math.sqrt(vx**2 + vy**2)

#graphing values                                          
        xarr = np.append(xarr,x)
        yarr = np.append(yarr,y)
        xarr2 = np.append(xarr2,t)
        yarr2 = np.append(yarr2,energy(v,r))
        count += 1
  
        t = t+h
 
#now plot
    fig, ax = plt.subplots()

#plot of the orbit, comment out and uncomment next section to see energy graph
    ax.plot (xarr, yarr, 'b')
    ax.set(title='mercury orbit', xlabel='x axis', ylabel='y axis')
    ax.grid()
    fig.savefig('merc_orbit1.png')  # uncomment to save plot

#plot of the energy as a function of time, uncomment section to see energy graph
    #ax.plot (xarr2, yarr2, 'b')
    #ax.set(title='Mercury Energy v time', xlabel='x axis', ylabel='y axis')
    #ax.grid()
    #fig.savefig('E_v_t1.png')  # uncomment to save plot


    plt.show('all') #show plot command

Problem1() #uncomment to call program

#Problem 2: Modify problem 1 for general relativity. F=(G*M*m/r**2)(1+alpha/r**2) where alpha = 0.005

def Problem2():
    import math
    import numpy as np
    import matplotlib.pyplot as plt

    def energy(varg, rarg):
        rarg = rarg * 1.496e11
        varg = varg * 1.496e11 / 3.154e7
        E = 0.5 * m_merc * varg**2 - G * m_sun * m_merc / rarg 
        return E

#variables given
    g = -3.7 #accel due to gravity on Mercury
    alpha = 0.005
    G = 6.67e-11 #gravitational const
    GMs = 4*(math.pi**2)
    ecc_merc = 0.2056 #eccentricity of mercury
    semimajor_merc = 0.387
    a = semimajor_merc
    perihelion_merc = a*(1-ecc_merc)
    m_merc = 3.3011e23 #mass of mercury in kg
    m_sun = 1.989e30 #in kg
    vp_merc = math.sqrt(GMs) * math.sqrt((1+ecc_merc) / (a*(1-ecc_merc)) * (1+(m_merc/m_sun)))

#initial values
    vx = 0
    vy = vp_merc
    x = -perihelion_merc
    y = 0 


# steps and time (in years)
    h = 1e-3
    t_final = 10
    t_initial = 0
    t = t_initial
    count = 0

#variables for graphing
    xarr = np.array([])
    xarr2 = np.array([])
    yarr = np.array([])
    yarr2 = np.array([])
    xarr = np.append(xarr,x)
    yarr = np.append(yarr,y)

#variable dependent variables
    r = math.sqrt(x**2 + y**2)
    v = math.sqrt(vx**2 + vy**2)
    ax=(-GMs)/r**2
    ay=(-GMs)/r**2

#more for graph
    xarr2 = np.append(xarr2, t)
    yarr2 = np.append(yarr2,energy(v,r))

#impliment verler method
    while (t < t_final):

#initial acceleration
        ax=(-GMs)*x/r**3
        ay=(-GMs)*y/r**3

#position values -> calculate r
        x += vx*h +(.5)*ax*h**2
        y += vy*h +(.5)*ay*h**2
        r = math.sqrt(x**2 + y**2)

#new acceleration values
        ax1 = ((-GMs)*x/r**3)*(1+ alpha/r**2)
        ay1 = ((-GMs)*y/r**3)*(1+ alpha/r**2)

#velocity values -> calculate v
        vx += (h/2)*(ax1+ax)
        vy +=(h/2)*(ay1+ay)
        v = math.sqrt(vx**2 + vy**2)

#graphing values                                          
        xarr = np.append(xarr,x)
        yarr = np.append(yarr,y)
        xarr2 = np.append(xarr2,t)
        yarr2 = np.append(yarr2,energy(v,r))
        count += 1
  
        t = t+h
 
#now plot
    fig, ax = plt.subplots()

#plot of the orbit, comment out and uncomment next section to see energy graph
    ax.plot (xarr, yarr, 'b')
    ax.set(title='mercury orbit', xlabel='x axis', ylabel='y axis')
    ax.grid()
    fig.savefig('merc_orbit2.png')  # uncomment to save plot

#plot of the energy as a function of time, uncomment section to see energy graph
    #ax.plot (xarr2, yarr2, 'b')
    #ax.set(title='Mercury Energy v time', xlabel='x axis', ylabel='y axis')
    #ax.grid()
    #fig.savefig('E_v_t2.png')  # uncomment to save plot


    plt.show('all') #show plot command

Problem2() #uncomment to call program

#Program 3: modify Problem 2 to add animation

def Problem3():
    import math
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    def energy(varg, rarg):
        rarg = rarg * 1.496e11
        varg = varg * 1.496e11 / 3.154e7
        E = 0.5 * m_merc * varg**2 - G * m_sun * m_merc / rarg 
        return E

#variables given
    g = -3.7 #accel due to gravity on Mercury
    alpha = 0.005
    G = 6.67e-11 #gravitational const
    GMs = 4*(math.pi**2)
    ecc_merc = 0.2056 #eccentricity of mercury
    semimajor_merc = 0.387
    a = semimajor_merc
    perihelion_merc = a*(1-ecc_merc)
    m_merc = 3.3011e23 #mass of mercury in kg
    m_sun = 1.989e30 #in kg
    vp_merc = math.sqrt(GMs) * math.sqrt((1+ecc_merc) / (a*(1-ecc_merc)) * (1+(m_merc/m_sun)))

#initial values
    vx = 0
    vy = vp_merc
    x = -perihelion_merc
    y = 0 


# steps and time (in years)
    h = 1e-3
    t_final = 10
    t_initial = 0
    t = t_initial
    count = 0

#variables for graphing
    xarr = np.array([])
    xarr2 = np.array([])
    yarr = np.array([])
    yarr2 = np.array([])
    xarr = np.append(xarr,x)
    yarr = np.append(yarr,y)

#variable dependent variables
    r = math.sqrt(x**2 + y**2)
    v = math.sqrt(vx**2 + vy**2)
    ax=(-GMs)/r**3
    ay=(-GMs)/r**3

#more for graph
    xarr2 = np.append(xarr2, t)
    yarr2 = np.append(yarr2,energy(v,r))

#impliment verler method
    while (t < t_final):

#initial acceleration
        ax=(-GMs)*x/r**3
        ay=(-GMs)*y/r**3

#position values -> calculate r
        x += vx*h +(.5)*ax*h**2
        y += vy*h +(.5)*ay*h**2
        r = math.sqrt(x**2 + y**2)

#new acceleration values
        ax1 = ((-GMs)*x/r**3)*(1+ alpha/r**2)
        ay1 = ((-GMs)*y/r**3)*(1+ alpha/r**2)

#velocity values -> calculate v
        vx += (h/2)*(ax1+ax)
        vy +=(h/2)*(ay1+ay)
        v = math.sqrt(vx**2 + vy**2)

#graphing values                                          
        xarr = np.append(xarr,x)
        yarr = np.append(yarr,y)
        xarr2 = np.append(xarr2,t)
        yarr2 = np.append(yarr2,energy(v,r))
        count += 1
  
        t = t+h

 
#now plot
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    x2data, y2data = [], []
    ln1, = plt.plot([], [], 'ro', animated=True)
    ln2, = plt.plot([], [], 'b', animated=True)
    print (type(xdata))

    def init():
        ax.set_xlim(-.5, .5)
        ax.set_ylim(-.5, .5)
        return ln1,ln2

    def update(frame):
    #print (type(frame))
        x2data.append(xarr[frame])
        y2data.append(yarr[frame]) 
        xdata = xarr[frame]
        ydata = yarr[frame]

    #ydata = yarr(frame)
    #xdata.append(frame)
    #ydata.append(np.sin(frame))
        ln1.set_data(xdata, ydata)
        ln2.set_data(x2data, y2data)
        return ln1, ln2 #ln2 is the trajectory ofthe planet, ln1 is the ball

#animate it!!
    ani = FuncAnimation(fig, update, frames=xarr.size, interval=50, init_func=init, blit=True)

    plt.show() #show plot command

Problem3() #uncomment to call program
