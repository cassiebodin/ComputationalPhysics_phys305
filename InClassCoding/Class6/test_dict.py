earth = {'radius' : 6378, 'mass' : 6.0e24, 'distance' : 150e6}

print (type(earth))

print (earth)

print (earth['distance'])

earth['orbit'] = 365.

print (earth)

del earth['mass']

print (earth) 
