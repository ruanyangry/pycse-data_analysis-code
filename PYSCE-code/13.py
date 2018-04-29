# _*_ coding: utf-8 _*_

def f1(x):
    if x < 0 :
        return 0
    elif (x >=0) & (x < 1):
        return x
    elif(x >=1) & (x < 2):
        return 2.0-x
    else:
        return 0

print(f1(-1111))

print('jod done')