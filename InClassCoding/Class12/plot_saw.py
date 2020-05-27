import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

time        = np.arange(0, 1, 0.01);
amplitude   = signal.sawtooth(2 * np.pi * 5 * time + np.pi)
plt.plot(time, amplitude)
plt.title('title')
plt.xlabel('time (s)')
plt.ylabel('amplitude (V)')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()
