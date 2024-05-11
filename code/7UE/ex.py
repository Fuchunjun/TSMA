

#第一步：基本类定义（路段，节点，OD对）
import os
class node():#节点类，包含每个节点的坐标信息
    def __init__(self):
        self.ID=None
        self.pos_x=None
        self.pos_y=None
        self.origin=-1
        self.innode=[]#进入节点路段集合
        self.outnode=[]#离开节点路段集合
class link(): #路段类，包含路段的起讫点、自由流行驶时间、容量、BRP路阻函数的参数
    def __init__(self):
        self.ID=None
        self.O_link=None#起点
        self.D_link=None#终点
        self.FFT=None
        self.Traveltime=None
        self.Capacity=None
        self.B=0.15#SiouxFalls网络中路网B与Power系数值均相等，方便期间，统一设置一个初始值
        self.Power=4
class OD():#OD类，记录每一个OD需求信息，包含起点、重点、流量需求
    def __init__(self):
        self.ID=None
        self.origin_node=None
        self.Destination=[]
        self.odlinks_demand=[]
#第二步：定义路网核心函数（路网信息导入、UE分配计算等）
class network():#网络类，核心函数
    def __init__(self):
        self.Nodes=[]#网络包含节点集合
        self.Links=[]#路段集合
        self.Origins=[]#起点集合，即流量发点
        self.num_Nodes=0#节点个数
        self.num_Links=0#路段个数
        self.num_Origins=0#起点个数
        self.Linkflows=[]#路段流量集合
        self.Linktimes=[]#路段行驶时间集合
        self.max_err=0.001#UE最大误差
        self.err=1#初始UE误差
        self.Djpathcost=[]#最短路阻抗集合（Dijkstra算法求得）
        self.Djpath=[]#最短路集合
    def read_nodes(self,path):#读取节点信息
        f=open(path)
        file=f.readlines()
        for i in file:
            row=i.strip('\n').split('\t')
            newnode=node()
            newnode.ID=int(row[0])
            newnode.pos_x=float(row[1])
            newnode.pos_y=float(row[2])
            self.Nodes.append(newnode)
        f.close()
    def read_link(self,path):#读取路段信息
        f=open(path)
        file=f.readlines() 
        linkid=1
        for i in file:
            row=i.strip('\n').split('\t')
            newlink=link()
            newlink.ID=linkid
            newlink.O_link=self.Nodes[int(row[0])-1]
            newlink.D_link=self.Nodes[int(row[1])-1]
            newlink.FFT=float(row[4])
            newlink.Capacity=float(row[2])
            newlink.O_link.outnode.append(newlink.ID)
            newlink.D_link.innode.append(newlink.ID)
            
            
            #self.Nodes[int(row[0])-1].innode.append(newlink.ID)
            linkid+=1
            self.Links.append(newlink) 
        f.close()
    def read_od(self,path):#读取OD信息
        f=open(path)
        file=f.readlines() 
        linkid=1
        for i in file:
            row=i.strip('\n').split('\t')
            newnode=self.Nodes[int(row[0])-1]
            if newnode.origin==-1:
                neworigin=OD()
                self.num_Origins+=1
                neworigin.ID=self.num_Origins
                neworigin.origin_node=newnode
                self.Nodes[int(row[0])-1].origin=neworigin.ID
                self.Origins.append(neworigin)
            else:
                neworigin=self.Origins[newnode.origin-1]
                
            self.Origins[newnode.origin-1].Destination.append(self.Nodes[int(row[1])-1].ID)
            self.Origins[newnode.origin-1].odlinks_demand.append(float(row[2]))
                
        f.close()        
    def Dijkstra(self,start,end):#Dijkstra求解最短路（也叫标号法）
        startpos=0
        endpos=1
        path=[]
        checkpath=[None for i in range(len(self.Nodes))]
        boolcheckpath=[]
        self.Djpathcost=[]
        self.Djpath=[None for i in range(len(self.Nodes))]
        bscanStatus=[None for i in range(len(self.Nodes))]
        for i in range(len(self.Nodes)):
            self.Djpath.append(-1)
            self.Djpathcost.append(9999999)#标号法初始路阻最大
            boolcheckpath.append(False)
            
        self.Djpathcost[start-1]=0
        checkpath[0]=start-1
        while startpos!=endpos:
            if startpos>=len(self.Nodes):
                startpos=0
            i=checkpath[startpos]
            startpos+=1
            newnode=self.Nodes[i]
            for j in range(len(newnode.outnode)):
                newlink=self.Links[newnode.outnode[j]-1]
                k=newlink.D_link.ID
                tt=newlink.Traveltime
                if self.Djpathcost[k-1]>self.Djpathcost[i]+tt:
                    self.Djpathcost[k-1]=self.Djpathcost[i]+tt
                    self.Djpath[k-1]=i
                    if endpos>=len(self.Nodes):
                        endpos=0
                    checkpath[endpos]=k-1
                    endpos+=1
                    bscanStatus[k-1]=True
        return self.Djpathcost[end-1]
    def Dijkstra_path(self,start,end):#记录最短路径，与上述函数基本相同，输出结果不同，为了后面调用方便，写了两次
        startpos=0
        endpos=1
        path=[]
        checkpath=[None for i in range(len(self.Nodes))]
        boolcheckpath=[]
        self.Djpathcost=[]
        self.Djpath=[None for i in range(len(self.Nodes))]
        bscanStatus=[None for i in range(len(self.Nodes))]
        for i in range(len(self.Nodes)):
            self.Djpath.append(-1)
            self.Djpathcost.append(9999999)
            boolcheckpath.append(False)         
        self.Djpathcost[start-1]=0
        checkpath[0]=start-1
        while startpos!=endpos:
            if startpos>=len(self.Nodes):
                startpos=0
            i=checkpath[startpos]
            startpos+=1
            newnode=self.Nodes[i]
            for j in range(len(newnode.outnode)):
                newlink=self.Links[newnode.outnode[j]-1]
                k=newlink.D_link.ID
                tt=newlink.Traveltime
                if self.Djpathcost[k-1]>self.Djpathcost[i]+tt:
                    self.Djpathcost[k-1]=self.Djpathcost[i]+tt
                    self.Djpath[k-1]=i
                    if endpos>=len(self.Nodes):
                        endpos=0
                    checkpath[endpos]=k-1
                    endpos+=1
                    bscanStatus[k-1]=True
        Djpathlink=[]
        point_out=end-1
        while True:
            i=0
            point_in=self.Djpath[point_out]
            for j in range(len(self.Links)):
                newlink=self.Links[j]
                if point_in==newlink.O_link.ID-1 and point_out==newlink.D_link.ID-1:
                    Djpathlink.insert(0,newlink.ID)
                    point_out=point_in
            i+=1
            if point_in==start-1:
                break        
        return Djpathlink
  
    def all_none(self):#全有全无分配函数
        all_none_linkflow=[0 for i in range(len(self.Links))]
        for i in range(len(self.Links)):           
            self.Links[i].Traveltime=self.Links[i].FFT*(1+self.Links[i].B*(self.Linkflows[i]/self.Links[i].Capacity)**self.Links[i].Power)#更新路段行驶时间
            all_none_linkflow[i]=0
        for i in range(len(self.Origins)):       
            o_node=self.Origins[i].origin_node.ID
            for j in range(len(self.Origins[i].Destination)):
                d_node=self.Origins[i].Destination[j]
                demand=self.Origins[i].odlinks_demand[j]
                Djpathlink=self.Dijkstra_path(o_node,d_node)#找最短路
                for index in Djpathlink:
                    all_none_linkflow[index-1]+=demand#将流量加载到最短路上                  
        return all_none_linkflow
    
    def getUEerr(self):#计算UE误差
        sum1=0
        for i in range(len(self.Links)):
            
            self.Links[i].Traveltime=self.Links[i].FFT*(1+self.Links[i].B*(self.Linkflows[i]/self.Links[i].Capacity)**self.Links[i].Power)
            sum1+=self.Links[i].Traveltime*self.Linkflows[i]#计算流量与行驶时间的乘积（UE公式中的积分项）
        
        sum2=0
        for i in range(len(self.Origins)):
            for j in range(len(self.Origins[i].Destination)):
                demand=self.Origins[i].odlinks_demand[j]
                cost=self.Dijkstra(self.Origins[i].origin_node.ID,self.Origins[i].Destination[j])
                sum2+=demand*cost#计算需求与行驶时间的乘积
           
        return 1-sum2/sum1
    def Optfunction(self,Descent,Lamuda):#计算最优下行方向函数，返回值越大，下降方向越优
        Sum=0
        for i in range(len(self.Links)):
            x=self.Linkflows[i]+Lamuda*Descent[i]
            Sum+=Descent[i]*(self.Links[i].FFT*(1+self.Links[i].B*(x/self.Links[i].Capacity)**self.Links[i].Power))
        return Sum
 
    def Frank_Wolfe(self):#Frank-Wolfe主函数
        
        iter=0#迭代次数
        self.Linkflows=[0 for i in range(len(self.Links))]
        self.Linkflows=self.all_none()
        while self.err>self.max_err:
            oldlinkflow=self.Linkflows
            newlinkflow=self.all_none()
            Descent=[]
            for i in range(len(self.Links)):
                Descent.append(newlinkflow[i]-self.Linkflows[i])
            Lamuda=0
            left=0#二分法求最优步长
            right=1
            mid=0
            f_left=self.Optfunction(Descent,left)      
            f_right=self.Optfunction(Descent,right)      
            f_mid=0
            if f_left*f_right>0:
                if abs(f_left)>abs(f_right):
                    Lamuda=right
                else:
                    Lamuda=left
                    
            else:              
                while right-left>self.max_err:
                    mid=(left+right)/2
                    f_left=self.Optfunction(Descent,left)
                    f_right=self.Optfunction(Descent,right)
                    f_mid=self.Optfunction(Descent, mid)
                    if f_left*f_mid>0:
                        left=mid
                    else: right=mid
                Lamuda=(left+right)/2
    
            for i in range(len(self.Links)):#更新路段流量
                self.Linkflows[i]+=Lamuda*Descent[i] 
            iter+=1
            self.err=self.getUEerr()        

        #print(self.Linkflows)
        
net=network()
#读取路网文件
net.read_nodes(r'code\7UE\net\SiouxFalls_node.csv')
net.read_link(r'code\7UE\net\SiouxFalls_net.csv')
net.read_od(r'code\7UE\net\SiouxFalls_od.csv')
net.Frank_Wolfe()#F-W主函数
print(net.Linkflows)#输出每条路段上的流量
           
