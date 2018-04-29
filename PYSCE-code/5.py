import numpy as np
from pylab import *
import time

x = np.linspace(0.78,0.79,100000)
y = np.sin(x)
dy_analytical = np.cos(x)

tf1 = time.time()
dyf = [0.0]*len(x)
for i in range(len(y)-1):
    dyf[i]=(y[i+1]-y[i])/(x[i+1]-x[i])
    dyf[-i]=(y[-i]-y[-2])/(x[-i]-x[-2])

print('Forward differences took %f seconds'%(time.time()-tf1))

tb1 = time.time()
dyb = [0.0]*len(x)
dyb[0] = (y[0]-y[1])/(x[0]-x[1])
for i in range(1,len(y)):
    dyb[i]=(y[i]-y[i-1])/(x[i]-x[i-1])

print('Backward difference took %f seconds'% (time.time()-tb1))

tc1=time.time()
dyc=[0.0]*len(x)
dyc[0]=(y[0]-y[1])/(x[0]-x[1])
for i in range(1,len(y)-1):
    dyc[i]=(y[i+1]-y[i-1])/(x[i+1]-x[i-1])
    dyc[-i]=(y[-i]-y[-2])/(x[-i]-x[-2])

print('Centered difference took %f seconds'%(time.time()-tc1))

plt.plot(x,dy_analytical,label='analytical derivative')
plt.plot(x,dyf,'--',label='forward')
plt.plot(x,dyb,'--',label='backard')
plt.plot(x,dyc,'--',label='centered')

plt.legend(loc='lower left')
plt.savefig('5.jpg',dpi=300)
plt.show()
print('job done')
