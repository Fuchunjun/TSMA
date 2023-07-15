# -*- coding: utf-8 -*-

#输出0-99
i=0
print('用while')
while i<100:
    print(i,end=" ")
    i+=1
print("\n----------------------------------------------------------------------------------")

print("用for")
for i in range(0,100):
    print(i,end=" ")
print("\n")
#求质数
list=[1,2]
startnum,endnum=input("输入起始数字").split()
for i in range(int(startnum),int(endnum)+1):
    for j in range(2,i):
        if i%j == 0:
            break
        elif j==i-1:
            print(i)

