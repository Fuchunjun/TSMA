#单队列
def labelcorrecting_Q(net,s,e):
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
    print(f'{s}-{e}最短路路径成本：',dis[e-1])
    print('路径：',end='')
    route=[e]
    while par[route[-1]-1]!=-1:
        route.append(par[route[-1]-1])
    route.reverse()
    print(route)
#双队列
def labelcorrecting_2Q(net,s,e):
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
    #print(dis)
    print(f'{s}-{e}最短路路径成本：',dis[e-1])
    print('路径：',end='')
    route=[e]
    while par[route[-1]-1]!=-1:
        route.append(par[route[-1]-1])
    route.reverse()
    print(route)

from 读取节点网络 import SiouxFalls_net
print('单队列')
labelcorrecting_Q(SiouxFalls_net,1,20)
labelcorrecting_Q(SiouxFalls_net,7,13)
labelcorrecting_Q(SiouxFalls_net,2,24)
print('双队列')
labelcorrecting_2Q(SiouxFalls_net,1,20)
labelcorrecting_2Q(SiouxFalls_net,7,13)
labelcorrecting_2Q(SiouxFalls_net,2,24)

