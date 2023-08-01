import 排序
import random
import time

n=100000    #数组长度

probability=[0.001,0.01,0.1,0.2,0.5]

for p in probability:
    arro = [random.randint(1, n) for _ in range(0, n)]
    arr = 排序.quicksort_改(arro)
    for i in range(0, n):
        if random.uniform(0, 1) < p:
            arr[i] = random.randint(1, n)
    T1 = time.perf_counter()
    排序.quicksort_改(arr)
    T2 = time.perf_counter()
    print(T2 - T1)


'''
结果记录
扰动概率	    p=0.001 	p=0.01 	    p=0.1 	    p=0.2 	    p=0.5 
直接排序	    223.9785 s	224.0583 s	222.3456 s	236.2338 s	315.3704 s
冒泡排序	    338.0857 s	381.1712 s	452.6590 s	479.8770 s	577.0643 s
快速排序	    - s	        - s	        - s	        - s	        - s         错误代码 -1073741571 (0xC00000FD) StackOverflow（栈区溢出）
改进快速排序	0.1552 s	0.1511 s	0.1747 s	0.1739 s	0.2375 s
堆排序	    0.3732 s	0.3546 s	0.3473 s	0.3671 s	0.4312 s
'''