#-*- coding: utf-8 -*-

#使用docplex
from docplex.mp.model import Model
#产量，需求，运费
production=[7,4,9]
need=[3,6,5,6]
freight=[[3,11,3,10],[1,9,2,8],[7,4,10,5]]
prob=Model('5.6.1产销平衡')
#添加变量
x=[]
for i in range(len(production)):
    temlist = [
        prob.continuous_var(name=f'X_{i}_{j}', lb=0, ub=production[i])
        for j in range(len(need))
    ]
    x.append(temlist)
#创建目标函数
prob.minimize(sum(freight[i][j]*x[i][j] for i in range(len(production)) for j in range(len(need))))
#添加约束
for i in range(len(production)):
    prob.add_constraint(sum(x[i][j] for j in range(len(need)))==production[i])
for j in range(len(need)) :
    prob.add_constraint(sum(x[i][j] for i in range(len(production)))==need[j])
solution=prob.solve()
print(solution)
'''
结果记录
solution for: 产销平衡
objective: 85
status: OPTIMAL_SOLUTION(2)
X_0_2=5.000
X_0_3=2.000
X_1_0=3.000
X_1_3=1.000
X_2_1=6.000
X_2_3=3.000
'''

#使用cplex
import cplex
'''
production=[7,4,9]
need=[3,6,5,6]
freight=[[3,11,3,10],[1,9,2,8],[7,4,10,5]]
'''
prob=cplex.Cplex()
prob.objective.set_sense(prob.objective.sense.minimize)

names=['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8','x9','x10', 'x11','x12']
obj = [3,11,3,10,1,9,2,8,7,4,10,5]
ub = [7,7,7,7,4,4,4,4,9,9,9,9]
prob.variables.add(names=names, obj=obj,ub=ub)
senses='E'*7
rhs=[7,4,9,3,6,5,6]
rows=[[['x1','x2','x3','x4'],[1,1,1,1]],
      [['x5','x6','x7','x8'],[1,1,1,1]],
      [['x9','x10','x11','x12'],[1,1,1,1]],
      [['x1','x5','x9'],[1,1,1]], 
      [['x2','x6','x10'],[1,1,1]],
      [['x3','x7','x11'],[1,1,1]],
      [['x4','x8','x12'],[1,1,1]]]
prob.linear_constraints.add(lin_expr=rows,rhs=rhs,senses=senses)
prob.solve()
print(prob.solution.get_objective_value())
print(prob.solution.get_values())
'''
结果记录
85.0
[0.0, 0.0, 5.0, 2.0, 3.0, 0.0, 0.0, 1.0, 0.0, 6.0, 0.0, 3.0]
'''
