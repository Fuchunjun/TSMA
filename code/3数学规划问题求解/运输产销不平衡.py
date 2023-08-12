#-*- coding: utf-8 -*-
from docplex.mp.model import Model
#产量，需求，运费
production=[50,60,50]
lneeds=[30,70,0,10]
hneeds=[50,70,30,float('inf')]
freight=[[16,13,22,17],[14,13,19,15],[19,20,23,float('inf')]]

prob=Model('5.6.2产销不平衡')
#添加变量
x = prob.continuous_var_matrix(
    keys1=list(range(len(production))),
    keys2=list(range(len(lneeds))),
    name='x',
)
for i,p in enumerate(production):
    for j in range(len(lneeds)):
        prob.add_constraint(x[i,j]<=p)
#目标函数
prob.minimize(sum(x[(i,j)]*freight[i][j] for i in range(len(production)) for j in range(len(lneeds))))
#设置约束
for i in range(len(production)):
    prob.add_constraint(prob.sum(x[(i,j)] for j in range(len(lneeds)))==production[i])
for j in range(len(lneeds)):
    prob.add_constraint(prob.sum(x[(i,j)] for i in range(len(production)))<=hneeds[j])
    prob.add_constraint(prob.sum(x[(i,j)] for i in range(len(production)))>=lneeds[j])
#导出lp文件，检查错误
#prob.export_as_lp('prob.lp')
solution=prob.solve()
print(solution)
'''
结果记录
solution for: 产销不平衡
objective: 2460
status: OPTIMAL_SOLUTION(2)
x_0_1=50.000
x_1_1=20.000
x_1_3=40.000
x_2_0=50.000
'''




