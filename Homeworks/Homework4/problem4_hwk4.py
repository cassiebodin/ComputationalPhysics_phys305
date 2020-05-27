def Problem4():
#import libraries
    import numpy as np
    import matplotlib.pyplot as plt

#euler method
    def Euler4():
#for x dv_x/dt=(g/vterm**2)*v*vx <--no term for acceleration due to gravity
        #vx1v*np.cos(theta) theta =35 v=50
        def fx(vx,t):
            return (9.8/11**2)*50*vx
#for y dv_y/dt=-g+(g/vterm**2)*v*vy
        def fy(vy,t):
            return -9.8 +(9.8/11**2)*50*vy

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
        while (y>=0):
            vx+=h*fx(vx,t)
            x+=h*gx(x,t)
  
            vy+=h*fy(vy,t)
            y+=h*gy(y,t)
            t+=h

            xarr.append(x)
            yarr.append(y)
            print(x,y,t)
    Euler4()
Problem4()
