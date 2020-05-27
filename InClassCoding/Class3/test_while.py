# examples of while loops

# note that blocks of code are determined by line indentation

temperature = 105.
while temperature > 100.:
    temperature = temperature - 0.5
    print (temperature)
print ("")

k1, k2 = 0, 1
print (k1, k2)
while k1 < 20:
    k1, k2 = k2, k1 + k2
    print (k1, k2)
print ("")

# use of simultaneous assignments
x = 5
y = 10
print (x, y)
x, y = y, x
print (x, y)

print ("")
x = 5
y = 10
print (x, y)
x = y
y = x
print (x, y)
