import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,1000)
y = np.sin(x)
dy_analytical = np.cos(x)

dy = np.zeros(y.shape,np.float)
dy[0:-1]=np.diff(y)/np.diff(x)
dy[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])

dy2 = np.zeros(y.shape,np.float)
dy2[1:-1]=(y[2:]-y[0:-2])/(x[2:]-x[0:-2])

dy2[0]=(y[1]-y[0])/(x[1]-x[0])
dy2[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])

plt.plot(x,y)
plt.plot(x,dy_analytical,label='analytical derivative',linewidth=3.0,color='green')
plt.plot(x,dy,label='forward off',linewidth=3.0,color='red')
plt.plot(x,dy2,'k--',lw=2,label='centered diff',linewidth=3.0,color='yellow')
plt.legend(loc='lower left')
plt.savefig('6.jpg',dpi=300)
plt.show()
print('job done')