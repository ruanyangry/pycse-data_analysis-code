# _*_ coding: utf-8  _*_

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# initial intercept
# define function

def f(x,y):
    return 2+x+y-x**2+8*x*y+y**3;

def g(x,y):
    return 1+2*x-3*y+x**2+x*y-y*np.exp(x);

def temp(x):
    return 0.0	

# initial x value

x=np.linspace(-5,5,500)

@np.vectorize
def fy(x):
    x0=0.0
    def tmp(y):
        return f(x,y)
    y1,=fsolve(tmp,x0)
    return y1

@np.vectorize
def gy(x):
    x0=0.0
    def tmp(y):
        return g(x,y)
    y1,=fsolve(tmp,x0)
    return y1

# draw graph
#plt.plot(x,fy(x),color='red',linestyle='--',linewidth=4.0,x,gy(x),color='green',linestyle='-.',linewidth=4.0)
plt.plot(x,fy(x),'red',x,gy(x),'green')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(['fy','gy','1.0'],loc='best')
plt.grid(True)
plt.savefig('33.jpg',dpi=300)
plt.show()
print('plot done')

# solve equations

def func(X):
    x,y=X
    return [f(x,y),g(x,y)]

print(fsolve(func,[-10,10]))
print('solve done')



