#-*- coding: utf-8 -*-
from docplex.mp.model import Model
cost=[[2,15,13,4],[10,4,14,15],[9,14,16,13],[7,8,11,9]]
prob=Model('5.6.3指派问题')
x=prob.integer_var_matrix(keys1=list(range(len(cost))),keys2=list(range(len(cost[1]))),lb=0,ub=1,name='x')
prob.minimize(sum(x[i,j]*cost[i][j] for i in range(len(cost)) for j in range(len(cost[1]))))
for i in range(len(cost)):
    prob.add_constraint(sum(x[i,j] for j in range(len(cost[1])))==1)
for j in range(len(cost[1])):
    prob.add_constraint(sum(x[i,j] for i in range(len(cost)))==1)
solution=prob.solve()
print(solution)
'''
结果记录
solution for: 5.6.3指派问题
objective: 28
status: OPTIMAL_SOLUTION(2)
x_0_3=1
x_1_1=1
x_2_0=1
x_3_2=1
'''
