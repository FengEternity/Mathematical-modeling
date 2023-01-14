# https://blog.csdn.net/m0_46778675/article/details/119859399

# 导入相关的库
import numpy as np
from scipy.optimize import minimize


# 定义目标函数
def objective(x):
    return -x


# 定义约束条件
# =
def constraint1(m):
    return m[1] - 0


# >=
def constraint2(t, i, j):
    return t[i][j] - 12


# >=
def constraint3(m, k, x):
    return (m[x] + k[x]) - 180


# >=
def constraint4(m, x):
    return m[x] + 6 - 180


# >=
def constraint5(k, i):
    return k[i] - 6


# >=
def constraint6(k, i):
    return 18 - k[i]


# >= 存疑
def constraint7(v, t, k):
    return 225 - sum(v[:k] * t[:k])


# =
def constraint8(v, t, k, i):
    return sum(v[:k + 1] * t[:k + 1]) - 225


# =
def constraint9(v, t, i, j):
    return t[i][j] - (225 - sum(v[:j] * t[i][:j])) / v[i]


# 约束条件应该是v等于4，或者等于8
# def constraint10(v,i):
#     return v[i] - 4

# >=
def constraint10(U, Y):
    return Y - abs(U)


# =
def constraint11(Y, L):
    return 225 / (Y + 1) - L


# >=
def constraint12(v, L, i):
    return 12 * v[i] - L


# >=
def constraint13(D):
    return D - 1


# >=
def constraint14(D):
    return 180 - D


# =
def constraint15(h, D, m, i):
    return h[i] - D + m[i]


# 存疑,如何表示前面的约束条件和不等于
# def constraint16(m, k, D, i):
#     return m[i] + k[i] - D

# 存疑,如何表示前面的约束条件和不等于
def constraint17(v, t, p, q, j):
    return sum(v[p] * t[p][j]) - sum(v[q] * t[q][j])


# >=
def constraint18(h, k, i):
    return h[i] + k[i] + 1


# >=
def constraint19(h, k, i):
    return h[i]


# =
def constraint20(v, t, n, L, i, j):
    return v[i] * t[i][j] - n * L


# >=
def constraint21(n):
    return n


# >=
def constraint22(n, L):
    return 12 * 8 / L - n


# >=
def constraint23(m, i):
    return m[i] - 1


# >=
def constraint24(m, i):
    return 180 - m[i]


# 每一个约束为一部字典，其中 type 表示约束类型：ineq 为大于等于，eq 为等于；
# fun 表示约束函数表达式，即 step2 中的自定义函数。
con1 = {'type': 'eq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'ineq', 'fun': constraint3}
con4 = {'type': 'ineq', 'fun': constraint4}
con5 = {'type': 'ineq', 'fun': constraint5}
con6 = {'type': 'ineq', 'fun': constraint6}
con7 = {'type': 'ineq', 'fun': constraint7}
con8 = {'type': 'eq', 'fun': constraint8}
con9 = {'type': 'eq', 'fun': constraint9}
con10 = {'type': 'ineq', 'fun': constraint10}
con11 = {'type': 'eq', 'fun': constraint11}
con12 = {'type': 'ineq', 'fun': constraint12}
con13 = {'type': 'ineq', 'fun': constraint13}
con14 = {'type': 'ineq', 'fun': constraint14}
con15 = {'type': 'eq', 'fun': constraint15}
# con16 = {'type': 'eq', 'fun': constraint4}
con17 = {'type': 'ineq', 'fun': constraint17}  # 有bug
con18 = {'type': 'ineq', 'fun': constraint18}
con19 = {'type': 'ineq', 'fun': constraint19}
con20 = {'type': 'eq', 'fun': constraint20}
con21 = {'type': 'ineq', 'fun': constraint21}
con22 = {'type': 'ineq', 'fun': constraint22}
con23 = {'type': 'ineq', 'fun': constraint23}
con24 = {'type': 'ineq', 'fun': constraint24}

# 4个约束条件
cons = ([con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12,
         con13, con14, con15, con17, con18, con19, con20, con21, con22, con23,
         con24])

# 决策变量的符号约束

b = (0.0, None)  # 即决策变量的取值范围为大于等于0
bnds = (b, b, b)

m = [i for i in range(0,1000)]
k = [i for i in range(0,1000)]
D = [i for i in range(0,1000)]
h = [i for i in range(0,1000)]
n = [i for i in range(0,1000)]
Y = [i for i in range(0,1000)]



x0 = np.array([0])  # 定义初始值
solution = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)
