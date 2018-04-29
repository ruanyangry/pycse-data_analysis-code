# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi)

#plt.figure(figsize=(4,6))
#plt.plot(x,np.sin(x),lw=2,color='r',marker='o',mec='k',mfc='b')
#mec='k' 在marker='o'上增加了黑色圈
#mfc='b' 圆圈中的颜色设为蓝色
plt.plot(x,np.sin(x),lw=2,color='r',marker='o',mec='k',mfc='blue')

plt.xlabel('x data',fontsize=12,fontweight='bold')
plt.ylabel('y data',fontsize=12,fontstyle='italic',color='b')
plt.xlim(-0.2,6.2)
plt.ylim(-1.05,1.05)
plt.tight_layout() # make the axis best fit the figure
plt.grid(True)
#plt.savefig('C:/Users/RY/Desktop/46.jpg',dpi=300)
plt.show()
print('plot done')