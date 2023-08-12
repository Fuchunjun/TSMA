import 排序
import random
import time

sum1=0
n=[1000,10000,100000]

for n in n:
    for _ in range(10):
        listo=[random.randint(1,n) for _ in range(n)]
        T1 = time.perf_counter()
        排序.bubblesort(listo)
        T2 = time.perf_counter()
        c=T2-T1
        sum1+=c
        listo.clear()
    print('平均用时：',sum1/10)

'''
结果记录 
        10**3        10**4       10**5       10**6
直接     0.0257       2.1578      224.0128    --
冒泡     0.0573       5.1775      634.8020    --
快速     0.0015       0.0195      0.2502      3.2962
改快     0.0018       0.0215      0.2639      3.6630
堆排     0.0025       0.0336      0.4293      5.8326
'''