import math

### class for 2D vectors ###
class Vector:

	## initialize the vector with its dimensions ##
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
	## calculate the magnitude using the euclidean norm ##
    def magnitude(self):
        fltNorm = math.sqrt(self.x**2 + self.y**2)
        return fltNorm

	## calculate the angle in radians ##
    def angle(self):
        fltAngle = math.atan2(self.y, self.x) # result is between -pi and pi
        return fltAngle

avector = Vector(1.,1.)		# avector is an instance of the Vector class
print avector.x				# x is an attribute of the avector instance
print avector.magnitude()	# magnitude is a method of the Vector class
print avector.angle()		# what is angle in relation to the avector object?
