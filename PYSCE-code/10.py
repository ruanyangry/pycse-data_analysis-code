# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

N = 101
L = 2*np.pi

x=np.arange(0.0,L,L/float(N))

y=np.sin(x)+0.05*np.random.random(size=x.shape)
dy_analytical = np.cos(x)

if N%2 == 0 :
    k =np.asarray(list(range(0,N//2))+[0]+list(range(-N//2+1,0)),np.float64)
else:
    k=np.asarray(list(range(0,(N-1)//2))+[0]+list(range(-(N-1)//2,0)),np.float64)

k *= 2*np.pi/L

fd = np.real(np.fft.ifft(1.0j*k*np.fft.fft(y)))

plt.plot(x,y,label='function',linestyle='-.',linewidth=3.0,color='green',alpha=1.0)
plt.plot(x,dy_analytical,label='analytical der',linewidth=3.0,color='black',alpha=1.0,linestyle='--')
#plt.plot(x,fd,label='fft der',color='red',alpha=1.0,marker='o') 这个是线图
plt.scatter(x,fd,label='fft der',color='red',alpha=1.0,marker='D') # 我将其转化成散点图
plt.xlim(0,6)
plt.legend(loc='best')
plt.savefig('10.jpg',dpi=300)
plt.show()
print('job done')