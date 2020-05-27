import numpy as np
from scipy import signal as sg
from scipy.io import wavfile

Fs = 44100
#frequency generating
f = 558
time = 5

t = np.linspace(0, time, Fs*time)
#sin wave with amplitude 5000(how loud it is)
y = 5000*np.sin(2 * np.pi * f * t)
#generate y as a 16bit int that it can convert to sound
z = y.astype(np.int16)


# square wave
# y = 100 * sg.square(2 * np.pi * f * x / Fs)
# and with duty cycle
# y = 100 * sg.square(2 * np.pi * f * x / Fs, duty = 0.8) 
# or sawtooth
#y = 10 * sg.sawtooth(2 * np.pi * f * x / Fs)

#make a sound file: file name, listening frequency, function as a 16bit int
wavfile.write('sin2.wav', Fs, z)


