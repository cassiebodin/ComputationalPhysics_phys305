#Cassandra Bodin
#Phys305
#Hw 6
#2/26/19

#run by "python hmk6_bodin.py"

#Problem 1: satellite orbits sun in circular orbit (r=1AU) as crossing xaxis add a 1 time impulse in direction of its motion. Plot orbit before and after kick.

def Problem1():
    import math
    import numpy as np
    import matplotlib.pyplot as plt

    G = 6.67e-11
    GMs = 4*(math.pi**2)
    ecc_sat = 0 #circular orbit
    semimajor_sat = 1 #radius 1AU
    a = semimajor_sat
    perihelion_sat = a*(1-ecc_sat)
    m_sat = 1000 #chose a mass for the satellite in kg. Would be a medium to large satellite
    m_sun = 1.989e30
    vp_sat = math.sqrt(GMs) * math.sqrt((1+ecc_sat) / (a*(1-ecc_sat)) * (1+(m_sat/m_sun)))

   #initial values
    vx = 0
    vy = vp_sat
    x = -perihelion_sat
    y = 0 


# steps and time (in years)
    h = 1e-3
    t_final = 10
    t_initial = 0
    t = t_initial
    count = 0

#variables for graphing
    xarr = np.array([])
    yarr = np.array([])
    xarr = np.append(xarr,x)
    yarr = np.append(yarr,y)

#variable dependent variables
    r = math.sqrt(x**2 + y**2)
    v = math.sqrt(vx**2 + vy**2)


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

#add the kick in the y direction using an if statement
#chose count==2000 because it is after a bunch of orbits and has a bunch of orbits after it
        if (count==2000): 
            vy += 1
            
#graphing values                                          
        xarr = np.append(xarr,x)
        yarr = np.append(yarr,y)

        count += 1
  
        t = t+h
 
#now plot
    fig, ax = plt.subplots()

#plot of the orbit, comment out and uncomment next section to see energy graph
    ax.plot (xarr, yarr, 'b')
    ax.set(title='satellite orbit', xlabel='x axis', ylabel='y axis')
    ax.grid()
    fig.savefig('satellite_orbit.png') #uncomment to save

    plt.show()
Problem1()
#________________________________________________________________________

#Problem 2:4 astroids at 2.5AU, 2.6AU, 3AU, 3.28AU from sun. Assume a circular orbit. 3 body orbit with jupiter and the sun.


def Problem2():
    import math
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation


    G = 6.674e-11
    GMs = 4*(math.pi**2)
    m_sun = 1.989e30

#info Jupiter
    ecc_jup = 0.0489
    semimajor_jup = 5.2044
    a_jup = semimajor_jup
    perihelion_jup = a_jup*(1-ecc_jup)
    m_jup = 1.8982e27
    
    vp_jup = math.sqrt(GMs) * math.sqrt((1+ecc_jup) / (a_jup*(1-ecc_jup)) * (1+(m_jup/m_sun)))

    def Asteroid1():
#info Asteroid 1
        ecc_a1 = 0 #circular
        semimajor_a1 = 2.5 
        a_a1 = semimajor_a1
        perihelion_a1 = a_a1*(1-ecc_a1)
        m_a1 = 1e10 #mass of the asteroids are arbitarary since <<Msun

#initial parameters for asteroid
        vp_a1 = math.sqrt(GMs) * math.sqrt((1+ecc_a1) / (a_a1*(1-ecc_a1)) * (1+(m_a1/m_sun)))
        vx = 0
        vy = vp_a1
        x = -perihelion_a1
        y = 0 

#initial parameters for Jupiter
        vx2 = 0
        vy2 = vp_jup
        x2 = -perihelion_jup
        y2 = 0

# steps and time (in years)
        h = 1e-2
        t_final = 300 #need a ton of orbits to see what is happening
        t_initial = 0
        t = t_initial
        count = 0

#variables for graphing asteroid and variable dependent variables
        xarr = np.array([])
        yarr = np.array([])
        xarr = np.append(xarr,x)
        yarr = np.append(yarr,y)
        r = math.sqrt(x**2 + y**2)
        v = math.sqrt(vx**2 + vy**2)

