import math

def fprime (arg):
      value = -K*(arg-Tout)
#      value = float(arg)**2
#      value = float(arg)
      return value

t = 0.
h = 1e-2
print ('stepsize is ', h)
duration = 15.
K = 0.1
# f is the temperature as a function of time
# fprime is the derivative
Tinit = 85.
Tfinal = 75.
temp = Tinit
Tout = 25.


while (temp > Tfinal):
      temp = temp + h*fprime(temp)
      t = t + h

print ('final temperature is ',temp)
print ('final time (t-h) is ',t-h)
print ('final time (t+h) is ',t)

temp = Tinit
t = 0
while (temp > Tfinal):
      temp = temp + h*fprime(temp)
      temp_old = temp
      t_old = t
      t = t + h

t_last = t_old - (Tfinal-temp_old)/fprime(temp_old)
print ('final temperature is ',Tfinal)
print ('final time is ',t_last)

# analytic solution is
#temp = Tout + (Tinit - Tout)*math.exp(-K*duration)
#print ('final temperature is ',temp)

