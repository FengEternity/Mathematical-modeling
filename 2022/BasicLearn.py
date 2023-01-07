#numpy,matplotlib,pandas为数据分析三剑客。
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#使用numpy产生数据
x = np.arange(-5, 5 , 0.1)
'''
np.arange()函数返回一个有终点和起点的固定步长的数列，里面可以设置1-3个参数，依次是起点数，步长和终点数。
一个参数时，参数值为终点，起点取默认值0，步长取默认值1。
两个参数时，第一个参数为起点，第二个参数为终点，步长取默认值1。
三个参数时，第一个参数为起点，第二个参数为终点，第三个参数为步长。其中步长支持小数。
'''
y = x*3

#创建窗口和子图
#方法一：先创建窗口，再创建子图（空白处绘制，子图填满窗口）
fig = plt.figure(num = 1, figsize=(15, 8), dpi=80) #开启一个窗口，设置宽高和dpi。
'''
figure()函数说明
figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
num:图像编号或名称，数字为编号 ，字符串为名称
figsize:指定figure的宽和高，单位为英寸；
dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值（默认值）为80。1英寸等于2.5cm,A4纸是 21*30cm的纸张 
facecolor:背景颜色
edgecolor:边框颜色
frameon:是否显示边框

'''
ax1 = fig.add_subplot(1,1,1) #参数之间的，可以省略。
#通过add_subplot()函数添加子图，三个参数依次表示：窗口中子图的总行数、总列数，本子图为从左往右从上往下第几块区域。
'''ax2 = fig.add_subplot(2,1,2)
print(fig, ax1, ax2) #打印窗口和子图参数'''

#设置子图的基本元素
ax1.set_title('python_drawing') #设置标题
ax1.set_xlabel('x_name') #设置X轴名称
ax1.set_ylabel('y_name') #设置Y轴名称
plt.axis([-5,5,-16,16]) #设置横、纵坐标的范围
'''
#上面axis（）函数的结果可以通过以下两个函数分解实现
ax1.set_xlim(-6,6)
ax1.set_ylim(-10,10)
'''
#定义横、纵向主刻度标签的刻度差，就是隔几个刻度才显示一个标签文本。
xmajorLocator = MultipleLocator(2)
ymajorLocator = MultipleLocator(2)
#X轴、Y轴应用定义的横、纵向主刻度，如果不应用将采用默认刻度。
ax1.xaxis.set_major_locator(xmajorLocator)
ax1.yaxis.set_major_locator(ymajorLocator)
#X轴、Y轴的网格应用定义的横、纵向主刻度。
ax1.xaxis.grid(True, which='major') #两个参数，为Flase时不显示网格，括号为空为默认值（显示网格，采用主刻度）。
ax1.yaxis.grid(True, which='major')

'''
#删除X轴、Y轴刻度
ax1.set_xticks([])
ax1.set_yticks([])
# 自由设置X轴、Y轴刻度
ax1.set_xticks([-5,-2,-1,1,3,5])
ax1.set_yticks([-1,-3,-7,-9])
'''

'''#设置刻度的显示文本,设置刻度时前后要各多一个，rotation旋转角度，fontsize字体大小（small/medium/large）
ax1.set_xticklabels(labels=['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8'], rotation = -45, fontsize = 'small')
ax1.set_yticklabels(labels=['y1', 'y2'], rotation = 0, fontsize = 'medium')
'''

#设置线条参数
plot1 = ax1.plot(x,y, linestyle='',marker = 's',color='g',label = 'legend8',alpha=0.5,linewidth=2)
#alpha透明度，label为图例中线条名称，linewidth线条宽度。
'''
plt.plot()函数说明：
一、plt.plot(x,y,format_string,**kwargs)

x,y:x轴数据，y轴数据

format_string:控制曲线的格式字串,有线条风格、线条标记、线条颜色三部分。
线条风格，linestyle（或ls）=’-’ 当参数为空时是点图
线条标记，marker = ‘o’  
线条颜色，color=’g’

以上三个参数的可选值
线条风格（linestyle）
‘-‘                         实线  
‘:’                         虚线   
‘–’                         破折线 
‘None’ ’’               什么都不画    
‘-.’                        点划线
线条标记（marker）
‘.’                 点
‘D’                 菱形  
‘s’                 正方形
‘h’                 六边形1    
‘*’                 星号
‘H’                 六边形2    
‘d’                 小菱形
‘_’                 水平线 
‘v’                 一角朝下的三角形
‘8’                 八边形 
‘<’                 一角朝左的三角形
‘p’                 五边形 
‘>’                 一角朝右的三角形
‘,’                 像素  
‘^’                 一角朝上的三角形
‘+’                 加号  
‘\  ‘               竖线
‘None’,’’         无   
‘x’                 X
线条颜色（color）
b               蓝色  
g               绿色
r               红色  
y               黄色
c               青色
k               黑色   
m               洋红色 
w               白色

关于*kwargs：
有时候，函数的参数里会有(*args, **kwargs)，都是可变参数，*args表示无名参数，是一个元组
**kwargs是键值参数，相当于一个字典
比如你输入参数为：(1,2,3,4,k,a=1,b=2,c=3)，*args=(1,2,3,4,k)，**kwargs={'a':'1,'b':2,'c':3}
如果同时使用这两个参数，*args要在**kwargs之前
本例子中，linestyle='',marker = 's',color='g', alpha=0.5,linewidth=2等键值对都是**kwargs
'''
#添加数字标签
for a,b in zip(x,y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=12)
'''
首先，前边设置的x、y值其实就代表了不同柱子在图形中的位置（坐标），通过for循环找到每一个x、y值的相应坐标——a、b，
再使用plt.text在对应位置添文字说明来生成相应的数字标签，而for循环也保证了每一个点都有标签。
其中，a, b+0.05表示在每一点对应x值、y值上方0.05处标注文字说明，'%.0f' % b,代表标注的文字，
即每个柱子对应的y值， ha='center', va= 'bottom'代表horizontalalignment（水平对齐）、
verticalalignment（垂直对齐）的方式，fontsize则是文字大小。
'''

#设置图例参数
ax1.legend(loc='best', title='legend',fontsize='medium', frameon=True, edgecolor='blue', facecolor='blue')
'''
plt.legend()函数说明：
位置：loc (可选参数 best, upper, right, upper left, lower left, lower right, right, center left,
center right, lower center, upper center, center)
图例标题：title
图例字体大小：fontsize （可选参数：xx-small, x-small, small, medium, large, x-large, xx-large）
图例边框：frameon （可选参数：True,Flase）
图例边框颜色：edgecolor
图例背景颜色：facecolor
位置：loc,可选一下参数

'''
#指定位置显示文字
ax1.text(2.8, 7, r'y=x*3')
#添加注解
ax1.annotate('important point', xy=(2,6), xytext=(3,1.5), arrowprops = dict(facecolor = 'black', shrink=0.05))
#设置网格参数
ax1.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--', linewidth=2 )
'''
#在当前窗口添加一个子图
axes1 = plt.axes([.2,.3,.1,.1], facecolor='y') #四个参数的话，前两个指的是相对于坐标原点的位置，后两个指的是坐标轴的长/宽度
axes1.plot(x,y)
'''

#保存图片
plt.savefig('test.jpg', dpi=100, bbox_inches='tight')
plt.show() #显示窗口和子图
