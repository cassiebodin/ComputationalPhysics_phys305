#Cassandra Bodin
#Phys 305
#Homework 9
#run using "python hmk_bodin.py"


#Problem1: Potential and magnitude of electriv field from 2 point charges. Charge density is 1C/m^2. 2D box. Find v by solving Poisson's eq. E_x=(V(i+1,j)-V(i-1,j))/2a and E_y=(V(i,j+1)-V(i,j-1))/2a. 1 plot Electric field, 2 plot Electric potential

def Problem1():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.colors as colors
    from mpl_toolkits import mplot3d
    import math

# Constants
    m = 10         # number of points
    Vtop = 0.0      # boundary conditions
    Vbot = 0.0
    Vleft = 0.0
    Vright = 0.0
    target = 1e-6   # Target accuracy
    a=1

# Create arrays to hold potential values
    V = np.zeros([m+1,m+1],float)
    V[m,:] = Vtop
    V[0,:] = Vbot
    V[:,m] = Vright
    V[:,0] = Vleft
    Vprime = np.zeros([m+1,m+1],float)
    zdata = np.zeros([m+1,m+1],float)
    edata = np.zeros([m+1,m+1],float)


# Main loop
    deltaV = 1.0
    while deltaV>target:
        deltaV = 0.
    # Calculate new values phiprime of the potential
    # in terms of the old values phi

        for i in range(m+1):
            for j in range(m+1):
#set conditions for edge of box
                if (i==m or i==0 or j==m or j==0):
                    Vprime[i,j]=V[i,j]

#set the conditions for point charges inside box
                elif (i==m-3 or i==3):
                    Vprime[m-3,5] =50
                    Vprime[3,5] = 50
                    Vprime[:,0] = Vleft
                    Vprime[:,m] = Vright


    # calculate new values phiprime of the potential in terms of the old values phi
                else:
                    Vprime[i,j]= (1/4)*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])

    # calculate some difference to use for convergence
                deltaV += abs(Vprime[i,j]- V[i,j])
                V, Vprime = Vprime, V
    for i in range(m+1):
        for j in range(m+1):
            if (i==m or i==0 or j==m or j==0):
                continue
            else:
                E_x=(Vprime[i+1,j]-Vprime[i-1,j])/(2*a)
                E_y=(Vprime[i,j+1]-Vprime[i,j-1])/(2*a)
                edata[i,j]= math.sqrt(E_x**2+E_y**2)

#append data for electric field

    zdata = Vprime

    np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
    for i in range(m,-1,-1):
        print (zdata[i,:])

#plot data, kept both plots since it uses a different color plot method
    fig, ax = plt.subplots(1,2)

    levels = 15
    cf = ax[0].contourf(zdata, levels=levels,cmap='jet')
    fig.colorbar(cf, ax=ax[0])
    ax[0].set_title('contourf potential')
    ax[0].set_xlabel('x axis')
    ax[0].set_ylabel('y axis')

    levels = 15
    cf = ax[1].contourf(edata, levels=levels,cmap='jet')
    fig.colorbar(cf, ax=ax[1])
    ax[1].set_title('contourf |E|')
    ax[1].set_xlabel('x axis')
    ax[1].set_ylabel('y axis')

    plt.show()


    fig.savefig('pointcharges.png')
    fig.tight_layout()
    plt.show()
#Problem1()

#print("________________________________________________________________")

#Problem 2: Make 3D plot for heat problem. Tempstart=100C, 2 ends in ice bath of 0C.

def Problem2_2d():
    import matplotlib.pyplot as plt
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D

# m is the number of space steps
    m = 50
    dcoeff=4e-4
    length=1
# h is the time step
    h = 1e-2
    a = length / m
    c = dcoeff * h / a**2


#temp on bar
    temp_end = 0.
    temp_start = 100.

    temp = np.zeros([m],float)
    temp[0] = temp_end
    temp[1:] = temp_start
    temp[-1]= temp_end


    tempprime = np.zeros([m],float)
    tempprime[0] = temp_end
    tempprime[1:] = temp_start
    tempprime[-1] = temp_end

