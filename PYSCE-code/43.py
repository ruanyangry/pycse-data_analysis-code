# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

N=1000
#cn=0
games=np.random.uniform(size=N)

#for i in np.arange(0,N,1):
#    games=np.random.uniform(i)
#    if games>0.49:
#        cn+=1

#wins=cn
wins=np.sum(games>0.49)
losses=N-wins

print('You won {0} times ({1:%})'.format(wins,float(wins)/N))

#wins=np.sum(games>0.49)
#losses=N-wins

# draw graph

count,bins,ignored=plt.hist(games)
plt.savefig('43.jpg',dpi=300)
plt.show()
print('plot done')

