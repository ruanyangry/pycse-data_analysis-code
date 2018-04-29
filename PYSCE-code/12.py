# _*_ coding: utf-8 _*_

import numpy as np
from scipy.integrate import quad

def f_(z):
    def integrand(t):
        return np.tan(t**3)
    return quad(integrand,0,z**2)

f=np.vectorize(f_)

x=np.linspace(0,1)

h=1e-7

#dfdx=np.imag(f(x+complex(0,h)))/h
dfdx_analytical=2*x*np.tan(x**6)

import matplotlib.pyplot as plt

#plt.plot(x,dfdx,x,dfdx_analytical,'r--')
plt.plot(x,dfdx_analytical,'ro',linewidth=5.0)
plt.xlabel('X')
plt.ylabel('dfdx_analytical')
plt.title('complex method not waork')
plt.savefig('12.jpg',dpi=300)
plt.show()
print('job done')