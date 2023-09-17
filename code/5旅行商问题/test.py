from itertools import product
import random
import GAtsp
from itertools import combinations
c1=[1,2,3,4,5,6,7,8,9]
c2=[5,4,6,9,2,1,7,8,3]

c=[c1,c2]
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
        print(pos1,pos2)
        print(par1,par2)
        print(child1,child2)
    return cross_children

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

a=mutate_随机插入变异(c)
print(a)