#variables for graphing jupiter and variable dependent variables
        xarr2 = np.array([])
        yarr2 = np.array([])
        xarr2 = np.append(xarr2,x2)
        yarr2 = np.append(yarr2,y2)
        r2 = math.sqrt(x2**2 + y2**2)
        v2 = math.sqrt(vx2**2 + vy2**2)

        while (t < t_final):
#radial values
            r = math.sqrt(x**2 + y**2)
            r2 = math.sqrt(x2**2 + y2**2)
            rrel = math.sqrt( (x-x2)**2 + (y-y2)**2)

#velocity values
      # vx, vy is asteroid
      # vx2, vy2 is jupiter
            vx = vx +h*(-GMs*x/r**3- GMs*(m_jup/m_sun)*(x-x2)/rrel**3)
            vy = vy+h*(-GMs*y/r**3- GMs*(m_jup/m_sun)*(y-y2)/rrel**3)
            vx2 = vx2 +h*(-GMs*x2/r2**3)#- GMs*(m_jup/m_sun)*(x2-x)/r**3) #add jupiter mass dependence on asteroid by uncommenting
            vy2 = vy2 +h*(-GMs*y2/r2**3)# - GMs*(m_jup/m_sun)*(y2-y)/r**3)#add jupiter mass dependence on asteroid by uncommenting

#position values
      # x, y is asteroid
      # x2, y2 is jupiter
            x = x + vx*h
            y = y + vy*h
            x2 = x2 + vx2*h
            y2 = y2 + vy2*h                                                                
#graph                                     
            xarr = np.append(xarr,x)
            yarr = np.append(yarr,y)
            xarr2 = np.append(xarr2,x2)
            yarr2 = np.append(yarr2,y2)
            count += 1
  
            t = t+h
#now plot
        fig, ax = plt.subplots()

#plot of the orbit
        ax.plot (xarr, yarr, 'b', linewidth=1)
        ax.plot (xarr2, yarr2, 'r')
        ax.set(title='asteroid 1', xlabel='x axis', ylabel='y axis')
        ax.grid()
        fig.savefig('asteroid_1.png')  # uncomment to save plot

    Asteroid1()

    def Asteroid2():
#info Asteroid 2 - 
        ecc_a2 = 0 #circular
        semimajor_a2 = 2.6
        a_a2 = semimajor_a2
        perihelion_a2 = a_a2*(1-ecc_a2)
        m_a2 = 1e10

#initial parameters for asteroid
        vp_a2 = math.sqrt(GMs) * math.sqrt((1+ecc_a2) / (a_a2*(1-ecc_a2)) * (1+(m_a2/m_sun)))
        vx = 0
        vy = vp_a2
        x = -perihelion_a2
        y = 0 

#initial parameters for Jupiter
        vx2 = 0
        vy2 = vp_jup
        x2 = -perihelion_jup
        y2 = 0

# steps and time (in years)
        h = 1e-2
        t_final = 300
        t_initial = 0
        t = t_initial
        count = 0

#variables for graphing asteroid and variable dependent variables
        xarr = np.array([])
        yarr = np.array([])
        xarr = np.append(xarr,x)
        yarr = np.append(yarr,y)
        r = math.sqrt(x**2 + y**2)
        v = math.sqrt(vx**2 + vy**2)

#variables for graphing jupiter and variable dependent variables
        xarr2 = np.array([])
        yarr2 = np.array([])
        xarr2 = np.append(xarr2,x2)
        yarr2 = np.append(yarr2,y2)
        r2 = math.sqrt(x2**2 + y2**2)
        v2 = math.sqrt(vx2**2 + vy2**2)

        while (t < t_final):
#radial values
            r = math.sqrt(x**2 + y**2)
            r2 = math.sqrt(x2**2 + y2**2)
            rrel = math.sqrt( (x-x2)**2 + (y-y2)**2)

