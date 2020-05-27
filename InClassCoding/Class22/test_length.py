import math

length = 10
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
dx = x1 - x2
dy = y1 - y2
# need this snippet because the walls are not reflecting
if (abs(dx) > length/2):
    if dx >= 0.:
        dx = dx - length
    else:
        dx = dx + length
              #print ('dx ',dx,x[i],x[j])
if (abs(dy) > length/2):
    if dy >= 0.:
        dy = dy - length
    else:
        dy = dy + length
dr = math.sqrt(dx**2 + dy**2)
print ('dx, dy, dr ',dx, dy, dr)
