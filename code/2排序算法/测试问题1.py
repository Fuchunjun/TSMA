import 排序

list = [18, 54, 14, 45, 96, 27, 80, 22, 81, 31, 0, 63, 49, 5, 59, 27, 28, 75, 68, 52, 52, 66, 5, 98, 44, 19, 22, 16, 88,
        34, 59, 81, 12, 85, 49, 54, 84, 13, 46, 83, 88, 1, 70, 32, 45, 32, 38, 41, 46, 50]

list1=list.copy()
print('直接选择排序',排序.directsort(list1))
list2=list.copy()
print('冒泡排序',排序.bubblesort(list2))
list3=list.copy()
print('快速排序',排序.quicksort(list3))
list4=list.copy()
print('堆排序',排序.heapsort(list4))
