# _*_ coding: utf-8 _*_

from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt

def press(event):
    print('press',event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible=xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()

fig,ax=plt.subplots()

fig.canvas.mpl_connect('key_press_event',press)
ax.plot(np.random.rand(120),np.random.rand(120),'go')
xl=ax.set_xlabel('easy come, easy go')

plt.savefig('54.jpg',dpi=300)
plt.show()
print('plot down')
