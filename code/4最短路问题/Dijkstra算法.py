def dijkstra(network,s,e): #s,e 开始，结束节点
    fmax=9999
    distance=[fmax for _ in range(len(network))]#距离信息
    visited=['T' for _ in range(len(network))]#是否为已选
    parent=[-1 for _ in range(len(network))]#父节点信息
    #初始化开始节点
    i=s-1
    distance[i]=0

    for _ in range(len(network)-2):  #这个循环次数可能多了，不太确定，反正是能运行
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
        for node,dis in network[str(i+1)].items():
            node=int(node)-1
            if visited[node]=='T':
                if dis+distance[i]<distance[node]:
                    distance[node]=dis+distance[i] 
                    parent[node]=i+1
    print(parent)
    print(distance)
    #输出路径
    for i in range(len(distance)):
        if i == e-1:
            print(f'{s}-{e}最短路路径成本：',distance[i])
    print('路径：',end='')
    route=[e]
    while parent[route[-1]-1]!=-1:
        route.append(parent[route[-1]-1])
    route.reverse()
    print(route)
        
network={
    '1':{'2':6,'3':4},
    '2':{'1':6,'6':5},
    '3':{'1':4,'4':4,'12':4},
    '4':{'3':4,'5':2,'11':6},
    '5':{'4':2,'6':4,'9':5},
    '6':{'2':5,'5':4,'8':2},
    '7':{'8':3,'18':2},
    '8':{'6':2,'9':10,'7':3,'16':5},
    '9':{'10':3,'8':10,'5':5},
    '10':{'11':5,'9':3,'16':4,'17':8,'15':6},
    '11':{'10':5,'4':6,'12':6,'14':4},
    '12':{'11':6,'13':3,'3':4},
    '13':{'12':3,'24':4},
    '14':{'11':4,'23':4,'15':5},
    '15':{'14':5,'10':6,'19':3,'22':3},
    '16':{'10':4,'8':5,'18':3,'17':2},
    '17':{'10':8,'16':2,'19':2},
    '18':{'7':2,'16':3,'20':4},
    '19':{'17':2,'15':3,'20':4},
    '20':{'21':6,'22':5,'18':4,'19':4},
    '21':{'20':6,'22':2,'24':3},
    '22':{'21':2,'15':3,'20':5,'23':4},
    '23':{'14':4,'22':4,'24':2},
    '24':{'13':4,'21':3,'23':2}
}

dijkstra(network,s=1,e=20)
dijkstra(network,s=7,e=13)
dijkstra(network,s=2,e=24)
