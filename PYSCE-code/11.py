# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(3*x)*np.log(x)

x = 0.7
h=1e-7

# analytical derivative 貌似下式是对函数求偏导

dfdx_a = 3*np.cos(3*x)*np.log(x)+np.sin(3*x)/x

# finite difference 有限差分

dfdx_fd = (f(x+h)-f(x))/h

# central difference 中心差分

dfdx_cd = (f(x+h)-f(x-h))/(2*h)

# complex method 复平面方法

dfdx_I = np.imag(f(x+np.complex(0,h))/h)

print(dfdx_a)
print(dfdx_fd)
print(dfdx_cd)
print(dfdx_I)

print('job done')


