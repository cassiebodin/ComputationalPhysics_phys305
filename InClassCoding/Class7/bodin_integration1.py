def Simp():
    #define the function
    def f(x):
        return x**5+2*x**2
#number of steps
    n = 1000
#range [0,2]
    a = 0.
    b = 2.
#define h
    h = (b-a)/n
    x = list()
    fx = list()
    i= 0.
    while i<=n:
        x.append(a+i*h)
        fx.append(f(x[i]))
        i+=1
        result = 0
        i=0
        while i<=n:
            if i ==0 or i ==n:
                result+= fx[i]
            elif i %2!= 0:
                result+=4*fx[i]
            else:
                result+=2*fx[i]
            i+=1
        result = result*(h/3)
        print (result)
Simp()
