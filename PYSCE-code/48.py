# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi)
y1=np.sin(x)
y2=0.01*np.cos(x)


plt.plot(x,y1,x,y2)
plt.legend(['y1','y2'])
plt.legend(loc='best')
plt.tight_layout() # make the axis best fit the figure
plt.savefig('48-1.jpg',dpi=300)
plt.show()
print('plot done')

# scale the value of y2

plt.figure()
plt.title('scale the value of y2')
plt.plot(x,y1,x,100*y2)
plt.legend(['y1','100*y2'])
plt.legend(loc='best')
plt.tight_layout() # make the axis best fit the figure
plt.savefig('48-2.jpg',dpi=300)
plt.show()
print('plot done')

# double Y-axis

fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(x,y1)
ax1.set_ylabel('y1')
ax2=ax1.twinx()
ax2.plot(x,y2,'r-')
ax2.set_ylabel('y2',color='r')
for t1 in ax2.get_yticklabels():
    t1.set_color('r')
    
plt.tight_layout() # make the axis best fit the figure
plt.savefig('48-3.jpg',dpi=300)
plt.show()
print('plot done')

# use subplots

plt.figure()
f,axes=plt.subplots(2,1)
axes[0].plot(x,y1)
axes[0].set_ylabel('y1')
axes[1].plot(x,y2)
axes[1].set_ylabel('y2')
plt.tight_layout() # make the axis best fit the figure
plt.savefig('48-4.jpg',dpi=300)
plt.show()
print('plot done')