mystring = 'hello world'
print (type(mystring))

mystring = 'hello' + " world"

print(mystring[1:4])

print(mystring.upper())

print(mystring.startswith('hello'))

print(len(mystring))

print(mystring.replace('hello','goodbye cruel'))
mystring2 = mystring.replace('hello','goodbye')
print (mystring2)

pi = 3.14
print("the value of pi is " + str(pi))

print(mystring.count('o'))

print(mystring.count('O'))

print(mystring.index('o'))

#print(mstring.index('O'))

print(mystring.isalpha())

print(mystring.isdigit())

print(mystring.isspace())

mystring='green eggs and ham'

mywords=mystring.split()
print(mywords)
print (type(mywords))

mystring2=' '.join(mywords)
print(mystring2)

print(list(mystring2))

for i in mystring2:
    print (i)
