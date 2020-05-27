import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal as sg
from scipy.io import wavfile

Fs = 44100
f = 440
time = 5

t = np.linspace(0, time, Fs*time)
rate, y = wavfile.read('mars7.wav','r')

fig, ax = plt.subplots()

ax.plot (y[0:1000], 'b')

ax.set(title='title', xlabel='x axis', ylabel='y axis')

ax.grid()

#fig.savefig("sine.png")

plt.show()


