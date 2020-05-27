#Cassandra Bodin
#Phys 305
#Homework 7
#due 3/14

#run by "python hmk7_bodin.py"

#Problem 1: analyze data in hmk_data.txt using DFT and FFT

def Problem1():
#import libraries
    from scipy import fftpack
    from scipy import signal
    import numpy as np
    import matplotlib.pyplot as plt

#function for dft
    def DFT():

#read file
        f = open('hmk_data.txt','r')

        time = np.array([])
        amplitude = np.array([])

        for line in f:
            s = line.split()
            time = np.append(time,float(s[0]))
            amplitude = np.append(amplitude,float(s[1]))

#info for dft
        nsamples = np.size(time)
        h = time[1]-time[0]
        samplingf = nsamples / (nsamples*h)

#implement dft
        frequency = np.array([])
        Y = np.zeros((nsamples,), dtype=complex)
        for n in range(nsamples):
            frequency = np.append(frequency,n/(nsamples*h))
            for m in range(nsamples):
                Y[n] += amplitude[m]*np.exp((-2*np.pi*1j*m*n)/nsamples)


#plot
        fig, ax = plt.subplots(2, 1)
        ax[0].plot(frequency[0:100], Y.imag[0:100])
        ax[0].set(title='dft-imag', xlabel='frequency (Hz)', ylabel='amplitude (V)')
        ax[0].grid()

        ax[1].plot(frequency[0:100], Y.real[0:100])
        ax[1].set(title='dft-real', xlabel='frequency (Hz)', ylabel='amplitude (V)')
        ax[1].grid()

        fig.savefig('dft.png')

        #plt.show() #uncomment to plot individual graph
    DFT() #uncomment to call function

#***************************************************************************
#function for fft
    def FFT():

#read file
        f = open('hmk_data.txt','r')

        time = np.array([])
        amplitude = np.array([])

        for line in f:
            s = line.split()
            time = np.append(time,float(s[0]))
            amplitude = np.append(amplitude,float(s[1]))

#info for fft
        SamplePeriod = 1
        Npoints = 10000
        h = 0.0001
        SampleRate = Npoints/SamplePeriod
        YM = fftpack.fft(amplitude)
        frequency = np.arange(Npoints)/Npoints/h
#plot
        fig, ax = plt.subplots(2,1)

        ax[1].plot (frequency[0:100], YM.real[0:100], 'b')
        ax[1].set(title='fft-real', xlabel='frequency (Hz)', ylabel='amplitude (V)')
        ax[1].grid()

        ax[0].plot (frequency[0:100], YM.imag[0:100], 'b')
        ax[0].set(title='fft-imag', xlabel='frequency (Hz)', ylabel='amplitude (V)')
        ax[0].grid()
        fig.savefig('fft7.1.png')

        #plt.show() #uncomment to plot individual graph
    FFT() #uncomment to call function

    plt.show('all') #plot all graphs in function
Problem1() #uncomment to call function

#_________________________________________________________________________

#Problem 2: Record voice using Audacity (bodin.wav). Use FFT to analyze your voice

def Problem2():
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    from scipy import signal as sg
    from scipy.io import wavfile
    from scipy import fftpack

    rate, amplitude = wavfile.read('bodin.wav','r') #note bodin.wav is me whistling

#info for fft
    SamplePeriod = 1
    Npoints = len(amplitude)
    h = 1/44100
    SampleRate = Npoints/SamplePeriod
    YM = fftpack.fft(amplitude)
    frequency = np.arange(Npoints)/Npoints/h
#plot
    fig, ax = plt.subplots()

    ax.plot (frequency, YM, 'b')
    ax.plot (frequency,amplitude)
    ax.set(title='fft', xlabel='frequency (Hz)', ylabel='amplitude (V)')

    fig.savefig('fft7.2.png')

    plt.show()
Problem2()

#__________________________________________________________________________

#Problem 3: use differential eq method and fft for V(x) = (1/p)*k*(x**p) and F(x)=m*a(x)=-k*(x**(p-1)). Where p = 4, m = 1, k=200, h = 0.005, t=np.arange[0,11]

def Problem3():
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    from scipy import signal as sg
    from scipy.io import wavfile
    from scipy import fftpack

#using verlet method to find
    def Verlet():
        
        h = .0005
        t_final = 10
        t_initial = 0
        t = t_initial
        count = 0

#initial values
        p = 4 #change to 2 to check that its like a SHO
        m = 1
        k=200.
        x1 = 0.5
        x=x1
        v1=0.
        v=v1


#variables for graphing
        xarr = np.array([])
        yarr = np.array([])
        xarr = np.append(xarr,t)
        yarr = np.append(yarr,x)


#impliment verlet method
        while (t < t_final):
#initial acceleration
            a=(-k/m)*(x**(p-1))
#position values 
            x += v*h +(.5)*a*h**2

#new acceleration values
            a1 = (-k/m)*(x**(p-1))

#velocity values -> calculate v
            v += (h/2)*(a1+a)

#graphing values                                          
            xarr = np.append(xarr,t)
            yarr = np.append(yarr,x)
            count += 1
  
            t = t+h

#export data to .txt file
        f=open('hmk7_data.txt','w')
        n=len(xarr)
        for i in range(n):
            f.write(str(xarr[i])+' '+str(yarr[i])+"\n")
        f.close()

#now plot
        fig, ax = plt.subplots()

#plot of the orbit, comment out and uncomment next section to see energy graph
        ax.plot (xarr, yarr, 'b')
        ax.set(title='Verlet', xlabel='time', ylabel='x values')
        ax.grid()
        fig.savefig('Verlet7.png')

        #plt.show()
    Verlet()
        

    def FFT():

#read file
        f = open('hmk7_data.txt','r') #import a file that I wrote that has time and amplitude values

        time = np.array([])
        amplitude = np.array([])

        for line in f:
            s = line.split()
            time = np.append(time,float(s[0]))
            amplitude = np.append(amplitude,float(s[1]))

#info for fft
        SamplePeriod = 1
        Npoints = len(time)
        h = 0.0005
        SampleRate = Npoints/SamplePeriod
        YM = fftpack.fft(amplitude)
        frequency = np.arange(Npoints)/Npoints/h
#plot
        fig, ax = plt.subplots()

        ax.stem (frequency[0:100], np.abs(YM[0:100]), 'b')
        ax.set_xlabel('Frequency in Hertz [Hz]')
        ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
        fig.savefig('fft7.png')

        #plt.show() #uncomment to plot individual graph
    FFT() #uncomment to call function

    plt.show('all')
Problem3()
