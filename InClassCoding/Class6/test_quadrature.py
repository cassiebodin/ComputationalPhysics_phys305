import math

def f (arg):
      value = float(arg)**2 + math.cos(arg)
      return value


x = [-0.3399810435848563,0.3399810435848563,-0.8611363115940526,0.8611363115940526]
w = [0.6521451548625461,0.6521451548625461,0.3478548451374538,0.3478548451374538]

lower = -1.
upper = 1.
A=0.

for i in range(4):
      A+=w[i]*f(x[i])

print ('integral between ', lower, ' ', upper, ' ',  A)

