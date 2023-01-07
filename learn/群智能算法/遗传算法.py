# 文章地址：https://www.jianshu.com/p/b10203e4902c
# 求解单源最短路径问题


## 环境设定
import numpy as np
import matplotlib.pyplot as plt
from deap import base, tools, creator, algorithms
import random

params = {
    'font.family': 'serif',
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'font.size': 12,
    'legend.fontsize': 'small'
}
plt.rcParams.update(params)

# -------------------------
## 问题定义
creator.create('FitnessMin', base.Fitness, weights=(-1.0,))
creator.create('Individual', list, fitness=creator.FitnessMin)

## 个体编码
geneLength = 10
toolbox = base.Toolbox()
toolbox.register('genPerm', np.random.permutation, geneLength)
toolbox.register('individual', tools.initIterate, creator.Individual, toolbox.genPerm)

## 解码
# 存储每个节点的可行路径
nodeDict = {'1': [2, 3], '2': [3, 4, 5], '3': [5, 6], '4': [7, 8], '5': [4, 6], '6': [7, 9], '7': [8, 9],
            '8': [9, 10], '9': [10]}


def decode(ind):
    # 输入一个优先度序列之后，返回一条从节点1到节点10的可行路径
    path = [1] # 表示起点
    while not path[-1] == 10: # 表示终点
        curNode = path[-1]  # 当前所在节点
        toBeSelected = nodeDict[str(curNode)]  # 获取可以到达的下一个节点列表
        priority = np.asarray(ind)[np.asarray(toBeSelected) - 1]  # 获取优先级,注意列表的index是0-9
        nextNode = toBeSelected[np.argmax(priority)]
        path.append(nextNode)
    return path


## 评价函数
# 存储距离矩阵，用于评价个体
# 12:节点1到节点2之间的距离
costDict = {'12': 36, '13': 27, '24': 18, '25': 20, '23': 13, '35': 12, '36': 23,
            '47': 11, '48': 32, '54': 16, '56': 30, '67': 12, '69': 38, '78': 20,
            '79': 32, '89': 15, '810': 24, '910': 13}


def evaluate(ind):
    path = decode(ind)  # 路径：节点顺序表示
    pathEdge = list(zip(path[::1], path[1::1]))  # 路径：用边表示
    pathLen = 0
    for pair in pathEdge:
        key = str(pair[0]) + str(pair[1])
        if not key in costDict:
            raise Exception("Invalid path!", path)
        pathLen += costDict[key]  # 将该段路径长度加入
    return (pathLen),


toolbox.register('evaluate', evaluate)

## 数据记录
stats = tools.Statistics(key=lambda ind: ind.fitness.values)
stats.register('min', np.min)
stats.register('avg', np.mean)
stats.register('std', np.std)

## 注册需要的工具
toolbox.register('select', tools.selTournament, tournsize=2)
toolbox.register('mate', tools.cxOrdered)
toolbox.register('mutate', tools.mutShuffleIndexes, indpb=0.5)

## 注册参数
toolbox.popSize = 100
toolbox.ngen = 200
toolbox.cxpb = 0.8
toolbox.mutpb = 0.1

## 生成初始族群
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
pop = toolbox.population(toolbox.popSize)

# -------------------------
## 遗传算法
pop, logbook = algorithms.eaSimple(pop, toolbox, cxpb=toolbox.cxpb, mutpb=toolbox.mutpb,
                                   ngen=toolbox.ngen, stats=stats, verbose=True)

## 输出结果
bestInd = tools.selBest(pop,1)[0]
bestFit = bestInd.fitness.values[0]
print('最优解为: '+str(decode(bestInd)))
print('最短路径为: '+str(bestFit))

## 可视化迭代过程
maxFit = logbook.select('min')
avgFit = logbook.select('avg')
plt.plot(maxFit, 'b-', label='Minimum Fitness')
plt.plot(avgFit, 'r-', label='Average Fitness')
plt.xlabel('# Gen')
plt.ylabel('Fitness')
plt.legend(loc='best')
# plt.show()

