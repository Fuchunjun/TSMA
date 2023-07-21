import 各种排序算法
import random
import time 

list = [random.randint(0,5000000) for i in range(0,100000)]

T1 = time.perf_counter()
各种排序算法.QuickSort(list)
T2 = time.perf_counter()
print((T2-T1),'s')