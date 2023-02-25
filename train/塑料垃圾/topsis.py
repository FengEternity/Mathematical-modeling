# #完整代码：
# import numpy as np
# import pandas as pd
#
# data = pd.read_excel('data.xlsx')  #读取原始数据
# label_need=data.keys()[1:]
# df=data[label_need]
# a=np.array(df)
# [n, m]=a.shape
# cs=a.sum(axis=0)  #逐列求和
# P=1/cs*a   #求特征比重矩阵
# e=-(P*np.log(P)).sum(axis=0)/np.log(n)  #计算熵值
# g=1-e   #计算差异系数
# w = g / sum(g)  #计算权重
# F = P @ w       #计算各对象的评价值
# print("\nP={}\ne={}\ng={}\nw={}\nF={}".format(P,e,g,w,F))
# print('各个学生评价值从高到低的次序为:')
# print(np.argsort(-F)+1)


import pandas as pd
import numpy as np

data=pd.read_excel('data.xlsx')

label_need=data.keys()[1:]
data1=data[label_need].values
[m,n]=data1.shape
data2=data1.copy().astype('float')
for j in range(0,n):
    data2[:,j]=data1[:,j]/np.sqrt(sum(np.square(data1[:,j])))

w=[0.07692308, 0.07692308, 0.23076923, 0.38461538, 0.23076923]
R=data2*w

r_max=np.max(R,axis=0)
r_min=np.min(R,axis=0)
d_z = np.sqrt(np.sum(np.square((R -np.tile(r_max,(m,1)))),axis=1))
d_f = np.sqrt(np.sum(np.square((R -np.tile(r_min,(m,1)))),axis=1))

s=d_f/(d_z+d_f )
Score=100*s/max(s)
for i in range(0,len(Score)):
    print(Score[i])
