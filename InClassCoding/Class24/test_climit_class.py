import matplotlib.pyplot as plt
import numpy as np
import random

# cl theorem
np.random.seed()
ntrials = 1000
sum1 = np.zeros(ntrials)
sum2 = np.zeros(ntrials)
n=20

# random number generation and summing goes here
for i in range(ntrials):
    for j in range(n):
        r1=random.randint(1,6)
        r2=random.randint(2,5)
        sum1[i] +=r1
        sum2[i] +=r2

fig, ax = plt.subplots(1,2)
ax[0].hist(sum1, bins=100, histtype = 'step', color='b') 
ax[0].set(title='clt', xlabel='sum', ylabel='number')
ax[0].grid()
ax[1].hist(sum2, bins=100, histtype = 'step', color='b') 
ax[1].set(title='clt', xlabel='sum', ylabel='number')
ax[1].grid()
plt.show()