#velocity values
      # vx, vy is asteroid
      # vx2, vy2 is jupiter
            vx = vx +h*(-GMs*x/r**3- GMs*(m_jup/m_sun)*(x-x2)/rrel**3)
            vy = vy+h*(-GMs*y/r**3- GMs*(m_jup/m_sun)*(y-y2)/rrel**3)
            vx2 = vx2 +h*(-GMs*x2/r2**3)#- GMs*(m_jup/m_sun)*(x2-x)/r**3) #add jupiter mass dependence on asteroid by uncommenting
            vy2 = vy2 +h*(-GMs*y2/r2**3)# - GMs*(m_jup/m_sun)*(y2-y)/r**3)#add jupiter mass dependence on asteroid by uncommenting

#position values
      # x, y is asteroid
      # x2, y2 is jupiter
            x = x + vx*h
            y = y + vy*h
            x2 = x2 + vx2*h
            y2 = y2 + vy2*h                                                                
#graph                                     
            xarr = np.append(xarr,x)
            yarr = np.append(yarr,y)
            xarr2 = np.append(xarr2,x2)
            yarr2 = np.append(yarr2,y2)
            count += 1
  
            t = t+h
#now plot
        fig, ax = plt.subplots()

#plot of the orbit
        ax.plot (xarr, yarr, 'b', linewidth=1)
        ax.plot (xarr2, yarr2, 'r')
        ax.set(title='asteroid 2', xlabel='x axis', ylabel='y axis')

        ax.grid()
        fig.savefig('asteroid_2.png')  # uncomment to save plot

    Asteroid2()
    def Asteroid3():
#info Asteroid 3 - 
        ecc_a3 = 0 #circular
        semimajor_a3 = 3
        a_a3 = semimajor_a3
        perihelion_a3 = a_a3*(1-ecc_a3)
        m_a3 = 1e10

#initial parameters for asteroid
        vp_a3 = math.sqrt(GMs) * math.sqrt((1+ecc_a3) / (a_a3*(1-ecc_a3)) * (1+(m_a3/m_sun)))
        vx = 0
        vy = vp_a3
        x = -perihelion_a3
        y = 0 

#initial parameters for Jupiter
        vx2 = 0
        vy2 = vp_jup
        x2 = -perihelion_jup
        y2 = 0

# steps and time (in years)
        h = 1e-2
        t_final = 300
        t_initial = 0
        t = t_initial
        count = 0

#variables for graphing asteroid and variable dependent variables
        xarr = np.array([])
        yarr = np.array([])
        xarr = np.append(xarr,x)
        yarr = np.append(yarr,y)
        r = math.sqrt(x**2 + y**2)
        v = math.sqrt(vx**2 + vy**2)

#variables for graphing jupiter and variable dependent variables
        xarr2 = np.array([])
        yarr2 = np.array([])
        xarr2 = np.append(xarr2,x2)
        yarr2 = np.append(yarr2,y2)
        r2 = math.sqrt(x2**2 + y2**2)
        v2 = math.sqrt(vx2**2 + vy2**2)

        while (t < t_final):
#radial values
            r = math.sqrt(x**2 + y**2)
            r2 = math.sqrt(x2**2 + y2**2)
            rrel = math.sqrt( (x-x2)**2 + (y-y2)**2)

#velocity values
      # vx, vy is asteroid
      # vx2, vy2 is jupiter
            vx = vx +h*(-GMs*x/r**3- GMs*(m_jup/m_sun)*(x-x2)/rrel**3)
            vy = vy+h*(-GMs*y/r**3- GMs*(m_jup/m_sun)*(y-y2)/rrel**3)
            vx2 = vx2 +h*(-GMs*x2/r2**3)#- GMs*(m_jup/m_sun)*(x2-x)/r**3) #add jupiter mass dependence on asteroid by uncommenting
            vy2 = vy2 +h*(-GMs*y2/r2**3)# - GMs*(m_jup/m_sun)*(y2-y)/r**3)#add jupiter mass dependence on asteroid by uncommenting

#position values
      # x, y is asteroid
      # x2, y2 is jupiter
            x = x + vx*h
            y = y + vy*h
            x2 = x2 + vx2*h
            y2 = y2 + vy2*h                                                                
