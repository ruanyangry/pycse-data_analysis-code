# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# 定义层流函数
def fF_laminar(Re):
    return 16.0/Re

# 定义湍流函数
def fF_turbulent_unvectorized(Re):
    def func(f):
        return 1/np.sqrt(f)-(4.0*np.log10(Re*np.sqrt(f))-0.4)
    fguess=0.01
    f,=fsolve(func,fguess) # f, 表示浮点数的意思
    return f

#np.vectorize将变量函数变成向量函数
fF_turbulent = np.vectorize(fF_turbulent_unvectorized)

def fanning_friction_factor(Re):
    sigma=1./(1+np.exp(-(Re-3000.0)/450.0))
    f=(1-sigma)*fF_laminar(Re)+sigma*fF_turbulent(Re)
    return f

#Re1=np.linspace(500,3000)
#Re2(np.linspace(3000,10000)
Re=np.linspace(500,10000)
f=fanning_friction_factor(Re)

plt.figure()
plt.plot(Re,f,label='smooth transition',linewidth=2.0,linestyle='-',color='green',alpha=1.0)
#plt.plot(Re1,fF_laminar(Re1),linewidth=4.0,linestyle='--',color='red',alpha=1.0)
#plt.plot(Re2,fF_turbulent(Re2),linewidth=4.0,linestyle='--',color='yellow',alpha=1.0)    
plt.xlabel('Re')
plt.ylabel('$f_F$')
plt.legend(loc='best')
plt.grid(True)
plt.savefig('C:/Users/RY/Desktop/19.jpg',dpi=300)
plt.show()
print('job done')