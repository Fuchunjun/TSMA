
import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt
import pandas as pd
num_points = 51
data=pd.read_excel(r'code\5旅行商问题\net\eil51.xlsx')
graph=[]
for _,row in data.iterrows():
    graph.append([row[1],row[2]])
distance_matrix = spatial.distance.cdist(graph, graph, metric='euclidean')
def cal_total_distance(routine):
    num_points, = routine.shape
    return sum([distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)])
from sko.GA import GA_TSP

pop=30
max_iter=20000
prob=0.05

ga_tsp = GA_TSP(func=cal_total_distance, n_dim=51, size_pop=30, max_iter=20000, prob_mut=0.02)
best_points, best_distance = ga_tsp.run()

print('pop{}，max_iter{}，prob_mut{}'.format(pop,max_iter,prob))
print(best_points,best_distance)

