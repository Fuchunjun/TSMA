# -*- coding: utf-8 -*-
#直接选择排序
def DirectSort(list):
    for i in range(len(list)):
        min=i
        for j in range(i+1,len(list)):
            if list[j]<list[min]:
                min=j
        list[i],list[min]=list[min],list[i]
    return list

#冒泡排序

def BubbleSort(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
#快速排序
def __Partition(list,s,e):
    p=list[s];l=s;r=e
    while l<r:
        while l<r and list[r]>=p:
            r-=1
        while l<r and list[l]<=p:
            l+=1
        list[l],list[r]=list[r],list[l]
    list[s],list[l]=list[l],list[s]
    return l

def QuickSort(list):
    def QuickSort1(list,s,e):
        q=__Partition(list,s,e)
        if s<q-1:QuickSort1(list,s,q-1)
        if q+1<e:QuickSort1(list,q+1,e)
    s=0;e=len(list)-1
    QuickSort1(list,s,e)
    return list
#改进的快速排序
def __Partition_Center(list,s,e):
    pass

list=[1,6,]
if __name__ == "__main__":
    print(QuickSort(list))

