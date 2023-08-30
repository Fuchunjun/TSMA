
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

net={0:{'2':0.26},
     1:{'3':0.29},
     2:{},
     3:{'6':0.52,'7':0.39},
     4:{'0':0.38,'7':0.37},
     5:{'1':0.32,'4':0.35,'7':0.28},
     6:{'0':-1.4,'2':-1.2,'4':-1.25},
     7:{'2':0.34}}