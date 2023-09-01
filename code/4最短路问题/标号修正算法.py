#单队列尾部
def labelcorrecting_Q(net,s,e=0):
    s-=1
    Q=[s] #队列q记录需要检查的节点
    dis=[999 for _ in range(len(net))] #距离
    par=[-1 for _ in range(len(net))] #前继节点
    dis[s]=0
    while Q:
        i=Q[0]
        Q.pop(0)
        for j,disij in net[i+1].items():
            j=int(j)-1
            if dis[j]>dis[i]+disij:
                dis[j]=dis[i]+disij
                par[j]=i+1
                if j not in Q:
                    Q.append(j)     #j不在q中，插入队列尾部 
    """      
    print(f'{s}-{e}最短路路径成本：',dis[e-1])
    print('路径：',end='')
    route=[e]
    while par[route[-1]-1]!=-1:
        route.append(par[route[-1]-1])
    route.reverse()
    print(route) 
    """

#单队列混合
def labelcorrecting_Q_混合(net,s,e=0):
    s-=1
    Q=[s] #队列q记录需要检查的节点
    st=[0 for _ in range(len(net))] #首次探测标记
    dis=[999 for _ in range(len(net))] #距离
    par=[-1 for _ in range(len(net))] #前继节点
    dis[s]=0
    st[s]=1
    while Q:
        i=Q[0]
        Q.pop(0)
        for j,disij in net[i+1].items():
            j=int(j)-1
            if dis[j]>dis[i]+disij:
                dis[j]=dis[i]+disij
                par[j]=i+1
                if j not in Q:
                    if st[j]==0:        #首次探测添加到尾部
                        Q.append(j)
                        st[j]=1
                    else:
                        Q.insert(0,j)
""" print(f'{s}-{e}最短路路径成本：',dis[e-1])
    print('路径：',end='')
    route=[e]
    while par[route[-1]-1]!=-1:
        route.append(par[route[-1]-1])
    route.reverse()
    print(route) """

#双队列
def labelcorrecting_2Q(net,s,e=0):
    s-=1
    Q1=[s]
    Q2=[]  #Q1中存放非首次探测到的待检查节点，Q2存放首次探测到的待检查节点
    st=[0 for _ in range(len(net))] #首次探测标记
    dis=[999 for _ in range(len(net))] #距离
    par=[-1 for _ in range(len(net))] #前继节点
    st[s]=1
    dis[s]=0
    while Q1 or Q2:
        if Q1:      #选取节点
            i=Q1[0]
            Q1.pop(0)
        else:
            i=Q2[0]
            Q2.pop(0)
        for j,disij in net[i+1].items():
            j=int(j)-1
            if dis[j]>dis[i]+disij:
                dis[j]=dis[i]+disij
                par[j]=i+1
                if j not in Q1 and j not in Q2:    #j第一次探测放到Q2，否则放Q1
                    if st[j]==0:
                        Q2.append(j)
                        st[j]=1
                    else:
                        Q1.append(j)
""" 
    print(f'{s}-{e}最短路路径成本：',dis[e-1])
    print('路径：',end='')
    route=[e]
    while par[route[-1]-1]!=-1:
        route.append(par[route[-1]-1])
    route.reverse()
    print(route)
 """
SiouxFalls_net={
    1: {'2': 6, '3': 4}, 
    2: {'1': 6, '6': 5}, 
    3: {'1': 4, '4': 4, '12': 4}, 
    4: {'3': 4, '5': 2, '11': 6}, 
    5: {'4': 2, '6': 4, '9': 5}, 
    6: {'2': 5, '5': 4, '8': 2}, 
    7: {'8': 3, '18': 2}, 
    8: {'6': 2, '7': 3, '9': 10, '16': 5}, 
    9: {'5': 5, '8': 10, '10': 3}, 
    10: {'9': 3, '11': 5, '15': 6, '16': 4, '17': 8}, 
    11: {'4': 6, '10': 5, '12': 6, '14': 4}, 
    12: {'3': 4, '11': 6, '13': 3}, 
    13: {'12': 3, '24': 4}, 
    14: {'11': 4, '15': 5, '23': 4}, 
    15: {'10': 6, '14': 5, '19': 3, '22': 3}, 
    16: {'8': 5, '10': 4, '17': 2, '18': 3}, 
    17: {'10': 8, '16': 2, '19': 2}, 
    18: {'7': 2, '16': 3, '20': 4}, 
    19: {'15': 3, '17': 2, '20': 4}, 
    20: {'18': 4, '19': 4, '21': 6, '22': 5}, 
    21: {'20': 6, '22': 2, '24': 3}, 
    22: {'15': 3, '20': 5, '21': 2, '23': 4}, 
    23: {'14': 4, '22': 4, '24': 2}, 
    24: {'13': 4, '21': 3, '23': 2}
}


if __name__=='__main__':
    print('单队列')
    labelcorrecting_Q(SiouxFalls_net,1,20)
    labelcorrecting_Q(SiouxFalls_net,7,13)
    labelcorrecting_Q(SiouxFalls_net,2,24)
    print('双队列')
    labelcorrecting_2Q(SiouxFalls_net,1,20)
    labelcorrecting_2Q(SiouxFalls_net,7,13)
    labelcorrecting_2Q(SiouxFalls_net,2,24)
    print('单队列混合')
    labelcorrecting_Q_混合(SiouxFalls_net,1,20)
    labelcorrecting_Q_混合(SiouxFalls_net,7,13)
    labelcorrecting_Q_混合(SiouxFalls_net,2,24)
