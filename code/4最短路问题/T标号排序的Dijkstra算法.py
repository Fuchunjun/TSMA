
def dijkstra_sort(network,s,e):
    tnodes=[i for i in range(1,len(network)+1)]
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
            if node in tnodes:
                if dis+nodeinfo[slectnode]['dis']<nodeinfo[node]['dis']:
                    nodeinfo[node]['dis']=dis+nodeinfo[slectnode]['dis']
                    nodeinfo[node]['par']=slectnode
                    #更新该节点在tnodes中的位置
                    for x in tnodes:
                        if  nodeinfo[node]['dis']<nodeinfo[x]['dis']:
                            tnodes.remove(node)
                            loc=tnodes.index(x)
                            tnodes.insert(loc,node)
                            break
    print(f'{s}-{e}最短路路径成本：',nodeinfo[e]['dis'])
    route=[e]
    while nodeinfo[route[-1]]['par']!=-1:
        route.append(int(nodeinfo[route[-1]]['par']))
    route.reverse()
    print('路径：',route)

from 读取节点网络 import SiouxFalls_net
dijkstra_sort(SiouxFalls_net,1,20)
dijkstra_sort(SiouxFalls_net,7,13)
dijkstra_sort(SiouxFalls_net,2,24)
