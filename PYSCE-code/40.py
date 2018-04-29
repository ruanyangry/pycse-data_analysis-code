# _*_ coding: utf-8 _*_

import numpy as np

n1=30         #students in class A
x1=78.0       #average grade in class A
s1=10.0       #std dev of exam grade in class A

n2=25         #students in class B
x2=85.0       #average grade in class B
s2=15.0       #std dev of exam grade in class B

# the standard error of the difference between in the average

SE=np.sqrt(s1**2/n1+s2**2/n2)

# compute DOF

DF=(n1-1)+(n2-1)

print('SE=',SE,'DF=',DF)

# calculate t-score

tscore=np.abs(((x1-x2)-0)/SE)
print(tscore)

# calculate t-value

from scipy.stats.distributions import t

# set confident level equal c1
c1=0.95
alpha=1-c1
t95=t.ppf(1.0-alpha/2.0,DF)

print(t95)

# set confident level equal c1
c1=0.94
alpha=1-c1
t95=t.ppf(1.0-alpha/2.0,DF)

print(t95)

f=t.cdf(tscore,DF)-t.cdf(-tscore,DF)
print(f)

