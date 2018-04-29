# _*_ coding: utf-8 _*_

import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve

# declare constants

k=0.23
nu=10.0
Fao=1.0

# define function

def integrand(Fa):
    return -1.0/(k*Fa/nu)

def func(Fa):
    integral,err=quad(integrand,Fao,Fa)
    return 100.0-integral

# 矢量化函数
# 将普通函数转换成适合函数运算的函数
vfunc=np.vectorize(func)

# draw graph

import matplotlib.pyplot as plt

f=np.linspace(0.001,1)
plt.plot(f,vfunc(f),linestyle='-.',linewidth=4.0,color='red')
plt.xlabel('Molar flow rate')
plt.ylabel('flow rate')
plt.ylim(-200,100)
#plt.ylim([-200,100])
plt.grid(True)
plt.savefig('32.jpg',dpi=300)
plt.show()
print('plot done')

# solve equation

Fa_guess=0.1
Fa_exit,=fsolve(vfunc,Fa_guess)
print('The exit concentration is {0:1.2f} mol/L'.format(Fa_exit/nu))
print('solve done')
