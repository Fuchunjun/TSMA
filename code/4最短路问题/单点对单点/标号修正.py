
import pickle
def one2onelabelcorrecting(net,s,e):
    dis=[9999 for _ in range(len(net))]
    par=[-1 for _ in range(len(net))]
    Q=[s-1]
    dis[s-1]=0
    while Q:
        i=Q.pop(0)
        for j,disij in net[i+1].items():
            j=int(j)-1
            if dis[j]>dis[i]+disij and dis[i]+disij<dis[e-1]:
                dis[j]=dis[i]+disij
                par[j]=i+1
                if j not in Q:
                    Q.append(j)
    print(f'{s}-{e}最短路路径成本：',dis[e-1])
    print('路径：',end='')
    route=[e]
    while par[route[-1]-1]!=-1:
        route.append(par[route[-1]-1])
    route.reverse()
    print(route)
with open(r'code\4最短路问题\net\SiouxFalls_net.txt','rb') as f:
    net=pickle.load(f)

one2onelabelcorrecting(net,s=1,e=20)
