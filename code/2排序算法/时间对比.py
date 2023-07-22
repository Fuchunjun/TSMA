import 排序
import random
import time 

list = [random.randint(0,50) for i in range(0,20)]

T1 = time.perf_counter()
排序.QuickSort_改(list)
T2 = time.perf_counter()
print(list)
print((T2-T1),'s')