import math
import matplotlib.pyplot as plt
import 数值积分

g=lambda x:(x*math.exp(x))/(1+x)**2

listx=[]
listy=[]
for i in range(1,101):
    listx.append(i)
    y=数值积分.sun中矩形(g,0,1,i)
    listy.append(y)
    t=abs(y-0.3591)/0.3591
    print("n=",i,"\t计算值：",y)
#绘图
plt.plot(listx,listy,color="blue")
plt.show()
