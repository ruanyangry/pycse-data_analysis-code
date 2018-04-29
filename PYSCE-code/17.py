# _*_ coding: utf-8 _*_

import numpy as np
from scipy.optimize import fsolve # fsolve对非线性方程组进行求解
import matplotlib.pyplot as plt

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

Re1=np.linspace(100,3000)
f1=fF_laminar(Re1)

Re2=np.linspace(3000,10000)
f2=fF_turbulent(Re2)

plt.figure(1)
plt.clf()
plt.title('judge laminar or turbulent flow')
plt.plot(Re1,f1,label='laminar',color='green',linewidth=4.0,alpha=1.0)
plt.plot(Re2,f2,label='turbulent',color='red',linewidth=4.0,alpha=1.0)
plt.xlabel('Re')
plt.legend(loc='best')
plt.grid(True)
plt.savefig('17.jpg',dpi=300)
plt.show()
print('job done')

