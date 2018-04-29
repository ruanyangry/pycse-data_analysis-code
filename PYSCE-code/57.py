# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()

ax=fig.add_subplot(111)
ax.plot(np.random.rand(100))
ax.set_title('Move the mouse somewhere and press a key')

def onpress(event):
    print(event.key)
    colors='rgb'
    ax=plt.gca()
    ax.set_title('key={2} at x={0:1.2f} y=1:1.2f}'.format(event.xdata,event.ydata,event.key))
    if event.key=='r':
        color='red'
    elif event.key=='y':
        color='yellow'
    else:
        color='blue'
    ax.plot([event.xdata],[event.ydata],'o',color=color)
    ax.figure.canvas.draw()
    plt.savefig('57.jpg',dpi=300)

cid=fig.canvas.mpl_connect('key_press_event',onpress)
plt.savefig('57.jpg',dpi=300)
plt.show()
print('plot done')