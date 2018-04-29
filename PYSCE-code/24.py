# _*_ coding: utf-8 _*_

import numpy as np
import time

a=0.0
b=np.pi
N=1000000

h=(b-a)/N #确定积分间隔

x=np.linspace(a,b,N)
y=np.sin(x)

t0=time.time() # 获取初始时间
f=0.0
for k in range(len(x)-1):
    f += 0.5*((x[k+1]-x[k])*(y[k+1]+y[k]))

tf=time.time()-t0 #计算完成之后得到的时间

print('time elapsed = {0} sec'.format(tf))
print(f)

t1=time.time()
Xk=x[1:-1]-x[0:-2]
Yk=y[1:-1]+y[0:-2]

f=0.5*np.sum(Xk*Yk)
tf=time.time()-t1
print('time elapsed = {0} sec'.format(tf))
print(f)

t2=time.time()
f=0.5*np.dot(Xk,Yk)
tf=time.time()-t1
print('time elapsed = {0} sec'.format(tf))
print(f)

              



