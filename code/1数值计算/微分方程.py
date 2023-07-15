# -*- coding: utf-8 -*-
import math


def f(x, y):
    return 2 * y / x + x * x * math.exp(x)


h = 0.1
yka = 0
'''
a,b:下限、上限
n:离散区间份数
令h和n分别为离散区间的长度和份数,xk=a+kh为等距节点
x0=a和xn=a+nh=b,令yk=y(xk)
'''


def sun_Euler(a, b, n):
    yk = yka
    for k in range(0, n):
        yk = yk + h * f(a + k * h, yk)
    return yk


def sun_Euler改进(a, b, n):
    yk = yka
    for k in range(0, n):
        ykt = yk + h * f(a + k * h, yk)
        yk = yk + (h / 2) * (f(a + k * h, yk) + f(a + (k + 1) * h, ykt))
    return yk


def sun四阶龙格库塔(a, b, n):
    yk = yka
    for k in range(0, n):
        p1 = f(a + k * h, yk)
        p2 = f(a + k * h + h / 2, yk + h / 2 * p1)
        p3 = f(a + k * h + h / 2, yk + h / 2 * p2)
        p4 = f(a + k * h + h, yk + h * p3)
        yk = yk + h * (p1 + 2 * p2 + 2 * p3 + p4) / 6
    return yk


print('k\txk\t', 'Euler方法\t\t', '改进Euler方法\t\t', '四阶龙格库塔方法')
for k in range(0, 11):
    print(k, '\t', round(k + 0.1 * k, 2), '\t', sun_Euler(1, 2, k), '\t', sun_Euler改进(1, 2, k), '\t',
          sun四阶龙格库塔(1, 2, k))
