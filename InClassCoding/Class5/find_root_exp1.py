import math

def fun(x):
    value = math.exp(-x) + x - 2
    return value

a = 0.
b = 2.
i = 0

while (math.fabs(a-b) > 1.e-6):
    i += 1
    mid = 0.5 * (a+b)
    if (fun(a)*fun(mid) < 0):
        a = a
        b = mid
    else:
        a = mid
        b = b

print (i, a, b, math.fabs(a-b))
