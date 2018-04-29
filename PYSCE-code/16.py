# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

def heaviside(x):
    x=np.array(x)
    if x.shape != ():
        y=np.zeros(x.shape)
        y[x > 0.0]=1
        y[x==0.0]=0.5
    # special case for 0d array(a number)    
    else:
        if x>0:y=1
        elif x==0:y=0.5
        else:y=0
    return y

def f3(x):
    x=np.array(x)
    # first interval
    y1=(heaviside(x)-heaviside(x-1))*x
    # second interval
    y2=(heaviside(x-1)-heaviside(x-2))*(2-x)
    return y1+y2

from scipy.integrate import quad
print(quad(f3,-1,3))

x=np.linspace(-6,6)
plt.plot(x,f3(x),linewidth=4.0,linestyle='--',color='green',alpha=1.0)
plt.xlabel('X value')
plt.ylabel('Y value')
plt.savefig('16.jpg',dpi=300)
plt.show()
print('job done')

      
        