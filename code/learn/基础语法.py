# -*- coding: utf-8 -*-
#声明文件编码方式

#字符串操作
字符串='12345678'
print(字符串)
print(字符串[0])        #输出第一个字符
print(字符串[-1])       #输出最后一个字符
print(字符串[0:5])      #输出第1-5个字符
print(字符串[0:8:2])    #输出第1-8个字符，步长2
print(字符串*2)         #输出两遍
print(字符串+'abc')     #连接字符串
print(字符串,end='')
print(字符串)           #不换行

print('123 \n456')
print(r'123\n456')      #不转义

#输入
a=input('输入一个数')
print(a)

a=[1 for _ in range(5)]
print(a)
a=[0 for _ in range(10)]
print(a)