import numpy as np
from scipy.linalg import lu

A=np.array([[6,2,3],[1,1,1],[0,4,9]])
P,L,U=lu(A)

nswaps=len(np.diag(P))-np.sum(np.diag(P))-1

detP=(-1)**nswaps
detL=np.prod(np.diag(L))
detU=np.prod(np.diag(U))

print(detP*detL*detU)
print(np.linalg.det(A))

print('job done')