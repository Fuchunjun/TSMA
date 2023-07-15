# -*- coding: utf-8 -*-

#多元函数
def f(x1,x2):
    return x1*x1+2*x1*x2+3*x2*x2*x2

def sun单侧差分(x1,x2,m):
    print((f(x1+m,x2)-f(x1,x2))/m,end=",")
    print((f(x1,x2+m)-f(x1,x2))/m,end="\t")

def sun中心差分(x1,x2,m):
    print((f(x1+m,x2)-f(x1-m,x2))/(2*m),end=",")
    print((f(x1,x2+m)-f(x1,x2-m))/(2*m))

print("m\t","\t右侧差分\t","\t\t\t\t中心差分")
print("0.05",end="\t")
sun单侧差分(1.5,1,0.05)
sun中心差分(1.5,1,0.05)
print("0.1",end="\t")
sun单侧差分(1.5,1,0.1)
sun中心差分(1.5,1,0.1)
print("0.2",end="\t")
sun单侧差分(1.5,1,0.2)
sun中心差分(1.5,1,0.2)
