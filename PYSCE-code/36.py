# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

# offer initial x variable

x=np.linspace(-8,4)

# equations

y=x**3+6*x**2-4*x-24

# draw graph

plt.plot(x,y,'r',linestyle='--',linewidth=4.0)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.savefig('36.jpg',dpi=300)
plt.show()
print('plot done')

# find roots number

print(np.sum(y[0:-2]*y[1:-1] < 0))

# method two used ODE function to solve the derivative of initial functions

from pycse import odelay

# define functions

def fprime(f,x):
    return 3.0*x**2+12.0*x-4.0

def event(f,x):
    value=f # we want f =0
    isterminal=False
    direction=0
    return value,isterminal,direction

xspan=np.linspace(-8,4)

f0=-120

X,F,TE,YE,IE=odelay(fprime,f0,xspan,events=[event])
for te,ye in zip(TE,YE):
    print('root round at x ={0:1.3f},f={1:1.3f}'.format(te,float(ye)))

print('ODE done')
