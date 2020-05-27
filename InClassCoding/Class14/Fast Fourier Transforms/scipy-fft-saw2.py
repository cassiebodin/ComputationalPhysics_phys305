from scipy import fftpack
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

SamplePeriod = 1
Npoints = 100
h = 0.01
SampleRate = Npoints/SamplePeriod

time = np.linspace(0.0, SamplePeriod, Npoints)
amplitude = signal.sawtooth(2 * np.pi * 5 * time + np.pi)
Yf = fftpack.fft(amplitude)

freqs = fftpack.fftfreq(len(amplitude)) * SampleRate

fig, ax = plt.subplots()

ax.stem(freqs, np.abs(Yf))
ax.set_xlabel('Frequency in Hertz [Hz]')
ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
ax.set_xlim(-SampleRate / 2, SampleRate / 2)
#ax.set_ylim(-5, 110)

plt.show()


#hw7 problem3???

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
        h = 0.005
        SampleRate = Npoints/SamplePeriod
        Yf = fftpack.fft(amplitude)
        freqs = fftpack.fftfreq(len(amplitude)) * SampleRate
#plot
        fig, ax = plt.subplots()

        ax.stem(freqs[0:50], np.abs(Yf[0:50]))
        ax.set_xlabel('Frequency in Hertz [Hz]')
        ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
        #ax.set_xlim(-SampleRate / 2, SampleRate / 2)

        #plt.show() #uncomment to plot individual graph
    FFT() #uncomment to call function
