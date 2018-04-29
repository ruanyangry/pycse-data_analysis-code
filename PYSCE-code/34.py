# _*_ coding: utf-8 _*_

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# define functions

def dxdL(x,Lambda):
    return -x**2/(-5.0+2*Lambda*x)

# declare constants

x0=6.0/5.0
Lspan=np.linspace(0,1,100)

# solve equations
# offer three args for function odeint

x=odeint(dxdL,x0,Lspan)

# draw graph

plt.plot(Lspan,x,'r',linestyle='-.',linewidth=4.0)
#plt.xlabel('$\lambda\$')
plt.xlabel('lambda')
plt.ylabel('x')
plt.xlim(0.0,1.0)
plt.ylim(1.2,2.0)
plt.grid(True)
plt.savefig('34.jpg',dpi=300)
plt.show()
print('plot done')

# define new functions

def dxdL(x,Lambda):
    return (5*x-10)/(2*x-5*Lambda)

# declare constants

x0=-2
Lspan=np.linspace(0,1,100)

# solve equations
# offer three args for function odeint

x=odeint(dxdL,x0,Lspan)

# draw graph
plt.plot(Lspan,x,'g',linestyle='-.',linewidth=4.0)
plt.xlabel('lambda')
plt.ylabel('x')
plt.grid(True)
plt.savefig('35.jpg',dpi=300)
plt.show()
print('plot done')
