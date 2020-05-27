import numpy as np

x=2
def f(x):
    return x**2

def f_1(x):
    return np.gradient(f)
print(f_1(x))
