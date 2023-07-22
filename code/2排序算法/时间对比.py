import 排序
import random
import time 

list = [random.randint(0,99999999) for i in range(0,1000000)]

T1 = time.perf_counter()
排序.DirectSort(list)
T2 = time.perf_counter()
print((T2-T1),'s')


