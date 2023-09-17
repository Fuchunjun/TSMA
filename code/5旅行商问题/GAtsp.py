import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
import math
from itertools import combinations
import matplotlib.pyplot as plt
population=[]
#读取坐标文件,返回城市名字，位置列表
def read_data(path):
    global city_name,city_position
    city_name=[]
    city_position=[]
    data=pd.read_excel(path)
    for _,rows in data.iterrows():
        city_name.append(rows[0])
        city_position.append([rows[1],rows[2]])
    return city_name,city_position

#计算距离矩阵,返回城市距离
def get_city_distance(city_name,city_position):
    count=len(city_name)
    global city_distance
    city_distance=np.zeros([count,count])
    for i in range(count):
        for j in range(count):
            city_distance[i][j]=math.sqrt((city_position[i][0]-city_position[j][0])**2+(city_position[i][1]-city_position[j][1])**2)
    return city_distance

#计算一条线路的距离
def get_distance(route):
    distance=0
    for i in range(len(route)):
        if i==len(route)-1:
            distance+=city_distance[route[i]][route[0]]
        else:
            distance+=city_distance[route[i]][route[i+1]]
    return distance

#计算适应度
def get_fitness(route):
    return 1/get_distance(route)

#计算最大适应度,返回最大适应度及对应染色体
def get_max_fitness(population):
    fitness_list=[[get_fitness(route),route] for route in population]
    fitness_list.sort(key=lambda x:x[0],reverse=True)
    return fitness_list[0][0],fitness_list[0][1]

#返回种群最优解，最短路径距离及对应路径
def get_best_result(population):
    result=[[get_distance(route),route] for route in population]
    result.sort(key=lambda x:x[0])
    return  result[0][0],result[0][1]

#返回交叉集合和变异集合，概率自适应
def select(population,generation_i,generation_num):
    fitness_max=get_max_fitness(population)[0]
    fitness_average=sum([get_fitness(route) for route in population])/len(population)
    cross_set=[]
    mutate_set=[]
    for route in population:
        #交叉集合
        p_c_min=0.9
        fitness=get_fitness(route)
        if generation_i<=generation_num/4:p_c_max=1
        elif generation_i>generation_num/4 and generation_i<=3*generation_num/4:p_c_max=0.98
        else: p_c_max=0.95   #p_c_max=0.95
        if fitness<fitness_average:
            p_c_i=p_c_max
        else:
            p_c_i=p_c_max-(p_c_max-p_c_min)*(0.5*generation_i/generation_num+0.5*(fitness-fitness_average)/(fitness_max-fitness_average))
        if random.random()<p_c_i:
            cross_set.append(route)
        #变异集合
        p_m_max=0.5  #p_m_max=0.5
        if generation_i<=generation_num/4:p_m_min=0.1
        elif generation_i>generation_num/4 and generation_i<=3*generation_num/4:p_m_min=0.2
        else: p_m_min=0.3
        if fitness<fitness_average:
            p_m_i=p_m_max
        else:
            p_m_i=p_m_min+(p_m_max-p_m_min)*(0.5*generation_i/generation_num+0.5*(fitness-fitness_average)/(fitness_max-fitness_average))
        if random.random()<p_m_i:
            mutate_set.append(route)
    return cross_set,mutate_set

#交叉算子(顺序交叉)
def cross(cross_set):
    cross_children=[]
    cross_list=list(combinations(cross_set,2))
    for count in range(len(cross_list)):
        par1=cross_list[count][0].copy()
        par2=cross_list[count][1].copy()
        pos1=random.randint(0,len(par1)-2)
        pos2=random.randint(pos1+1,len(par1)-1)
        child1=[-1 for _ in range(len(par1))]
        child2=[-1 for _ in range(len(par1))]
        child1[pos1:pos2+1]=par1[pos1:pos2+1]
        child2[pos1:pos2+1]=par2[pos1:pos2+1]
        for i in child1:
            if i!=-1:
                par2.remove(i)
        for i in child2:
            if i!=-1:
                par1.remove(i)
        iter1=iter(par1)
        iter2=iter(par2)
        for i in range(len(child1)):
            if child1[i]==-1:
                child1[i]=next(iter2)
            if child2[i]==-1:
                child2[i]=next(iter1)
        cross_children.append(child1)
        cross_children.append(child2)
    return cross_children

#变异算子
#随机交换变异
def mutate_随机交换变异(mutate_set):
    mutate_children=[]
    mutate_list=mutate_set.copy()
    for child in mutate_list:
        p=random.sample(range(len(child)),2)
        p1=p[0]
        p2=p[1]
        tem=child[p1]
        child[p1]=child[p2]
        child[p2]=tem
        mutate_children.append(child)
    return mutate_children
#随机插入变异
def mutate_随机插入变异(mutate_set):
    mutate_children=[]
    mutate_list=mutate_set.copy()
    for child in mutate_list:
        pos=random.sample(range(len(child)),2)
        tem=child[pos[0]]
        child.remove(child[pos[0]])
        child.insert(pos[1],tem)
        mutate_children.append(child)
    return mutate_children


#锦标赛选择,二元
def championship_select(population,population_num):
    new_population=[]
    count=1
    while count<=population_num:
        player=random.sample(population,2)
        if get_distance(player[0])<get_distance(player[1]):
            winner=player[0]
        else:
            winner=player[1]
        if winner not in new_population:
            new_population.append(winner)
            count+=1
    return new_population


def ga_tsp(path,population_num,generation_num):
    gen=[0]
    #读取城市坐标
    city_name,city_position=read_data(path);print('已读取城市信息')
    #计算城市距离
    city_distance=get_city_distance(city_name,city_position);print('已计算城市距离')
    #生成初代种群
    city_num=len(city_name)
    tem_route=[i for i in range(city_num)]
    population=[]
    for _ in range(population_num):
        route=tem_route.copy()
        random.shuffle(route)
        population.append(route)
    print('已生成初代种群')
    #记录最优解
    best_distance_history=[]
    best_distance,best_route=get_best_result(population)
    best_distance_history.append(best_distance)
    print('开始迭代')
    for generation_i in range(1,generation_num+1):
        cross_set,mutate_set=select(population,generation_i,generation_num)   #自适应概率选择交叉，变异
        children=cross(cross_set)+mutate_随机插入变异(mutate_set)     #交叉变异形成子代
        children_best_distance,children_best_route=get_best_result(children)  #子代最优染色体
        best_distance_history.append(children_best_distance)   
        gen.append(generation_i)
        if children_best_distance<best_distance:
            best_route=children_best_route
            best_distance=children_best_distance
        population=population+children
        population=championship_select(population,population_num)    #锦标赛选择形成下一代
        #print('交叉集合{},变异集合{: <3}'.format(len(cross_set),len(mutate_set)),end=' ')
        print('当前第{}代，最短距离{}'.format(generation_i,best_distance))
    #输出并保存结果
    print(best_route,best_distance)
    plt.plot(gen,best_distance_history)
    plt.title('{}_{}_{}'.format(population_num,generation_num,best_distance))
    plt.savefig(r'code\5旅行商问题\结果\{}_{}_{}.jpg'.format(population_num,generation_num,best_distance))
    

if __name__=='__main__':
    for _ in range(10):
        ga_tsp(path=r'code\5旅行商问题\net\eil51.xlsx',population_num=28,generation_num=18000)

    





    



