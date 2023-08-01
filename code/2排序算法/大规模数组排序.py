import 排序
import random
import time

sum1=0
for _ in range(10):
    list=[random.randint(1,10000) for _ in range(10000)]
    T1 = time.perf_counter()
    排序.quicksort(list)
    T2 = time.perf_counter()
    c=T2-T1
    print(c,'s')
    sum1+=c
    list.clear()
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