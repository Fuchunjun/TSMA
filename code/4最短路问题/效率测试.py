#从xlsx读取网络并保存二进制
def rwnetwork(path):
    import pandas as pd
    import pickle
    data=pd.read_excel(path)
    net={}
    for _,row in data.iterrows():
        init=row[0]
        term=row[1]
        fftt=row[4]
        if init not in net:
            net[init]={}
        net[init][str(term)]=fftt
        txtpath=path.replace('.xlsx','.txt')
    with open(txtpath, 'wb') as f:
        pickle.dump(net,f)
#读取网络
import os 
def readnetwork(path):
    import pickle
    txtpath=path.replace('.xlsx','.txt')
    if os.path.exists(txtpath)==False:
        rwnetwork(path)
    with open(txtpath, 'rb') as f:
        net=pickle.load(f)
    return net




path=r'code\4最短路问题\net\ChicagoSketch_net.xlsx'
net=readnetwork(path)
import 标号设置算法
import 标号修正算法
import time
t1=time.perf_counter()
for i in range(1,len(net)+1):
    标号修正算法.labelcorrecting_2Q(net,1)
t2=time.perf_counter()
print(t2-t1)


'''
结果记录
算法                                时间 
Label-setting算法	                36.26434
T标号排序的Label-setting算法	     10.59079
T标号堆排序的Label-setting算法       3.073973
单队列尾部Label-correcting算法	     3.666588
单队列混合Label-correcting算法	     1.640590
双队列Label-correcting算法	         1.681312
'''


""" 
标号设置算法.dijkstra(net,1)
标号设置算法.dijkstra_sort(net,1)
标号设置算法.dijkstra_t_heap(net,1)
标号修正算法.labelcorrecting_Q(net,1)
标号修正算法.labelcorrecting_Q_混合(net,1)
标号修正算法.labelcorrecting_2Q(net,1) 
"""




