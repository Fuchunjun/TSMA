
def dijkstra(network,s,e): #s,e 开始，结束节点
    fmax=9999
    distance=[fmax for _ in range(len(network))]#距离信息
    visited=['T' for _ in range(len(network))]
    parent=[-1 for _ in range(len(network))]#父节点信息
    #初始化开始节点
    i=s-1
    distance[i]=0

    for _ in range(len(network)-1):
        '''
        第一次拉的屎
        templist=[]
        for count in range(len(distance)):
            if visited[count]=='T' :
                templist.append(distance[count])
        if len(templist)!=0:
            for count in range(len(distance)):
                if visited[count]=='T' and distance[count]==min(templist):
                    i=count
                    visited[i]='P'
                    break
        templist.clear()
        '''
        #找到T标号中最小的，选中并设置成P标号
        min=fmax
        for j in range(len(distance)):
            if visited[j]=='T' and distance[j]<min:
                min=distance[j]
                i=j
        visited[i]='P'
        #更新节点信息
        for node,dis in network[i+1].items():
            node=int(node)-1
            if visited[node]=='T':
                if dis+distance[i]<distance[node]:
                    distance[node]=dis+distance[i] 
                    parent[node]=i+1
    #输出路径，成本
    print(distance)
    print(parent)
    print(f'{s}-{e}最短路路径成本：',distance[e-1])
    print('路径：',end='')
    route=[e]
    while parent[route[-1]-1]!=-1:
        route.append(parent[route[-1]-1])
    route.reverse()
    print(route)
#从表格文件读取节点网络
import pandas as pd
data=pd.read_excel(r'code\4最短路问题\SiouxFalls_net.xlsx',usecols='A,B,E')
n=24   #节点数
keys=[]
values=[]
tempdict={}
for k in range(0,n):
    keys.append(k+1)
    for i in range(len(data)):
        if data.iloc[i,0]==k+1:
            tempdict[str(data.iloc[i,1])]=data.iloc[i,2]
    copdict=tempdict.copy()
    values.append(copdict)
    tempdict.clear()
network={k:v for k,v in zip(keys,values)}

dijkstra(network,s=1,e=20)
dijkstra(network,s=7,e=13)
dijkstra(network,s=2,e=24)

'''
[0, 6, 4, 8, 10, 11, 16, 13, 15, 18, 14, 8, 11, 18, 23, 18, 20, 18, 22, 22, 18, 20, 17, 15]
[-1, 1, 1, 3, 4, 2, 8, 6, 5, 9, 4, 3, 12, 11, 14, 8, 16, 7, 17, 18, 24, 21, 24, 13]
1-20最短路路径成本： 22
路径：[1, 2, 6, 8, 7, 18, 20]
[16, 10, 15, 11, 9, 5, 0, 3, 12, 9, 14, 19, 19, 17, 12, 5, 7, 2, 9, 6, 12, 11, 15, 15]
[2, 6, 4, 5, 6, 8, -1, 7, 10, 16, 10, 3, 24, 15, 19, 18, 16, 7, 17, 18, 20, 20, 22, 21]
7-13最短路路径成本： 19
路径：[7, 18, 20, 21, 24, 13]
[6, 0, 10, 11, 9, 5, 10, 7, 14, 16, 17, 14, 17, 21, 19, 12, 14, 12, 16, 16, 22, 21, 23, 21]
[2, -1, 1, 5, 6, 2, 8, 6, 5, 16, 4, 3, 12, 11, 19, 8, 16, 7, 17, 18, 20, 20, 24, 13]
2-24最短路路径成本： 21
路径：[2, 1, 3, 12, 13, 24]
'''

#用字典方式存储的节点网络
'''
network={
    1:{'2':6,'3':4},
    2:{'1':6,'6':5},
    3:{'1':4,'4':4,'12':4},
    4:{'3':4,'5':2,'11':6},
    5:{'4':2,'6':4,'9':5},
    6:{'2':5,'5':4,'8':2},
    7:{'8':3,'18':2},
    8:{'6':2,'9':10,'7':3,'16':5},
    9:{'10':3,'8':10,'5':5},
    10:{'11':5,'9':3,'16':4,'17':8,'15':6},
    11:{'10':5,'4':6,'12':6,'14':4},
    12:{'11':6,'13':3,'3':4},
    13:{'12':3,'24':4},
    14:{'11':4,'23':4,'15':5},
    15:{'14':5,'10':6,'19':3,'22':3},
    16:{'10':4,'8':5,'18':3,'17':2},
    17:{'10':8,'16':2,'19':2},
    18:{'7':2,'16':3,'20':4},
    19:{'17':2,'15':3,'20':4},
    20:{'21':6,'22':5,'18':4,'19':4},
    21:{'20':6,'22':2,'24':3},
    22:{'21':2,'15':3,'20':5,'23':4},
    23:{'14':4,'22':4,'24':2},
    24:{'13':4,'21':3,'23':2}
}
'''