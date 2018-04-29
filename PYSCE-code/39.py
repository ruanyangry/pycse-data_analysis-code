# _*_ coding: utf-8 _*_

import numpy as np

# offer data

y=[8.1,8.0,8.1]

# average value

ybar=np.mean(y)

# standard deviration

s=np.std(y,ddof=1)

print(ybar,s)

# calculate confident interval
# define of confident interval
# ybar+T_multiplier*std/sqrt(n)

from scipy.stats.distributions import t

# 95% confident interval
c1=0.95

alpha=1.0-c1

# acquire the length of the array

n=len(y)

T_multiplier=t.ppf(1.0-alpha/2.0,n-1)

c195=T_multiplier*s/np.sqrt(n)

print('T_multiplier={0}'.format(T_multiplier))
print('c195={0}'.format(c195))
print('The true average is between {0} and {1} at a 95% confidence level'.format(ybar-c195,ybar+c195))




