import numpy as np

def func(a,b=2,*args,**kwargs):
    for kw in kwargs:
        print('kw: {0} = {1}'.format(kw,kwargs[kw]))

    return a**b+np.sum(args)

print(func(2,3,4,5,mysillykw='hahah'))
