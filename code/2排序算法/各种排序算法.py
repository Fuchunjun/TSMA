# -*- coding: utf-8 -*-

def sun直接选择排序(list):
    for i in range(len(list)):
        min=i
        for j in range(i+1,len(list)):
            if list[j]<list[min]:
                min=j
        list[i],list[min]=list[min],list[i]
    return list

def sun冒泡排序(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

list=[1,65,6,3,489,341,6,31,54,6,651,651,654,6,132,1,165,156,15,135,1,48,64,641,6,15,165,16,139,46,89,354]
print(sun直接选择排序(list))
print(sun冒泡排序(list))

