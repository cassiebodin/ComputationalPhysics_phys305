#Cassandra Bodin
#Phys 305
#Hw 2
#run as "python bodin_plot.py"

import matplotlib.pyplot as plt
import numpy as np

    # example simple plot
x = np.linspace(0.,2.,50)
y  = np.exp(x)

fig, ax = plt.subplots()

plt.errorbar(x, y, yerr = np.sqrt(abs(y)),color = 'blue',marker = "None", linestyle = 'None')

    #plots x and y in purple
ax.plot (x, y, color = 'red',marker = ".", linestyle = 'None')


    #Add a title, and x and y axis labels
ax.set(title='Exponential Plot', xlabel='x axis', ylabel='y axis')


    # ads a grid to the graph
ax.grid()

fig.savefig("exp.png")

plt.show()
