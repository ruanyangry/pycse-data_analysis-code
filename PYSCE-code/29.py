import numpy as np

#[H2 H Br2 Br HBr]

M=[[-1,0,-1,0,2],[0,0,-1,2,0],[-1,1,0,-1,1],[0,-1,-1,1,1],[1,-1,0,1,-1],[0,0,1,-2,0]]
U,s,V=np.linalg.svd(M)

print(s)
print(np.sum(np.abs(s) > 1e-15))

import sympy
M=sympy.Matrix(M)
reduced_form,inds=M.rref()

print(reduced_form)

labels=['H2','H','Br2','Br','HBr']
for row in reduced_form.tolist():
    s='0 = '
    for nu,species in zip(row,labels):
        if nu !=0:
            s += '{0:+d}{1}'.format(int(nu),species)
    if s != '0 = ':
        print(s)

