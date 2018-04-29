# _*_ coding: utf-8 _*_
# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

x0=2.0/3.0
x1=1.5

w=0.05

D=np.linspace(0,2,500)

sigmaD=1.0/(1.0+np.exp(-(1-D)/w))

x=x0+(x1-x0)*(1-sigmaD)

plt.plot(D,x,'r--',linewidth=3.0)
plt.xlabel('D')
plt.ylabel('X')
plt.grid(True)
plt.ylim(0.0,2.0)
plt.savefig('C:/Users/RY/Desktop/20.jpg',dpi=300)
plt.show()
print('job done')
