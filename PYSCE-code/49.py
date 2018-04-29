# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2)
y1=x
y2=x**2
y3=x**3

plt.plot(x,y1,x,y2,x,y3)
xL=plt.xlabel('x')
yL=plt.ylabel('f(x)')
plt.title('plots of y=x^n')
plt.legend(['x','x^2','x^3'],loc='best')
plt.grid(True)
plt.savefig('49-1.jpg',dpi=300)

fig=plt.gcf()

plt.step(fig,'size_inches'(4,6))
plt.savefig('49-2.jpg',dpi=300)

# set lines to dash

from matplotlib.lines import Line2D
for o in fig.findobj(Line2D):
    o.set_linestyle('--')

# set(allaxes,'FontName','Arial','FontWeight','Bold','LineWidth',2,'FontSize',14)


