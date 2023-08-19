
def dijkstra_t_heap(network,s,e):
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
        p=(s-1)%2
        while p>=0:
            if node[theap[p]]['dis']>node[theap[s]]['dis']:
                theap[s],theap[p]=theap[p],theap[s]
                s=p
                p=(s-1)%2
            else:
                break
    theap=[] #T标号节点的小顶堆
    node={k+1:{'dis':9999,'par':-1,'st':0} for k in range(len(network))} 
    #dis:距离，par:前继节点，st:是否被探测0为否
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
    print(f'{s}-{e}最短路路径成本：',node[e]['dis'])
    route=[e]
    while node[route[-1]]['par']!=-1:
        route.append(int(node[route[-1]]['par']))
    route.reverse()
    print('路径：',route)

network={1: {'2': 6, '3': 4}, 2: {'1': 6, '6': 5}, 3: {'1': 4, '4': 4, '12': 4}, 4: {'3': 4, '5': 2, '11': 6}, 5: {'4': 2, '6': 4, '9': 5}, 6: {'2': 5, '5': 4, '8': 2}, 7: {'8': 3, '18': 2}, 8: {'6': 2, '7': 3, '9': 10, '16': 5}, 9: {'5': 5, '8': 10, '10': 3}, 10: {'9': 3, '11': 5, '15': 6, '16': 4, '17': 8}, 11: {'4': 6, '10': 5, '12': 6, '14': 4}, 12: {'3': 4, '11': 6, '13': 3}, 13: {'12': 3, '24': 4}, 14: {'11': 4, '15': 5, '23': 4}, 15: {'10': 6, '14': 5, '19': 3, '22': 3}, 16: {'8': 5, '10': 4, '17': 2, '18': 3}, 17: {'10': 8, '16': 2, '19': 2}, 18: {'7': 2, '16': 3, '20': 4}, 19: {'15': 3, '17': 2, '20': 4}, 20: {'18': 4, '19': 4, '21': 6, '22': 5}, 21: {'20': 6, '22': 2, '24': 3}, 22: {'15': 3, '20': 5, '21': 2, '23': 4}, 23: {'14': 4, '22': 4, '24': 2}, 24: {'13': 4, '21': 3, '23': 2}}

dijkstra_t_heap(network,1,20)
dijkstra_t_heap(network,7,13)
dijkstra_t_heap(network,2,24)














