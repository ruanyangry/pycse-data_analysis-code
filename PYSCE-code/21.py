#_*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

x =np.array([0,0.5,1,1.5,2.0])
y=x**3

x2=np.linspace(0,2,50)
y2=x2**3

plt.plot(x,y,'r-',linewidth=3.0,label='5 points')
plt.plot(x2,y2,'g--',linewidth=3.0,label='50 points')
plt.legend(loc='best')
plt.grid(True)
plt.savefig('C:/Users/RY/Desktop/21.jpg',dpi=300)
plt.show()
print('job done')
