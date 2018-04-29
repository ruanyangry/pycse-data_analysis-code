import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,np.pi,10)
plt.plot(x,np.cos(x),color='green',linestyle='--',linewidth=2.0)
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title('4')
plt.savefig('4.jpg',dpi=300)
plt.show()
print('job done')
