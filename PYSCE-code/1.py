from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

k=2.2
def myode(y,t):
    return k*y

y0=3
tspan=np.linspace(0,0.5)
y=odeint(myode,y0,tspan)

plt.plot(tspan,y)
plt.xlabel('Time')
plt.ylabel('y')
plt.savefig('1.jpg',dpi=300)
plt.show()
print('job done')