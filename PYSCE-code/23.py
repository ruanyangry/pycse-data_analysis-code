# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt
import numpy as np

@np.vectorize  #需要加上这句话
def wilkinson(x):
    p=np.prod(np.array([x-i for i in range(1,21)]))
    return p

x=np.linspace(0,21,1000)
plt.plot(x,wilkinson(x),'r--',linewidth=3.0)
plt.grid(True)
plt.ylim([-5e13,5e13])
plt.xlim(0,20)
plt.savefig('C:/Users/RY/Desktop/23.jpg',dpi=300)
plt.show()
print('job done')
