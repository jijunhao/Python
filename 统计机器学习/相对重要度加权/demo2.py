import math
import numpy as np
import numpy.matlib as nm
import matplotlib.pyplot as plt

n=100
u = nm.randn(n,1)/4+2
x= nm.randn(n,1)/2+1
w = 2*nm.exp(-8*np.power((x-2),2)+2*np.power((x-1),2))
y = nm.sin(nm.pi*x)/(nm.pi*x)+0.1*nm.randn(n,1)
x2 = np.ones(len(x)).reshape(len(x),1)              # 生成一个维度为（n，1），元素全是1的数组
x= np.c_[x,x2]                                      # x(:,2)=1;加第二行为1
t1= np.multiply(nm.repmat(w,1,2),x)                 # np.multiply为矩阵对应元素相乘
t = np.linalg.inv(x.T*t1)*(x.T*(np.multiply(w,y)))  # np.linalg.inv(.)求逆矩阵
X=nm.linspace(-1,3,100)                             # 生成数据节点
Y= nm.sin(nm.pi*X)/(nm.pi*X)         # 根据节点计算Y
u= np.c_[u,x2]
v = u*t
print(u.shape)
plt.figure()
plt.plot(x[:,0],y,'bo',label='xi,yi')   # 绘制原始数据点
plt.plot(X,Y,'r-',label='f(x)')        # 绘制重要度加权的最小二乘曲线
plt.plot(u[:,0],v,'kx',label='xi1,yi1')   # 绘制最小二乘曲线
plt.legend()         # 显示绘制的legend
plt.show()                # 显示绘制的画布
