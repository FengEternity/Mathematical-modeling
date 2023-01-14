# 数据清洗1：将数据修改为csv文件格式
# with open("8 50%随机.csv", 'r+') as f:
#     for line in f:
#         line = line.replace('                                       ', '')
#         line = line.replace('                                   ', '')
#         line = line.replace('                                  ', '')
#         line = line.replace('        ', ',')
#         line = line.replace('           ', ',')
#         line = line.replace('       ', ',')
#         line = line.replace(',,,, ', '')
#         line = line.replace('    ', '')
#
#         print(line)


# with open('K.csv', 'r+') as f:
#     for line in f:
#         line = line.replace('K.csv( ', '')
#         line = line.replace(')', '')
#         line = line.replace('6.0', '6')
#         print(line)


import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('8占比与总数关系.csv')
plt.figure(figsize=(10, 8), dpi=80)

x = data['proportion']
y = data['total']

plt.plot(x,y)

for x1, y1 in zip(x, y):
    plt.text(x1, y1, str(y1), ha='center', va='bottom', fontsize=10)

plt.show()