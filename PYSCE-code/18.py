# _*_ coding: utf-8 _*_

import numpy as np

x=np.linspace(-4,4)
y=1.0/(1+np.exp(-x/0.1))
plt.figure()
plt.clf()
plt.plot(x,y,label='value',color='green',linewidth=4.0,linestyle='--')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('$\sigma(x)\$')
plt.legend(loc='upper left')
plt.savefig('C:/Users/RY/Desktop/18.jpg',dpi=300)
plt.show()
print('job done')