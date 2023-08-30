def p2p_dijkstra(network,s,e): #s,e 开始，结束节点
    fmax=9999
    distance=[fmax for _ in range(len(network))]#距离信息
    visited=['T' for _ in range(len(network))]
    parent=[-1 for _ in range(len(network))]#父节点信息
    #初始化开始节点
    i=s-1
    distance[i]=0
    for _ in range(len(network)-1):
        #找到T标号中最小的，选中并设置成P标号
        mini=fmax
        for j in range(len(distance)):
            if visited[j]=='T' and distance[j]<mini:
                mini=distance[j]
                i=j
        if i == e-1:   #终点被设置成P终止算法
            break
        visited[i]='P'
        #更新节点信息
        for node,dis in network[i+1].items():
            node=int(node)-1
            if visited[node]=='T' and dis+distance[i]<distance[node]:
                distance[node]=dis+distance[i] 
                parent[node]=i+1
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

p2p_dijkstra(net,s=1,e=20)
