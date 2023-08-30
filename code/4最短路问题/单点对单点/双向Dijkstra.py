
import pickle
def bidirection_dijkstra(net,s,e):
    dis_s=[9999 for _ in range(len(net))]  #s表示前向搜索，e表示后向搜索
    dis_e=[9999 for _ in range(len(net))]
    par_s=[-1 for _ in range(len(net))]
    par_e=[-1 for _ in range(len(net))]
    visited_s=[0 for _ in range(len(net))]
    visited_e=[0 for _ in range(len(net))]
    #初始化
    D=9999
    s-=1
    e-=1
    t_s = list(range(len(net)))
    t_e = list(range(len(net)))
    visited_s[s]=1
    visited_e[e]=1
    dis_s[s]=0
    dis_e[e]=0
    for _ in range(len(net)):
        min_s=9999
        min_e=9999
        i_s=0
        i_e=0
        j_x=0
        for j in range(len(net)):
            if visited_s[j]==0 and dis_s[j]<min_s:
                min_s=dis_s[j]
                i_s=j
            if visited_e[j]==0 and dis_e[j]<min_e:
                min_e=dis_e[j]
                i_e=j
        t_s.pop(i_s)
        visited_s[i_s]=1
        t_e.pop(i_e)
        visited_e[i_e]=1
        for j,disij in net[i_s+1].items():
            j=int(j)-1
            if dis_s[j]>dis_s[i_s]+disij:
                dis_s[j]=dis_s[i_s]+disij
                par_s[j]=i_s+1
                if visited_e[j]==1 and D>dis_s[j]+dis_e[j]:# 更新上界
                    D=dis_s[j]+dis_e[j]
                    j_x=j     #最优中继节点j_x
                    
        for j,disij in net[i_e+1].items():
            j=int(j)-1
            if dis_e[j]>dis_e[i_e]+disij:
                dis_e[j]=dis_e[i_e]+disij
                par_e[j]=i_e+1
                if visited_s[j]==1 and D>dis_s[j]+dis_e[j]:# 替换上界
                    D=dis_s[j]+dis_e[j]
                    j_x=j     #最优中继节点j_x
        if dis_s[i_s]+dis_e[i_e]>=D:
            break
    print(D)
    print(j_x)
    print(par_s)
    print(par_e)


with open(r'code\4最短路问题\net\SiouxFalls_net.txt','rb') as f:
    net=pickle.load(f)

bidirection_dijkstra(net,s=1,e=20)

