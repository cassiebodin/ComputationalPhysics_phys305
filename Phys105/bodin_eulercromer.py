#Cassandra Bodin
 #cassandrabodin@email.arizona.edu
 #4/25/17
 #

def a(k,y,b,vy):
    k = 100
    m = 2
    return (-k*y +b*vy)/m


b = input("Enter a value for b:\n")

dt = .01
y = 2.
v = 0.

for i in range(200):
    y += v*dt
    vy += a(k,y,b,vy)*dt
