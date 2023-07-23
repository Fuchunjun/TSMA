# -*- coding: utf-8 -*-
# 直接选择排序
def directsort(list):
    for i in range(len(list)):
        min = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list


# 冒泡排序
def bubblesort(list):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


# 快速排序
def __partition_sun(list, s, e):  # s,e:起始，结束位置  #这个函数是自己理解写的，效率不如下面的__partition
    p = list[s]
    l = s
    r = e  # p：基准
    while l < r:
        while l < r and list[r] >= p:
            r -= 1
        while l < r and list[l] <= p:
            l += 1
        list[l], list[r] = list[r], list[l]
    list[s], list[l] = list[l], list[s]
    return l  # 返回基准位置


def __partition(list, s, e):
    p = list[s]
    l = s
    r = e
    while l < r:
        while l < r and list[r] >= p:
            r -= 1
        if l < r:
            list[l], list[r] = list[r], list[l]
        while l < r and list[l] <= p:
            l += 1
        if l < r:
            list[l], list[r] = list[r], list[l]
    return l


def quicksort(list):  # 排序整个列表
    def QuickSort1(list, s, e):  # 递归调用
        q = __partition(list, s, e)
        if s < q - 1: QuickSort1(list, s, q - 1)
        if q + 1 < e: QuickSort1(list, q + 1, e)

    s = 0
    e = len(list) - 1
    QuickSort1(list, s, e)
    return list


# 改进的快速排序
def __partition_center(list, s, e):
    c = (s + e) / 2
    c = int(c)  # 基准位置,中间
    l = s
    r = e
    p = list[c]
    while l < c:
        if list[l] > p:
            list[l], list[c] = list[c], list[l]
            break
        l += 1
    while l < r:
        while l < r and list[r] >= p:
            r -= 1
        if l < r:
            list[l], list[r] = list[r], list[l]
        while l < r and list[l] <= p:
            l += 1
        if l < r:
            list[l], list[r] = list[r], list[l]
    return l


def quicksort_改(list):
    def QuickSort2(list, s, e, ):
        q = __partition_center(list, s, e)
        if s < q - 1: QuickSort2(list, s, q - 1)
        if q + 1 < e: QuickSort2(list, q + 1, e)

    s = 0
    e = len(list) - 1
    QuickSort2(list, s, e)
    return list


# 堆排序
'''
def makeheap(list,l):
    while l>0:
        if list[l]>list[int((l-1)/2)]:
            list[l],list[int((l-1)/2)]=list[int((l-1)/2)],list[l]
        l-=1
第一次写的，有点扯
def heapsort(list):
    e=len(list)-1
    for l in range(e,-1,-1):
        makeheap(list,l)
        list[0],list[l]=list[l],list[0]
    return list
'''
def adjustdown(list, p, l):
    s = 2 * p + 1
    while s < l:
        if s + 1 < l and list[s + 1] > list[s]:
            s += 1
        if list[p] >= list[s]:
            break
        list[p], list[s] = list[s], list[p]
        p = s
        s = 2 * p + 1

def makeheap(list,l):
    for p in range(int(l/2-1),-1,-1):
        adjustdown(list,p,l)

def heapsort(list):
    n=len(list)
    makeheap(list,n)
    for l in range(n-1,-1,-1):
        list[0],list[l]=list[l],list[0]
        adjustdown(list,0,l)
    return list


list = [6, 8, 4, 3, 9, 54, 5]
if __name__ == "__main__":
    print(heapsort(list))
