import pandas as pd
df = pd.read_excel("data.xlsx")
Q1=[]
Q2=[]
Q3=[]
Q4=[]
Q5=[]
Q6=[]
Q7=[]
Q8=[]
Q9=[]
Q = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9]
list = [1719.81,1789.42,1859.03,1928.63,1998.24,2067.85,2137.45,2207.06,2276.67]  #根据实际情况选的阈值
for i in range(0,9):
    for j in range(0,25):
        if (list[i] >= df['figure'][j] and list[i] <= df['figure'][j+1]) or\
        (list[i] <= df['figure'][j] and list[i] >= df['figure'][j+1]):
            q = j + 1 + (list[i] - df['figure'][j])/(df['figure'][j+1] - df['figure'][j])
            Q[i].append(q)
    print('时刻序列%d为: ' % (i+1))
    print(Q[i])

import numpy as np
import matplotlib.pyplot as plt

def GM11(x,n):                                   # x：原始序列，L * 1 维列向量，numpy对象。
    a = x[:len(x) - 1].reshape((len(x) - 1,1))   # 级比检验的分子序列
    Y = x[1:].reshape((len(x) - 1,1))           # 级比检验的分母序列，也是后面要用到的常数项向量
    x1 = x.cumsum()                             # 一次累加
    print('累加序列：',x1)
    z1 = (x1[:len(x1) - 1] + x1[1:])/2.0  # 紧邻均值
    z1 = z1.reshape((len(z1),1))          # 把行向量转为列向量
    B = np.append(-z1,np.ones_like(z1),axis=1)  # 在参数一（数组）后面按列添加参数二,L-1 *2 维，
                                                # L表示原始序列的长度
# a为发展系数 b为灰色作用量
    [[a],[b]] = np.dot(np.dot(np.linalg.inv(np.dot(B.T, B)), B.T), Y)  # 最小二乘法计算参数,得到的是 2 * 1 向量
    print('系数：',[[a],[b]])
    predict_cum=[]   # 对应累加序列的预测序列
    for k in range(0,x.shape[0]):
        pred_cum = (x[0]-b/a)*np.exp(-a*k)+b/a    # 计算一次累加的预测值
        predict_cum.append(pred_cum)
    predict=[]     # 对应原始序列的预测序列
    predict.append(predict_cum[0])   # 原始序列预测值的第一个等于累加序列预测值的第一个
    for k in range(1,x.shape[0]):   # 累减还原原始序列
        predict.append(predict_cum[k]-predict_cum[k-1])
    print("拟合序列",predict)
    predict1=[]
    for i in range(x.shape[0],x.shape[0]+n):
        pred_cum = (x[0]-b/a)*np.exp(-a*i)+b/a
        predict_cum.append(pred_cum)
        predict1.append(predict_cum[i]-predict_cum[i-1])
    print("预测序列:",predict1)
GM11(np.array(Q[3]),20)