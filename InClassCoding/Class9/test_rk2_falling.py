import math

def fyprime (yarg, targ):
      value = -v
      return value

def fvprime (varg, targ):
      value = -g
      return value

g = -9.8
ymin = 0
ymax = 30
h = 1e-5
t = 0.
y = ymax
v = 0.
v2 = 0.
y2 = 0.

while (y > 0):

      k1 = h*fyprime(y, t)
      k2 = h*fyprime(y+k1/2, t+h/2)
      y = y + k2

      k1 = h*fvprime(v, t)
      k2 = h*fvprime(v+k1/2, t+h/2)
      v = v + k2

      t = t + h

print (t, y, v)

# analytic solution is
t = math.sqrt(-2*(ymin-ymax)/math.fabs(g))
print ('analytic t is ',t)

