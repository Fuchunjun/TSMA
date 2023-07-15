# -*- coding: utf-8 -*-
import math
'''
利用不同公式求积分
a:积分下限
b:积分上限
n:分割区间数量
'''
def sun中矩形(f, a, b, n):
    tem = 0
    for i in range(1, n + 1):
        tem += f(((a + i * (b - a) / n) + (a + (i - 1) * (b - a) / n)) / 2)
    return tem * (b - a) / n


def sun梯形(f, a, b, n):
    tem = 0
    for i in range(1, n):
        tem += f(a + i * (b - a) / n)
    return (b - a) / (2 * n) * (f(a) + 2 * tem + f(b))


def sun辛普森(f, a, b, n):
    tem1, tem2 = 0, 0
    for i in range(1, n + 1):
        tem1 += f(((a + i * (b - a) / n) + (a + (i - 1) * (b - a) / n)) / 2)
    for i in range(1, n):
        tem2 += f(a + (b - a) / n * i)
    return (b - a) / n * (f(a) + 4 * tem1 + 2 * tem2 + f(b)) / 6


# 定义函数
f1 = lambda x: 1 / x
f2 = lambda x: (math.log(3 + x ** 2)) / (1 + x ** 2)

if __name__ == '__main__':
    print('f(x) = 1/x')
    print("区间数量\t\t", 10, '\t\t\t', 100)
    print("复化中矩形公式\t", sun中矩形(f1, 1, 2, 10), '\t', sun中矩形(f1, 1, 2, 100))
    print("复化梯形公式\t", sun梯形(f1, 1, 2, 10), '\t', sun梯形(f1, 1, 2, 100))
    print("复化辛普森公式\t", sun辛普森(f1, 1, 2, 10), '\t', sun辛普森(f1, 1, 2, 100))

    print('f(x)=(math.log(3+x**2))/(1+x**2)')
    print("区间数量\t\t", 10, '\t\t\t', 100)
    print("复化中矩形公式\t", sun中矩形(f2, 1, 2, 10), '\t', sun中矩形(f2, 1, 2, 100))
    print("复化梯形公式\t", sun梯形(f2, 1, 2, 10), '\t', sun梯形(f2, 1, 2, 100))
    print("复化辛普森公式\t", sun辛普森(f2, 1, 2, 10), '\t', sun辛普森(f2, 1, 2, 100))
