# _*_ coding: utf-8 _*_

from scipy.integrate import dblquad
import numpy as np

def integrand(y,x):
    return y*np.sin(x)+x*np.cos(y)

ans,err=dblquad(integrand,np.pi,2*np.pi,
                lambda x:0,
                lambda x:np.pi)

print(ans)