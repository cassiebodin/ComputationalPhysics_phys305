import math

def fprime (xarg, targ):
      value = -xarg**3 + math.sin(targ)
      return value

t1 = 0.
t2 = 10.
h = 1e-2
print ('t1 t2 = ',t1, t2)
print ('stepsize is ', h)

v = 0
t = t1
while (t < t2):
      k1 = h*fprime(x, t)
      k2 = h*fprime(x+k1/2, t+h/2)
      x = x + k2
      t = t + h

print ('final x, t is  ',x, t-h)

