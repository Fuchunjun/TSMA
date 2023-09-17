
def topologicalsort(net):
    l=0
    in_degree={i:0 for i in range(len(net))}
    for _,i in net.items():
        for j,_ in i.items():
            j=int(j)
            in_degree[j]+=1
    Q=[q for q in in_degree if in_degree[q]==0]
    res=[]
    while Q:
        i=Q.pop()
        res.append(i)
        l+=1
        for j,_ in net[i].items():
            j=int(j)
            in_degree[j]-=1
            if in_degree[j]==0:
                Q.append(j)
    return res

def Dijkstra_TopologicalOrder(net,s):
    l=topologicalsort(net)
    print(l)
    dis=[9999 for _ in range(len(net))]
    par=[-1 for _ in range(len(net))]
    dis[s]=0
    for i in l[l.index(s):]:
        for j,disij in net[i].items():
            j=int(j)
            if dis[j]>dis[i]+disij:
                dis[j]=dis[i]+disij
                par[j]=i
    for node in range(len(net)):
        route=[]
        x=node
        while x!=-1:
            route.append(x)
            x=par[x]
        route.reverse()
        route='->'.join([str(i) for i in route])
        print('{: <3}'.format(node),end='')
        print('{: <18}'.format(route),end='')
        print('{:.2f}'.format(dis[node]))

net={0:{'2':0.26},
     1:{'3':0.29},
     2:{},
     3:{'6':0.52,'7':0.39},
     4:{'0':0.38,'7':0.37},
     5:{'1':0.32,'4':0.35,'7':0.28},
     6:{'0':-1.4,'2':-1.2,'4':-1.25},
     7:{'2':0.34}}


if __name__=='__main__':
    Dijkstra_TopologicalOrder(net,s=5)