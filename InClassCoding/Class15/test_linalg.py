import math
import matplotlib.pyplot as plt
import numpy as np

#solve augmented matrix ax=b
a = np.array([ [2, 2, 4], [3, -4, 1], [-1, 4, 1] ])
b = np.array([-8,6,4])
x=np.linalg.tensorsolve(a,b)

print(x)

#Find eigenvalues and vectors for Quantum Mechanics for spin components
hbar = 1

S_x= np.array([ [0,hbar/2], [hbar/2,0]])

lambda_x = np.linalg.eig(S_x)
print (lambda_x)

S_y= np.array([ [0,-1j*hbar/2], [1j*hbar/2,0]])

lambda_y = np.linalg.eig(S_y)
print (lambda_y)

S_z= np.array([ [hbar/2,0], [0,-hbar/2]])
lambda_z = np.linalg.eig(S_z)
print (lambda_z)
