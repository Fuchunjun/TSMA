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
        mini=fmax
        for j in range(len(distance)):
            if visited[j]=='T' and distance[j]<mini:
                mini=distance[j]
                i=j
        visited[i]='P'
        #更新节点信息
        for node,dis in network[i+1].items():
            node=int(node)-1
            if visited[node]=='T' and dis+distance[i]<distance[node]:
                distance[node]=dis+distance[i] 
                parent[node]=i+1
    #输出路径，成本
    #print(distance)
    #print(parent)
    print(f'{s}-{e}最短路路径成本：',distance[e-1])
    print('路径：',end='')
    route=[e]
    while parent[route[-1]-1]!=-1:
        route.append(parent[route[-1]-1])
    route.reverse()
    print(route)

import pickle
with open(r'code\4最短路问题\net\SiouxFalls_net.txt','rb') as f:
    net=pickle.load(f)

dijkstra(net,s=1,e=20)
dijkstra(net,s=7,e=13)
dijkstra(net,s=2,e=24)

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
