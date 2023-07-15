import math


# 求函数在某一点微分
# x：某一点
# m：增量
def sun单侧差分(f, x, m):
    return (f(x + m) - f(x)) / m


def sun中心差分(f, x, m):
    return (f(x + m) - f(x - m)) / (2 * m)


f = lambda x: 1 / ((1 + x) ** 2)

print("\t  右侧差分\t", "\t  中心差分")
print("m=0.1\t", sun单侧差分(f, 0.5, 0.1), "\t", sun中心差分(f, 0.5, 0.1))
print("m=0.2\t", sun单侧差分(f, 0.5, 0.2), "\t", sun中心差分(f, 0.5, 0.2))
