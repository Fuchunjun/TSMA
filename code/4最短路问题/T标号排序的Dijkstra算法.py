
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

dijkstra_sort(network,1,20)
dijkstra_sort(network,7,13)
dijkstra_sort(network,2,24)