#info for graphing
    xarr = np.linspace(length,0,m)
    yarr = np.linspace(0,length,m)
    zarr = np.zeros([m,m],float)

#print (y.shape)

    snapshot = np.array ([0.01,0.1,0.5,2,10,50,100,500])

    t = 0.
    t_stop = 501.
    epsilon = 1e-6

    fig, ax = plt.subplots()

    while t < t_stop:
# calculating the new temperature, tempprime, in terms of the old temperature
        for i in range(1,m-1):
            tempprime[i]=temp[i]+ c*(temp[i+1]+temp[i-1]-2*temp[i])


            i+=1
        tempprime[m-1]=tempprime[m-2]


        t += h
        temp, tempprime = tempprime, temp


        for i in range(8):
            if (abs(t - snapshot[i]) < epsilon):
                yarr = tempprime
                ax.plot(xarr,yarr,'b')



    ax.set_title("solving heat equation")
    ax.set_xlabel("position along rod")
    ax.set_ylabel("temperature")
    plt.savefig("heat_example.png")

    plt.show()
#Problem2_2d()

#print("________________________________________________________________________________")
def Problem2_3d():
    import matplotlib.pyplot as plt
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D

# m is the number of space steps
    m = 50
    dcoeff=4e-4
    length=1
# h is the time step
    h = 0.5
    a = length / m
    c = dcoeff * h / a**2


#temp on bar
    temp_end = 0.
    temp_start = 100.

    temp = np.zeros([m],float)
    temp[0] = temp_end
    temp[1:] = temp_start
    temp[-1]= temp_end


    tempprime = np.zeros([m],float)
    tempprime[0] = temp_end
    tempprime[1:] = temp_start
    tempprime[-1] = temp_end

#time information
    t = 0.
    t_stop = 501.
    epsilon = 1e-6

#info for graphing
    xarr = np.linspace(0,length,m)
    yarr = np.linspace(0,t_stop,m)
    zarr = np.zeros([m,m],float)

#print (y.shape)

    snapshot = np.array ([0.01,0.1,0.5,2,10,50,100,500])
    fig, ax = plt.subplots()

    for j in range(m):
# calculating the new temperature, tempprime, in terms of the old temperature
        for i in range(1,m-1):
            tempprime[i]=temp[i]+ c*(temp[i+1]+temp[i-1]-2*temp[i])
            i+=1
        # tempprime[m-1]=tempprime[m-2]
        t += h
        temp, tempprime = tempprime, temp

        zarr[:,j]=tempprime[:]

        print(f'Completed Time {t} of {t_stop}')
        print(np.size(xarr), np.size(yarr), np.size(zarr))

    xdata, ydata = np.meshgrid(xarr,yarr)
    ax = plt.axes(projection='3d')
    surf = ax.plot_surface(xdata, ydata, zarr, rstride=1, cstride=1,cmap='jet', edgecolor='none')
    fig.colorbar(surf, ax=ax)
    ax.set_title('surface')
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')

    plt.savefig("heat_example.png")
    plt.show()
Problem2_3d()

#print("__________________________________________________________________")

#Problem 3:pluck a guitar string,L=.65, c=350, initial position =L/4 and is a triangle, a=.005, h=5e-6,frequency =2000. Apply fft method to amplitude data for x=.025.

def Problem3():
    import math
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    from scipy import fftpack
    from scipy import signal
    import time

    # t0 = time.time()

    c = 350.
# space spacing
    a = 5e-3
    time = 0.25
# time spacing
    h = 5e-6
    L = 0.65
    asize = int((L/a)+1)
    ratio = (c*c*h*h)/(a*a)
    height = 0.1

# 3 = past, present, future
    y = np.zeros([asize,3], float)
    print (y.shape)
    x = np.linspace(0,L,asize)
    print (x.shape)
    print (x)
    end_val = len(x)-1

