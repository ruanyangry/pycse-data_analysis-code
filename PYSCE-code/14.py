# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    if x < 0 :
        return 0
    elif (x >=0) & (x < 1):
        return x
    elif(x >=1) & (x < 2):
        return 2.0-x
    else:
        return 0
    
x = np.linspace(-2,6)
y = [f1(xx) for xx in x]

plt.scatter(x,y,color='green',marker='o')
plt.savefig('14.jpg',dpi=300)
plt.show()
print('job done')