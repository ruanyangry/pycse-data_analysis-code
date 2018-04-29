# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi)
plt.plot(x,np.sin(x),lw=2,color='r',marker='o',mec='k',mfc='blue')

plt.xlabel('x data',fontsize=12,fontweight='bold')
plt.ylabel('y data',fontsize=12,fontstyle='italic',color='b')

# set all font properties
# set_fontsize 设定横坐标刻度的字体大小
fig=plt.gcf()
for o in fig.findobj(lambda x:hasattr(x,'set_fontname') or hasattr(x,'set_fontweight') or (hasattr(x,'set_fontsize'))):
    o.set_fontname('Arial')
    o.set_fontweight('bold')
    o.set_fontsize(14)

# make anything you can set linewidth to be lw=2
def myfunc(x):
    return hasattr(x,'set_linewidth')

#set_linewidth设定图片上所有线的粗细
for o in fig.findobj(myfunc):
    o.set_linewidth(4)

plt.tight_layout()
plt.grid(True)
plt.savefig('47.jpg',dpi=300)
plt.show()
print('plot down')
