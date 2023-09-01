
def dijkstra(network,s,e=0): #s,e 开始，结束节点
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
    """ 
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
     """


def dijkstra_t_heap(network,s,e=0):
    def adjustdown_tnode(theap,p):#T标号下沉
        s=2*p+1
        while s<len(theap):
            if s+1<len(theap) and node[theap[s]]['dis']>node[theap[s+1]]['dis']:
                s+=1
            if node[theap[p]]['dis']<node[theap[s]]['dis']:
                break
            else:
                theap[p],theap[s]=theap[s],theap[p]
                p=s
                s=2*p+1

    def adjustup_tnode(theap,s):  #T标号上浮
        p=(s-1)//2
        while p>=0:
            if node[theap[p]]['dis']>node[theap[s]]['dis']:
                theap[s],theap[p]=theap[p],theap[s]
                s=p
                p=(s-1)//2
            else:
                break

    theap=[] #T标号节点的小顶堆
    node={k+1:{'dis':999,'par':-1,'st':0} for k in range(len(network))} 
    #dis:距离，par:前继节点，st:是否被探测 0为否
    #初始化开始节点
    theap.append(s)  
    node[s]['dis']=0;node[s]['st']=1
    for _ in range(1,len(network)):
        i=theap[0]
        for j,disij in network[i].items():
            j=int(j)
            if node[j]['dis']>node[i]['dis']+disij:
                node[j]['dis']=node[i]['dis']+disij
                node[j]['par']=i
                if node[j]['st']==0:
                    node[j]['st']=1
                    theap.append(int(j))
                adjustup_tnode(theap,len(theap)-1)
        theap[0]=theap[-1]
        theap.pop(-1)
        adjustdown_tnode(theap,0)
    """     
    print(f'{s}-{e}最短路路径成本：',node[e]['dis'])
    route=[e]
    while node[route[-1]]['par']!=-1:
        route.append(int(node[route[-1]]['par']))
    route.reverse()
    print('路径：',route)
     """


def dijkstra_sort(network,s,e=0):
    tnodes = list(range(1,len(network)+1))
    nodeinfo={k+1:{'dis':9999,'par':-1} for k in range(len(network))}
    #初始化开始节点
    slectnode=tnodes[0]
    nodeinfo[s]['dis']=0
    tnodes.remove(s)
    tnodes.insert(0,s)  #将开始节点移动到第一位
    for _ in range(len(network)-1):
        slectnode=tnodes[0]
        tnodes.pop(0)
        for node,dis in network[slectnode].items():
            #更新节点信息
            node=int(node)
            if node in tnodes and dis+nodeinfo[slectnode]['dis']<nodeinfo[node]['dis']:
                nodeinfo[node]['dis']=dis+nodeinfo[slectnode]['dis']
                nodeinfo[node]['par']=slectnode
                #更新该节点在tnodes中的位置
                for x in tnodes:
                    if  nodeinfo[node]['dis']<nodeinfo[x]['dis']:
                        tnodes.remove(node)
                        loc=tnodes.index(x)
                        tnodes.insert(loc,node)
                        break
    '''
    print(f'{s}-{e}最短路路径成本：',nodeinfo[e]['dis'])
    route=[e]
    while nodeinfo[route[-1]]['par']!=-1:
        route.append(int(nodeinfo[route[-1]]['par']))
    route.reverse()
    print('路径：',route)
    '''


if __name__=='__main__':
    import pickle
    with open(r'code\4最短路问题\net\ChicagoSketch_net.txt','rb') as f:
        net=pickle.load(f)

    dijkstra_t_heap(net,1)

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
