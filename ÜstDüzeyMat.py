#I didn't do this

import Blatt07_lib as lib
import numpy as np

def CG(A, b, x0):
    pk = r0 = b - A.dot(x0)
    rk = r0
    xk = x0
    while(True):
        Apk = A.dot(pk)
        alpha = rk.dot(rk) / pk.dot(Apk)
        xk = xk + alpha * pk
        rkrk = rk.dot(rk)
        rk = rk - alpha * Apk
        beta = rk.dot(rk) / rkrk
        pk = rk + beta * pk
        if(np.linalg.norm(rk,2) / np.linalg.norm(r0,2) < 10**(-6)):
            break
    return xk.round(4)

A = np.array([[2,1],
             [1,2]])
b = [2,1]
x0 = [0,0]

print(CG(A,b,x0)) # exakt = [1,0]

for m in [50,100,200]:
    A,b = lib.system(m)
    x0 = np.zeros(m*m)
    xk = CG(A,b,x0)
    print(xk)
    lib.plotxk(xk)
