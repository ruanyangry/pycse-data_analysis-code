# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()

ax=fig.add_subplot(111)
ax.plot(np.random.rand(100))
ax.set_title('Click somewhere')

def onclick(event):
    print(event)
    ax=plt.gca()
    a.set_title('x={0:1.2f} y={1:1.2f}'.format(event.xdata,event.ydata))
    if event.key == 'shift+control':
        color='red'
    elif event.key == 'shift':
        color='yellow'
    else:
        color='blue'
    ax.plot([event.xdata],[event.ydata],'o',color=color)
    ax.figure.canvas.draw() # this line is critical to change the title
    plt.savefig('55.jpg',dpi=300)

cid=fig.canvas.mpl_connect('button_press_event',onclick)
plt.savefig('55.jpg',dpi=300)
plt.show()
print('plot down')