# initialize the position at the present time
    # y[:,1] = signal.triang(x-L/4,sym=True)
    first_bit = [x[i]*(4*height/L) for i in range((asize//4)+1)]
    print(first_bit)
    first_bit.extend(first_bit[-1]+[x[j]*(-4*height/(3*L)) for j in range(3*asize//4)])
    print(first_bit)
    y[:,1] = np.array(first_bit)
    print(f'y[:,1] = {y[:,1]}')
#print (y[:, 1])


    for i in range(asize):
        if i == 0:
            y[i,2] = 0
        elif i == end_val:#0000:
            y[i,2] = 0
        else:
# initialize the position at a future time
            y[i,2] = y[i,1] + (ratio/2)*(y[i+1,1] + y[i-1,1] - 2*y[i,1])
            print(f'y[i,2] = {y[i,2]}')
# done initialize

    y[:, 0] = np.copy(y[:, 2])
#print (y[:,0])
#print (y[:,1])
#print (y[:,2])

    yarr = np.zeros( (1,asize) )
    yarr[0, :] = np.copy(y[:, 2])
    print (yarr.shape)
    idx = 1

    count = 0
    timesteps = int(time/h)

    print (timesteps)
    for j in range(timesteps):
        y[:, 0] = np.copy(y[:, 1])
        y[:, 1] = np.copy(y[:, 2])
        for i in range(asize):
            if i == 0:
                y[i,2] = 0
            elif i ==end_val :
                y[i,2] = 0
            else:
    # put the position at a future time here
                y[i,2] = 2*y[i,1]-y[i,0]+ ratio*(y[i+1,1]+y[i-1,1]-2*y[i,1])
                print(f'y[i,2] = {y[i,2]}')
        count += 1
        if (count%50 == 0):
            idx += 1
            temp = y[:, 2]
            yarr = np.append(yarr, [y[:, 2]], axis=0)
            print (y[:, 2])
        print(f'Completed Loop {j}')
    fig, ax1 = plt.subplots()
    xdata, ydata = [], []
    ln1, = plt.plot([], [], 'b', animated=True)
    print (type(xdata))

    def init():
        print('Init')
        ax1.set_xlim(0., L)
        ax1.set_ylim(-height*1.1,height*1.1)
        # ax[1].set_xlim(0., 2.)
        # ax[1].set_ylim(-1.,1.)
        return ln1,

    def update(frame):
    #print (frame)
        xdata = x
        ydata = yarr[frame, :]
        print(xdata[100], ydata[100])
        ln1.set_data(xdata, ydata)
        return ln1,

    ani = FuncAnimation(fig, update, frames=int(idx), interval=50, init_func=init, blit=True)
    plt.title("guitar string")
    plt.xlabel("position along string")
    plt.ylabel("displacement")

#fft method
    SamplePeriod = time
    Npoints = time/h
    SampleRate = Npoints/SamplePeriod

    time = np.linspace(0.0, SamplePeriod, Npoints)
    amplitude = y[:,1]
    Yf = fftpack.fft(amplitude)

    freqs = fftpack.fftfreq(len(amplitude)) * SampleRate

    print(f'Max freq = {max(freqs)}')

    for i, f in enumerate(freqs):
        if f > 0:
            i_crit = i
            break

    fig1, ax2 = plt.subplots()
    ax2.stem(freqs[i_crit:], np.abs(Yf[i_crit:])) #[int(i_crit*.90):int(i_crit*1.10)]
    ax2.set_xlabel('Frequency in Hertz [Hz]')
    ax2.set_ylabel('Frequency Domain (Spectrum) Magnitude')
    # ax[1].set_xlim(-SampleRate / 2, SampleRate / 2)

    fig1.savefig("guitar_string.png")

    fig2 = plt.figure()
    plt.plot(freqs[i_crit:], np.abs(Yf[i_crit:]))

    # t1 = time.time()
    # print('Runtime: ',t1 - t0)

    plt.show()

# Problem3()
