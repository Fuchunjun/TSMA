import math

def 黄金分割法(f,L0,U0,precision):
    L=L0
    U=U0
    x1=L+0.328*(U-L)
    x2=L+0.618*(U-L)
    F1=f(x1)
    F2=f(x2)
    while U-L>precision:
        if F1<F2:
            U=x2
            x2=x1
            F2=F1
            x1=L+0.328*(U-L)
            F1=f(x1)
        else:
            L=x1
            x1=x2
            F1=F2
            x2=L+0.618*(U-L)
            F2=f(x2)
    print((L+U)/2)

def 二分法(f,L0,U0,precision):
    def f1(x,m=0.01):
        return(f(x + m) - f(x - m)) / (2 * m)
    L=L0
    U=U0
    while U-L>precision:
        x=(L+U)/2
        if f1(x)<0:
            L=x
        else:
            U=x
    print((L+U)/2)

f=lambda x:x**2-6*x+2

黄金分割法(f,0,10,0.1)
二分法(f,0,10,0.1)

