# -*- coding: utf-8 -*-
#列表操作
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [5,8,416,46,92,3,48,15,67,11,8 ]
 
print ("list1[3]: ", list1[3])
print ("list2[1:5]: ", list2[1:5])

for i in list1:
    print(i,end=" ")
print()
list1.append('mdk')
print(list1[4])

print(len(list1))
list2.sort(reverse=False)
print(list2)
list2.sort(reverse=True)
print(list2)
del list1,list2

#字典操作
d={
    'Name': 'scf', 
    'Age': 20, 
    'Class': '22'
}

print(d['Age'])
d['Age']=21
print(d['Age'])
del d

#集合操作
set1=set('sunchunfu')
set2=set('fuchunjun')

print(set1-set2) #1有2没有
print(set1|set2)  #1或2中所有元素
print(set1&set2) #1和2中都有
print(set1^set2) #不同时存在
del set1, set2

a={'c++','python','java'}
b={'Alice','Bob','Steve'}
a.add('php')
print(a) 
a.update(b)
print(a)
del a,b