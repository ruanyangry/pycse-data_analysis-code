# _*_ coding: utf-8 _*_

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# unit definitions

m=1.0
L=m**3/(1000.0)
mol=1.0
s=1.0

# provide data

Cao=2.0*mol/L
V=10.0*L
nu=0.5*L/s
k=0.23*L/mol/s

# define function
# variable : Ca

def func(Ca):
    return V-nu*(Cao-Ca)/(k*Ca**2)

# offer concentration variable
c=np.linspace(0.001,2)*mol/L

# draw graph
plt.plot(c,func(c),'r',linestyle='--',linewidth=4.0)
plt.xlabel('C (mol/m^3)')
plt.ylabel('V')
plt.ylim([-0.1,0.1])
plt.savefig('31.jpg',dpi=300)
plt.show()
print('job done')

# solve the equation

from scipy.optimize import fsolve

cguess=500
c,=fsolve(func,cguess)
print(c)
print(func(c))
print(func(c)/(mol/L))

print('solve done')
