# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def fac(n):
#     return (1 if n < 1 else n * fac(n - 1))
# def item(n,x):
#     return (-1)**n*x**(2*n+1)/fac(2*n+1)
# def mysin(n,x):
#     return (0 if n < 0 else mysin(n - 1, x) + item(n, x))
#
# x = np.linspace(-2*np.pi,2*np.pi,101)
# plt.plot(x,np.sin(x),'*-')
# str = ['v-','H--','-.']
# for n in [1,2,3]:
#     plt.plot(x,mysin(2*n-1,x),str[n-1])
# plt.legend(['sin','n=1','n=3','n=5'])
# plt.savefig('figure3_16.png', dpi=500)
# plt.show()

import numpy as np, numpy.linalg as ng
import matplotlib.pyplot as plt

N = 4
v = 1.0
d = 200.0
time = 400.0
divs = 201
xy = np.array([[-d, d], [d, d], [d, -d], [-d, -d]])
T = np.linspace(0, time, divs)
dt = T[1] - T[0]
xyn = np.empty((4, 2))
Txy = xy
for n in range(1, len(T)):
    for i in [0, 1, 2, 3]:
        j = (i + 1) % 4
        dxy = xy[j] = xy[i]
        dd = dxy / ng.norm(dxy)
        xyn[i] = xy[i] + v * dt * dd
    Txy = np.c_[Txy, xyn]
    xy = xyn.copy()

for i in range(N):
    plt.plot(Txy[i, ::2], Txy[i, 1::2])

plt.show()
