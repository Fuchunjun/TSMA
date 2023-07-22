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
def __Partition(list,s,e):  #s,e:起始，结束位置
    p=list[s];l=s;r=e       #p：基准
    while l<r:
        while l<r and list[r]>=p:
            r-=1
        while l<r and list[l]<=p:
            l+=1
        list[l],list[r]=list[r],list[l]
    list[s],list[l]=list[l],list[s]
    return l    #返回基准位置

def QuickSort(list):        #排序整个列表
    def QuickSort1(list,s,e):   #递归调用
        q=__Partition(list,s,e)
        if s<q-1:QuickSort1(list,s,q-1)
        if q+1<e:QuickSort1(list,q+1,e)
    s=0;e=len(list)-1
    QuickSort1(list,s,e)
    return list

#改进的快速排序
def __Partition_Center(list,s,e):
    c=(s+e)/2;c=int(c)      #基准位置,中间
    l=s;r=e                 
    p=list[c]
    while l<c:
        if list[l]>p:
            list[l],list[c] = list[c],list[l]
            break
        l+=1
    while l<r:
        while l<r and list[r]>=p:
            r-=1
        if l<r:
            list[l],list[r]=list[r],list[l]
        while l<r and list[l]<=p:
            l+=1
        if l<r:
            list[l],list[r]=list[r],list[l]
    return l
    
def QuickSort_改(list):
    def QuickSort2(list,s,e,):
        q=__Partition_Center(list,s,e)
        if s<q-1:QuickSort2(list,s,q-1)
        if q+1<e:QuickSort2(list,q+1,e)
    s=0;e=len(list)-1
    QuickSort2(list,s,e)
    return list

list=[6,8,4,3,9]
if __name__ == "__main__":
    print(list)
    print(QuickSort_改(list))

