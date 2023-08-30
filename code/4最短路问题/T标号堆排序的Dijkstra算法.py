
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
    print(f'{s}-{e}最短路路径成本：',node[e]['dis'])
    route=[e]
    while node[route[-1]]['par']!=-1:
        route.append(int(node[route[-1]]['par']))
    route.reverse()
    print('路径：',route)

from 读取节点网络 import SiouxFalls_net
dijkstra_t_heap(SiouxFalls_net,1,20)
dijkstra_t_heap(SiouxFalls_net,7,13)
dijkstra_t_heap(SiouxFalls_net,2,24)














