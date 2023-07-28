import 排序
import random
import time

sum1=0
for _ in range(10):
    list=[random.randint(0,1000000) for _ in range(1000000)]
    T1 = time.perf_counter()
    排序.heapsort(list)
    T2 = time.perf_counter()
    c=T2-T1
    print(c,'s')
    sum1+=c
    list.clear()
print('平均用时：',sum1/10)