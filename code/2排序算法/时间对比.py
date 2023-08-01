import 排序
import random
import time

def bubblesort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


arr = [random.randint(1, 100000) for _ in range(0, 100000)]
t1 = time.perf_counter()
bubblesort(arr)
t2 = time.perf_counter()
print(t2 - t1)
