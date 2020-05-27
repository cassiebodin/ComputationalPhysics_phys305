import numpy as np
from scipy import signal as sg
import struct

Fs = 44100
f = 580
time = 5

t = np.linspace(0, time, Fs*time)
y = 5000*np.sin(2 * np.pi * f * t)
print (np.size(t))

# square wave
# y = 100 * sg.square(2 * np.pi * f * x / Fs)
# and with duty cycle
# y = 100 * sg.square(2 * np.pi * f * x / Fs, duty = 0.8) 
# or sawtooth
#y = 10 * sg.sawtooth(2 * np.pi * f * x / Fs)

f = open('sin.wav','wb')

for i in y:
   #print (i)
   #print (type(i))
   j = int(i)
   f.write(struct.pack('h',j))
f.close()

