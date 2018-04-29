# _*_ coding: utf-8 _*_

from pycse import regress
import numpy as np

time=np.array([0.0,50.0,100.0,150.0,200.0,250.0,300.0])
Ca=np.array([50.0,38.0,30.6,25.6,22.2,19.5,17.4])*1e-3

T=np.column_stack([time**0,time,time**2,time**3,time**4])

alpha=0.05
p,pint,se=regress(T,Ca,alpha)
print(pint)

# new one

import numpy as np
from scipy.stats.distributions import t

time=np.array([0.0,50.0,100.0,150.0,200.0,250.0,300.0])
Ca=np.array([50.0,38.0,30.6,25.6,22.2,19.5,17.4])*1e-3

T=np.column_stack([time**0,time,time**2,time**3,time**4])

p,res,rank,s=np.linalg.lstsq(T,Ca)
# the parameter are now in p

# compute the confidence intervals

n=len(Ca)
k=len(p)

sigma2=np.sum((Ca-np.dot(T,p))**2)/(n-k) # RMSE

C=sigma2*np.linalg.inv(np.dot(T.T,T))  # covariance matrix
se=np.sqrt(np.diag(C)) # standard error

alhpa=0.05 #100*(1-alpha) confidence level

sT=t.ppf(1.0-alpha/2.0,n-k) # student T multiplier
CI=sT*se

for beta,c1 in zip(p,CI):
    print('{2:1.2e} {0:1.4e} {1:1.4e}'.format(beta-c1,beta+c1,beta))

SS_tot=np.sum((Ca-np.mean(Ca))**2)
SS_err=np.sum((np.dot(T,p)-Ca)**2)

Rsq=1-SS_err/SS_tot
print('R^2 = {0}'.format(Rsq))

# plot fit

import matplotlib.pyplot as plt

plt.plot(time,Ca,'bo',label='Raw data')
plt.plot(time,np.dot(T,p),'r-',label='fit')
plt.xlabel('Time')
plt.ylabel('Ca (mol/L)')
plt.legend(loc='best')
plt.savefig('58.jpg',dpi=300)
plt.show()
print('plot done')
print('I will fight for myself')