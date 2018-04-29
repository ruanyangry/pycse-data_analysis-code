# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

# read data from .txt file

data=np.loadtxt('PT.txt',skiprows=2)

# set file data to variable T,P
# T corresponding to data file row 3
# P corresponding to data file row 4

T=data[:,3]
P=data[:,4]

# draw graph

plt.plot(T,P,'k.')
plt.xlabel('Temperature')
plt.ylabel('Pressure')
plt.savefig('41.jpg',dpi=300)
plt.show()
print('plot down')

# fit the P vs T

A=np.vstack([T**0,T]).T
b=P

x,res,rank,s=np.linalg.lstsq(A,b)
intercept,slope=x

print('b,m=',intercept,slope)

n=len(b)
k=len(x)

sigma2=np.sum((b-np.dot(A,x))**2)/(n-k)

C=sigma2*np.linalg.inv(np.dot(A.T,A))
se=np.sqrt(np.diag(C))

from scipy.stats.distributions import t

alpha=0.05

sT=t.ppf(1-alpha/2.0,n-k)
CI=sT*se

print('CI = ',CI)

for beta,c1 in zip(x,CI):
    print('[{0} {1}]'.format(beta-c1,beta+c1))

# average

ybar=np.mean(P)
SStot=np.sum((P-ybar)**2)
SSerr=np.sum((P-np.dot(A,x))**2)
R2=1-SSerr/SStot

print(R2)

# draw graph

plt.figure()
plt.clf()
plt.plot(T,P,'k.',T,np.dot(A,x),'b-')
plt.xlabel('Temperature')
plt.ylabel('Pressure')
plt.title('R^2 = {0:1.3f}'.format(R2))
plt.savefig('41-1.jpg',dpi=300)
plt.show()
print('plot done')

# calculate residuals

residuals=P-np.dot(A,x)

# draw graph

plt.figure()
f,(ax1,ax2,ax3)=plt.subplots(3)

ax1.plot(T,residuals,'ko')
ax1.set_xlabel('Temperature')

run_order=data[:,0]
ax2.plot(run_order,residuals,'ko')
ax2.set_xlabel('run order')

ambientT=data[:,2]
ax3.plot(ambientT,residuals,'ko')
ax3.set_xlabel('ambient temperature')

plt.tight_layout()
plt.savefig('41-2.jpg',dpi=300)
plt.show()

print('plot done')

# judge the correlations with residual[i] and residuals[i-1]
# if they have no relations, comfire that model is good

plt.figure()
plt.clf()
plt.plot(residuals[1:-1],residuals[0:-2],'ko')
plt.xlabel('residual[i]')
plt.ylabel('residual[i-1]')
plt.savefig('41-3.jpg',dpi=300)
plt.show()
print('plot done')

