import pandas as pd
data=pd.read_excel(r'code\4最短路问题\SiouxFalls_net.xlsx',usecols='A,B,E')
n=24   #节点数
keys=[]
values=[]
tempdict={}
for k in range(0,n):
    keys.append(k+1)
    for i in range(len(data)):
        if data.iloc[i,0]==k+1:
            tempdict[str(data.iloc[i,1])]=data.iloc[i,2]
    copdict=tempdict.copy()
    values.append(copdict)
    tempdict.clear()
network={k:v for k,v in zip(keys,values)}

print(network)

