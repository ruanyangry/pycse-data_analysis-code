# _*_ coding: utf-8 _*_

import numpy as np

# fit a lint to numerical data

x=[0,0.5,1,1.5,2.0,3.0,4.0,6.0,10]
y=[0,-0.157,-0.315,-0.472,-0.629,-0.942,-1.256,-1.884,-3.147]

p=np.polyfit(x,y,1)
print(p)

slope,intercept=p
print(slope,intercept)

# draw graph

import matplotlib.pyplot as plt

# variable xfit include the data in x
xfit=np.linspace(0,10)
yfit=np.polyval(p,xfit)

plt.plot(x,y,'bo',label='raw data')
plt.plot(xfit,yfit,'r-.',label='fit line')
plt.legend(loc='best')
plt.xlabel('X')
plt.ylabel('Y')
#plt.xlim(0,10)
plt.savefig('45.jpg',dpi=300)
plt.show()
print('plot done')


# Linear least squares fitting with linear algebra

x=np.array([0,0.5,1,1.5,2.0,3.0,4.0,6.0,10])
y=np.array([0,-0.157,-0.315,-0.472,-0.629,-0.942,-1.256,-1.884,-3.147])

A=np.column_stack([x**0,x])
M=np.dot(A.T,A)
b=np.dot(A.T,y)

11,slope1=np.dot(np.linalg.inv(M),b)
12,slope2=np.linalg.solve(M,b)

print(11,slope1)
print(12,slope2)

# plot data and fit

plt.plot(x,y,'bo')
plt.plot(x,np.dot(A,[11,slpoe1]),'r--')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('45-1.jpg',dpi=300)
plt.show()
print('plot done')



