import math
import random
import numpy as np
import datetime
import matplotlib.pyplot as plt


# some examples with datetime

x = datetime.date.today()
print (x)
print (type(x))
print ("")

x = datetime.date.today()
print (x)
print (x.year)
print (x.month)
print (x.day)
print ("")

y = datetime.timedelta(days=7)
nextweek = x + y
print (nextweek)
print ("")
 
x = datetime.datetime.today()
print (x)
print (x.hour)
print (x.minute)
print (x.second)
print (x.microsecond)
print ("")

# set a date
x = datetime.date(2019, 2, 22)
print (x)
