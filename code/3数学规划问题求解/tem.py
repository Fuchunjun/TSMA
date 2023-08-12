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




    


