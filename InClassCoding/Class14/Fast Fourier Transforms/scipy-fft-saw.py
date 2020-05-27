from scipy import fftpack
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

SamplePeriod = 1
Npoints = 10000
h = 0.0001
SampleRate = Npoints/SamplePeriod

time = np.linspace(0.0, SamplePeriod, Npoints)
amplitude = signal.sawtooth(2 * np.pi * 5 * time + np.pi)
YM = fftpack.fft(amplitude)

frequency = np.arange(Npoints)/Npoints/h

fig, ax = plt.subplots(2,2)
ax[0,0].plot (time, amplitude, 'b')
ax[0,0].set(title='title', xlabel='time', ylabel='amplitude')
ax[0,0].grid()

ax[0,1].plot (frequency[0:100], YM.real[0:100], 'b')
ax[0,1].set(title='title', xlabel='frequency (Hz)', ylabel='amplitude (V)')
ax[0,1].grid()

ax[1,0].plot (frequency[0:100], YM.imag[0:100], 'b')
ax[1,0].set(title='title', xlabel='frequency (Hz)', ylabel='amplitude (V)')
ax[1,0].grid()

plt.show()
