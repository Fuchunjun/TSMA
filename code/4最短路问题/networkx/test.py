import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
path=r'code\4最短路问题\net\SiouxFalls_net.xlsx'

data=pd.read_excel(path)
nodes=[]
edges=[]
for _,row in data.iterrows():
    init=row[0]
    term=row[1]
    fftt=row[4]
    if init not in nodes:
        nodes.append(init)
    oneedge=(init,term,fftt)
    edges.append(oneedge)

G=nx.DiGraph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)
#nx.write_weighted_edgelist(G, "test.txt")
nx.draw_networkx(G, with_labels=True)
plt.show()



