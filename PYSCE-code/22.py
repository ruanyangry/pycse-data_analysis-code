# _*_ coding: utf-8 _*_

from scipy.interpolate import *
from scipy.integrate import quad
import numpy as np

x=[0,0.5,1.0,1.5,2.0]
y=[0,0.125,1.0,3.375,8.0]

f=interp1d(x,y)

#numerical trapezoid method

xfine=np.linspace(0.25,1.75)
yfine=f(xfine)
print(np.trapz(yfine,xfine))

# quadrature with interpolation

ans,err=quad(f,0.25,1.75)
print(ans)