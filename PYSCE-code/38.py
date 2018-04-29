#　_*_ coding: utf-8 _*_

import numpy as np
from scipy.optimize import fsolve

# solve two equations together
# y=x**2
# y=8-x**2

# define functions

def objective(X):
    x,y=X
    z1=y-x**2
    z2=y-8+x**2
    return [z1,z2]

# initial guesses

x0,y0=1,1
guess=[x0,y0]

# solve equations

sol=fsolve(objective,guess)
print(sol)

# offer another guesses

x0,y0=-1,-1
guess=[x0,y0]

# solve equations

sol=fsolve(objective,guess)
print(sol)
