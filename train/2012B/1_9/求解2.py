from gurobipy import *

# 创建模型
NLP = Model("NLP")

# 变量声明
x1 = NLP.addVar(lb=1, ub=3, name="x1")
x2 = NLP.addVar(lb=1, ub=3, name="x2")
x3 = NLP.addVar(lb=1, ub=3, name="x3")
x4 = NLP.addVar(lb=1, ub=3, name="x4")

y14 = NLP.addVar(lb=0, ub=300, name="y14")
y23 = NLP.addVar(lb=0, ub=300, name="y23")

# 设置目标函数
NLP.setObjective(y14 * (x1 + x2 + x3) + x2, GRB.MAXIMIZE)

# 添加约束
NLP.addConstr(y14 * y23 >= 20, "Con1")
NLP.addConstr(x1 * x1 + x2 * x2 + x3 * x3 + x4 * x4 == 30, "Con2")

# 表示乘积项
NLP.addConstr(y14 == x1 * x4, "Con_y14")
NLP.addConstr(y23 == x2 * x3, "Con_y23")

NLP.Params.NonConvex = 2

# Optimize model
NLP.optimize()

NLP.write("NLP.lp")

print('**************')
print(' The optimal solution ')
print('**************')
print('Obj is :', NLP.ObjVal)  # 输出目标值
print('x1 is :', x1.x)  # 输出 x1 的值
print('x2 is :', x2.x)  # 输出 x2 的值
print('x3 is :', x3.x)  # 输出 x3 的值
print('x4 is :', x4.x)  # 输出 x4 的值