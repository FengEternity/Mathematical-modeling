# 15%为合格线
data1 = [0.34105, 0.3239975,0.307797625,0.292407744,0.277787357,0.263897989,0.250703089,0.238167935,0.226259538,0.214946561,0.204199233,0.193989271,0.184289808,
0.175075318,0.166321552,0.158005474,0.1501052,0.14259994] # 一次性塑料占比

data2 = [0.025697192,0.050109525,0.073301242,0.095333372,0.116263896,0.136147894,0.155037691,0.172982999,0.190031042,0.206226682,0.221612541,0.236229106,0.250114843,
0.263306294,0.275838171,0.287743455,0.299053475,0.309797994] # 预测减少环境塑料投入量比例

data3 = [90902424.6,177259728,259299166.2,337236632.4,411277225.4,481615788.7,548437423.9,611917977.3,672224503,729515702.5,783942341.9,835647649.4,884767691.6,
931431731.6,975762569.6,1017876866,1057885447,1095893599,] # 减少环境塑料投入量/吨

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = [i for i in range(0,35,2)]

bar = ax.bar(x, data3)

ax2 = plt.twinx()
line1 = ax2.plot(x, data1, '-', label='Single-use plastics', color='mediumseagreen')
line2 = ax2.plot(x, data2, '--', label='Plastic reduction ratio', color='darksalmon')
ax.axvline(x=15, ls='solid', color='#FF4500')   # 添加垂直竖线

plt.xlabel('Percentage reduction of environmental plastic inputs')

# plt.figure(figsize=(6, 4), dpi=100)
plt.style.use('seaborn-darkgrid')  # 设置绘图样式
plt.rcParams['figure.figsize'] = (6.0, 4.0)
plt.rcParams['savefig.dpi'] = 200  #图片像素
plt.rcParams['figure.dpi'] = 200  #分辨率
plt.legend(loc='upper left')
plt.grid()
plt.show()