import pandas as pd

# 数据清洗，实现将第三列中小于1的数换成0
df = pd.read_csv("data.csv", header=None)
data = df.iloc[:,2]
data = data.where(data>1,0)
print(data)
# 实现每十五列数据换成一个新列

# # 读取 CSV 文件，每次读取 15 行
# import pandas as pd
#
# # 读取 CSV 文件，每次读取 15 行
# df = pd.read_csv('data2.csv', header = None)
# res = pd.DataFrame()
# for i in range(-15,1470,15):
#     # print(i)
#     data = df.iloc[i:i+14]
#     res = pd.DataFrame({"{i}":data})
# # print(df)
# print(res)
#
#
# # import pandas as pd
# #
# # # 读取 CSV 文件，每次读取 15 列
# # df = pd.read_csv('data2.csv', header=None)
# #
# # # 创建一个空的列表，用于保存每一块数据
# # chunks = []
# #
# # # 遍历每一块数据
# # for i in range(0, df.shape[1], 15):
# #     # 选择原始的 DataFrame 中的每一块数据
# #     data = df.iloc[:, i:i+15]
# #     # 将每一块数据添加到列表中
# #     chunks.append(data)
# #
# #
# #
# # # 使用 pd.concat 函数将所有的块数据合并成一个 DataFrame
# # df = pd.concat(chunks)
#
# import pandas as pd
#
# # 读取 CSV 文件，每次读取 15 列
# df = pd.read_csv('data2.csv', header=None)
#
# # 创建一个空的列表，用于保存每一块数据
# chunks = []
#
# # 遍历每一块数据
# for i in range(0, df.shape[1], 15):
#     # 选择原始的 DataFrame 中的每一块数据
#     data = df.iloc[:, i:i+15]
#     # 将每一块数据添加到列表中
#     chunks.append(data)
#
# # 使用 pd.concat 函数将所有的块数据合并成一个 DataFrame
# res = pd.concat(chunks, axis=1)
#
# # 输出结果
# print(res)

