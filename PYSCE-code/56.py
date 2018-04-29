# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# the data

x=np.linspace(0,10*np.pi,100)
y=np.sin(x)

# interploating function between points
p=interp1d(x,y,'cubic')

# make the figure

fig=plt.figure()

ax=fig.add_subplot(111)
line, =ax.plot(x,y,'ro-')
marker,=ax.plot([0.5],[0.5],'go',ms=15)
plt.grid(True)

ax.set_title('Move the mouse around')

def onmove(event):
    xe=event.xdata
    ye=event.ydata
    ax.set_title('at x={0} y={1}'.format(xe,p(xe)))
    marker.set_xdata(xe)
    marker.set_ydata(p(xe))
    ax.figure.canvas.draw() # this line is crictial to change the title

cid=fig.canvas.mpl_connect('motion_notify_event',onmove)
plt.savefig('56.jpg',dpi=300)
plt.show()
print('job done')