#graph                                     
            xarr = np.append(xarr,x)
            yarr = np.append(yarr,y)
            xarr2 = np.append(xarr2,x2)
            yarr2 = np.append(yarr2,y2)
            count += 1
  
            t = t+h
#now plot
        fig, ax = plt.subplots()

#plot of the orbit
        ax.plot (xarr, yarr, 'b', linewidth=1)
        ax.plot (xarr2, yarr2, 'r')
        ax.set(title='asteroid 3', xlabel='x axis', ylabel='y axis')

        ax.grid()
        fig.savefig('asteroid_3.png')  # uncomment to save plot

    Asteroid3()
    def Asteroid4():
#info Asteroid 4 - 
        ecc_a4 = 0 #circular
        semimajor_a4 = 3.28
        a_a4 = semimajor_a4
        perihelion_a4 = a_a4*(1-ecc_a4)
        m_a4 = 1e10

#initial parameters for asteroid
        vp_a4 = math.sqrt(GMs) * math.sqrt((1+ecc_a4) / (a_a4*(1-ecc_a4)) * (1+(m_a4/m_sun)))
        vx = 0
        vy = vp_a4
        x = -perihelion_a4
        y = 0 

#initial parameters for Jupiter
        vx2 = 0
        vy2 = vp_jup
        x2 = -perihelion_jup
        y2 = 0

# steps and time (in years)
        h = 1e-2
        t_final = 300
        t_initial = 0
        t = t_initial
        count = 0

#variables for graphing asteroid and variable dependent variables
        xarr = np.array([])
        yarr = np.array([])
        xarr = np.append(xarr,x)
        yarr = np.append(yarr,y)
        r = math.sqrt(x**2 + y**2)
        v = math.sqrt(vx**2 + vy**2)

#variables for graphing jupiter and variable dependent variables
        xarr2 = np.array([])
        yarr2 = np.array([])
        xarr2 = np.append(xarr2,x2)
        yarr2 = np.append(yarr2,y2)
        r2 = math.sqrt(x2**2 + y2**2)
        v2 = math.sqrt(vx2**2 + vy2**2)

        while (t < t_final):
#radial values
            r = math.sqrt(x**2 + y**2)
            r2 = math.sqrt(x2**2 + y2**2)
            rrel = math.sqrt( (x-x2)**2 + (y-y2)**2)

#velocity values
      # vx, vy is asteroid
      # vx2, vy2 is jupiter
            vx = vx +h*(-GMs*x/r**3- GMs*(m_jup/m_sun)*(x-x2)/rrel**3)
            vy = vy+h*(-GMs*y/r**3- GMs*(m_jup/m_sun)*(y-y2)/rrel**3)
            vx2 = vx2 +h*(-GMs*x2/r2**3)#- GMs*(m_jup/m_sun)*(x2-x)/r**3) #add jupiter mass dependence on asteroid by uncommenting
            vy2 = vy2 +h*(-GMs*y2/r2**3)# - GMs*(m_jup/m_sun)*(y2-y)/r**3)#add jupiter mass dependence on asteroid by uncommenting

#position values
      # x, y is asteroid
      # x2, y2 is jupiter
            x = x + vx*h
            y = y + vy*h
            x2 = x2 + vx2*h
            y2 = y2 + vy2*h                                                                
#graph                                     
            xarr = np.append(xarr,x)
            yarr = np.append(yarr,y)
            xarr2 = np.append(xarr2,x2)
            yarr2 = np.append(yarr2,y2)
            count += 1
  
            t = t+h
#now plot
        fig, ax = plt.subplots()

#plot of the orbit
        ax.plot (xarr, yarr, 'b', linewidth=1)
        ax.plot (xarr2, yarr2, 'r')
        ax.set(title='asteroid 4', xlabel='x axis', ylabel='y axis')

        ax.grid()
        fig.savefig('asteroid_4.png')  # uncomment to save plot

    Asteroid4()

    plt.show('all') #show plot command
Problem2()
