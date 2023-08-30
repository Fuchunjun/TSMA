 
import time
import pickle
t1=time.perf_counter()
with open(r'code\4最短路问题\net\SiouxFalls_net.txt','rb') as f:
    net=pickle.load(f)
t2=time.perf_counter()
print(t2 - t1)
