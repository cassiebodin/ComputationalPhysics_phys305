import math
#import random
import matplotlib.pyplot as plt
import numpy as np


# some examples with matplotlib
# see https://matplotlib.org/users/examples_index.html

x = np.arange(0.001, 2.0, 0.001)
y = np.sin(1./(x * (2-x))) * np.sin(1./(x * (2-x)))
plt.plot(x, y)

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.savefig("example.png")
plt.show()



