# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()

ax=fig.add_subplot(111)
ax.plot(np.random.rand(30))
ax.set_title('Click somewhere')

def onclick(event):
    ax.set_title('x={0:1.2f} y={1:1.2f} button={2}'.format(event.xdata,event.ydata,event.button))
    colors='rbg'
    print('button={0} (dblclick={2}).making a {1} dot'.format(event.button, colors[event.button],event.dblclick))
    ms=5 #marker size
    if event.dblclick: # make marker bigger
        ms=10
    ax.plot([event.xdata],[event.ydata],'o',color=colors[event.button],ms=ms)
    ax.figure.canvas.draw()
    plt.savefig('53.jpg',dpi=300)

cid=fig.canvas.mpl_connect('button_press_event',onclick)
plt.show()
