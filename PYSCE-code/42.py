# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

# first for addition and subtraction

N=100           # Numbers of samples of parameters

A_mu=2.5
A_sigma=0.4

B_mu=4.1
B_sigma=0.3

A=np.random.normal(A_mu,A_sigma,size=N)
B=np.random.normal(B_mu,B_sigma,size=N)

p=A+B
m=A-B

# draw graph

plt.hist(p)
plt.hist(m)
plt.savefig('42.jpg',dpi=300)
plt.show()
print('plot done')

print(np.std(p))
print(np.std(m))
print(np.sqrt(A_sigma**2+B_sigma**2))  #the analytical std dev

# second multiplication

F_mu=25.0
F_sigma=1

x_mu=6.4
x_sigma=0.4

F=np.random.normal(F_mu,F_sigma,size=N)
x=np.random.normal(x_mu,x_sigma,size=N)

t=F*x

# draw graph
plt.hist(t)
plt.show()
plt.savefig('42-1.jpg',dpi=300)
print('plot done')

print(np.std(t))
print(np.sqrt((F_sigma/F_mu)**2+(x_sigma/x_mu)**2*F_mu*x_mu))

print('job done')