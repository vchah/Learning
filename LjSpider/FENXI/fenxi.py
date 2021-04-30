"""
Construction -- 建筑样式
Direction -- 朝向
District -- 街道
Floor -- 楼层
Garden -- 小区
Height -- 楼层高
Id -- 房屋ID
Layout -- 户型
Price -- 总价
Region -- 区域
Renovation -- 装修
Size -- 面积
Subway -- 地铁
Taxfree -- 税
UnitPrice -- 单价
"""
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import statsmodels.api as sm
from numpy import corrcoef,array
#from IPython.display import HTML, display
from statsmodels.formula.api import ols

 
import os

datall=pd.read_csv("D:\Code\Python\LianjiaCrawer\LjSpider\FENXI\哈尔滨房价原始数.csv")  #读入清洗过后的数据
print(datall.shape[0])  #样本量

dat0=datall
dat0.describe(include="all").T  #查看数据基本描述p


matplotlib.rcParams['axes.unicode_minus']=False#解决保存图像时负号'-'显示为方块的问题
plt.rcParams['font.sans-serif'] = ['SimHei']#指定默认字体 
 
#因变量直方图
dat0.UnitPrice.hist(bins=20)
#dat0.price.plot(kind="hist",color='lightblue')
plt.xlabel("单位面积房价（万元/平方米）")
plt.ylabel("频数")
print(dat0.UnitPrice.agg(['mean','median','std']))  #查看UnitPrice的均值、中位数和标准差等更多信息
print(dat0.UnitPrice.quantile([0.25,0.5,0.75]))
pd.concat([(dat0[dat0.UnitPrice==min(dat0.UnitPrice)]),(dat0[dat0.UnitPrice==max(dat0.UnitPrice)])])
