import numpy as np
import matplotlib.pyplot as plt


def f2(x):
    'fully vectorized version'
    x = np.asarray(x)    # np.asarray()可以直接将任何输入转化成数组进行输出
    y = np.zeros(x.shape)
    y += ((x >=0)&(x <1))*x
    y += ((x >=1)&(x<2))*(2-x)
    return y

print(f2([-1,0,1,2,3,4]))
x = np.linspace(-1,3,50)
plt.scatter(x,f2(x),marker='*')
plt.savefig('15.jpg',dpi=300)
plt.show()
print('job done')