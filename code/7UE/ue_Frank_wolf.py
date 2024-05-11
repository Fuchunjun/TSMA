import pandas as pd
import matplotlib.pyplot as plt
import time


'''节点'''
class CNode:
    def __init__(self,ID):
        self.ID = ID
        self.Name = None
        self.Position_x = 0
        self.Position_y = 0
        self.Origin_ID = -1
        self.IncomingLink = []
        self.OutgoingLink = []

'''路段'''
class CLink:
    def __init__(self,ID):
        self.ID = ID
        self.pInNode = None
        self.pOutNode = None
        self.FreeFlowTime = 0.0
        self.TravelTime = 0.0
        self.Capacity = 0.0
        self.Alpha = 0.15
        self.Power = 4.0

'''起点'''
class COrigin:
    def __init__(self,ID):
        self.ID = ID
        self.pOriginNode = None
        self.DestinationNode = []
        self.ODDemand = []

'''网络'''
class CNetwork:
    def __init__(self):
        self.m_Node = []
        self.m_Link = []
        self.m_Origin = []
        self.LinkFlow = []
        self.LinkTravelTime = []
        self.MaxUEGap = 0.00000001
        self.UEGap = 1
        self.netdict={}

    #读取节点
    def read_node(self,path):
        data = pd.read_csv(path)
        for ID,row in data.iterrows():
            node = CNode(ID)
            node.Name = str(row['Node'])
            node.Position_x = row['X']
            node.Position_y = row['Y']
            self.m_Node.append(node)
        #print('读取节点完成')
    
    #通过节点名字查找节点编号，返回编号
    def search_node(self,node_name):
        for node in self.m_Node:
            if node.Name == node_name:
                return node.ID

    #读取路段
    def read_link(self,path):
        data = pd.read_csv(path)
        for ID,row in data.iterrows():
            link = CLink(ID)
            link.pInNode = self.m_Node[self.search_node(str(row['Init node']))]
            link.pOutNode = self.m_Node[self.search_node(str(row['Term node']))]
            link.FreeFlowTime = row['Free Flow Time']
            link.Capacity = row['Capacity']
            self.m_Link.append(link)
        #print('读取路段完成')

    #读取起点和OD需求，并建立起点和OD之间的关系
    def read_origin(self,path):
        data = pd.read_csv(path)
        O=0
        ID = 0
        for _,row in data.iterrows():
            if O != row['O']:
                O = row['O']
                origin = COrigin(ID)
                ID += 1
                origin.pOriginNode = self.m_Node[self.search_node(str(row['O']))]
                self.m_Origin.append(origin)
            origin = self.m_Origin[-1]
            origin.DestinationNode.append(self.m_Node[self.search_node(str(row['D']))])
            origin.ODDemand.append(row['Ton'])
        #print('读取起点和OD完成')

    #网络初始化
    def net_init(self):
        self.LinkTravelTime = [0 for i in range(len(self.m_Link))]
        self.LinkFlow = [0 for i in range(len(self.m_Link))]
        #更新节点与路段关系
        for node in self.m_Node:
            for link in self.m_Link:
                if link.pInNode.Name == node.Name:
                    node.OutgoingLink.append(link.ID)
                if link.pOutNode.Name == node.Name:
                    node.IncomingLink.append(link.ID)

    #更新路段阻抗
    def update_link_trvael_time(self):
        for link in self.m_Link:
            self.LinkTravelTime[link.ID] = link.FreeFlowTime*(1+link.Alpha*pow(self.LinkFlow[link.ID]/link.Capacity,link.Power))

    def search_link_id(self,start,end):
        for i in self.m_Link:
            if i.pInNode.ID==start and i.pOutNode.ID==end:
                return i.ID

    def get_shortest_path(self,start,end):
        '''输入节点编号,返回起点和目的地之间的路段集合及花费，使用单队列标号修正'''

        pathpar=[-1 for _ in range(len(self.m_Node))] #父节点
        Q=[start] #队列
        dis=[float('inf') for i in range(len(self.m_Node))] #初始化所有距离为无穷
        dis[start]=0 #起点到起点的距离为0 
        while Q:
            i=Q.pop(0)
            for j,disij in self.netdict[i].items():
                if dis[j]>dis[i]+disij:
                    dis[j]=dis[i]+disij
                    pathpar[j]=i
                    if j not in Q:
                        Q.append(j)
        path=[end]
        while pathpar[path[-1]]!=-1:
            path.append(pathpar[path[-1]])
        path.reverse()
        path_link=[]
        for i in range(len(path)-1):
            path_link.append(self.search_link_id(path[i],path[i+1]))
        return path_link,dis[end]

    def get_all_shortest_path(self,origin):
        '''输入起点，返回起点到所有目的地的路段集合及花费,字典'''
        path_dict={}
        if origin.DestinationNode:
            for D_node in origin.DestinationNode:
                path,_=self.get_shortest_path(origin.pOriginNode.ID,D_node.ID)
                path_dict[D_node.ID]=path
        return path_dict
    
    def get_shortest_path_cost(self,start,end):
         _,cost=self.get_shortest_path(start,end)
         return cost
    
    def get_uegap(self):
        '''计算UE误差'''
        self.update_link_trvael_time()
        num1=0.0
        for i in range(len(self.m_Link)):
            num1+=self.LinkFlow[i]*self.LinkTravelTime[i]
        num2=0.0
        for origin in self.m_Origin:
            for D_node in origin.DestinationNode:
                num2+=origin.ODDemand[origin.DestinationNode.index(D_node)]*self.get_shortest_path_cost(origin.pOriginNode.ID,D_node.ID)
        self.UEGap = 1 - num2/num1

    def allor_nothing_assignment(self):
        '''全有全无交通分配'''
        an_link_flow=[0 for i in range(len(self.m_Link))]
        self.update_link_trvael_time()
        #更新网络字典
        self.netdict.clear()
        for origin in self.m_Origin:
            origin = self.search_node(origin.pOriginNode.Name)
            if origin not in self.netdict:
                self.netdict[origin]={}
                for link in self.m_Link:
                    if link.pInNode.ID==origin:
                        self.netdict[origin][link.pOutNode.ID]=self.LinkTravelTime[link.ID]
        for origin in self.m_Origin:
            path_dict=self.get_all_shortest_path(origin)
            for D_node in origin.DestinationNode:
                for link in path_dict[D_node.ID]:
                    an_link_flow[link]+=origin.ODDemand[origin.DestinationNode.index(D_node)]
        return an_link_flow

    def Optfunction(self,Descent,Lamuda):#计算最优下行方向函数，返回值越大，下降方向越优
        Sum=0
        for i in range(len(self.m_Link)):
            x=self.LinkFlow[i]+Lamuda*Descent[i]
            Sum+=Descent[i]*(self.m_Link[i].FreeFlowTime*(1+self.m_Link[i].Alpha*(x/self.m_Link[i].Capacity)**self.m_Link[i].Power))
        return Sum

    def frank_wolfe(self):
        iter_history=[]
        UEGap_history=[]
        iter=0#迭代次数
        self.LinkFlow=self.allor_nothing_assignment()
        self.get_uegap()
        while self.UEGap>self.MaxUEGap:
            iter_history.append(iter)
            UEGap_history.append(self.UEGap)
            oldlinkflow=self.LinkFlow
            newlinkflow=self.allor_nothing_assignment()
            descent=[]
            for i in range(len(self.m_Link)):
                descent.append(newlinkflow[i]-oldlinkflow[i])
            Lamuda=0
            left=0#二分法求最优步长
            right=1
            mid=0
            f_left=self.Optfunction(descent,left)      
            f_right=self.Optfunction(descent,right)      
            f_mid=0
            if f_left*f_right>0:
                if abs(f_left)>abs(f_right):
                    Lamuda=right
                else:
                    Lamuda=left
            else:
                while right-left>self.MaxUEGap:
                    mid=(left+right)/2
                    f_left=self.Optfunction(descent,left)
                    f_right=self.Optfunction(descent,right)
                    f_mid=self.Optfunction(descent, mid)
                    if f_left*f_mid>0:
                        left=mid
                    else: right=mid
                Lamuda=(left+right)/2
            
            for i in range(len(self.m_Link)):#更新路段流量
                self.LinkFlow[i]+=Lamuda*descent[i] 
            iter+=1
            self.get_uegap()
            if iter%25==0:
                print('第%d次迭代，UEGap=%f'%(iter, self.UEGap))
            if iter == 10001:
                break
        data={'iter':iter_history,
            'UEGap':UEGap_history}
        df=pd.DataFrame(data)
        df.to_csv(r'code\7UE\result\frank_wolf.csv',index=False) 
        
net = CNetwork()
net.read_node(r'code\7UE\net\SiouxFalls_node.csv')
net.read_link(r'code\7UE\net\SiouxFalls_net.csv')
net.read_origin(r'code\7UE\net\SiouxFalls_od.csv')
net.net_init()
T1=time.time() 
net.frank_wolf()
T2=time.time() 
print('耗时：%f'%(T2-T1))


