# _*_ coding: utf-8 _*_

from scipy.special import jn,jn_zeros
import matplotlib.pyplot as plt
import numpy as np

# what is the Biot number
Bi=1

# define functions

def f(x):
    return x*jn(1,x)-Bi*jn(0,x)

# offer value of variable x

X=np.linspace(0,400)

# draw graph

plt.plot(X,f(X),'r',linestyle='-',linewidth=2.0)
plt.savefig('37.jpg',dpi=300)
plt.grid(True)
plt.show()
print('plot done')


# method two integrate ODE functions to solve equations

# import new library
from pycse import *


# define functions

def f(x):
    "functions we want roots for"
    return x*jn(1,x)-Bi*jn(0,x)

def fprime(f,x):
    "df/dx"
    return x*jn(0,x)-Bi*(-jn(1,x))

def el(f,x):
    "events function to find zeros of f"
    isterminal=False
    value=f
    direction=0
    return value,isterminal,direction

# offer value of variables

f0=f(0)
xspan=np.linspace(0,30,200)

# offer args to solve equations

x,fsol,XE,FE,IE=odelay(fprime,f0,xspan,events=[el])

# draw graph

plt.plot(x,fsol,'-.',label='Numerical solution')
plt.plot(xspan,f(xspan),'--',label='Analytical function')
plt.plot(XE,FE,'ro',label='roots')
plt.legend(loc='best')
plt.savefig('37-1.jpg',dpi=300)
plt.show()
print('plot done')

for i,root in enumerate(XE):
    print('root {0} is at {1}'.format(i,root))

# at {1} 需要怎样理解呢？


