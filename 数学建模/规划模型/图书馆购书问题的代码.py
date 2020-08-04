import numpy as np
import math
from scipy.optimize import minimize
import warnings
warnings.filterwarnings("ignore")
A = np.array([2000.,1400,600,3800,800,900,500,1000,600,500,400,100])  # 各个类别的书想要看的人数
def fun_1(n):
    m = np.array([30.]*12)                   # 每种类型书的平均价格，全都定义为30元
    Aij = np.r_[A,A,A].reshape(3,12)
    a = np.r_[A * 0.8, np.zeros(24,dtype=np.float)].reshape(3, 12)
    q = np.zeros((3, 12),dtype=np.float)
    for j in range(12):
        for i in range(3):
            if i!=0:
                for k in range(i):
                    Aij[i][j] = Aij[i][j]- q[k][j]
                a[i][j] = a[i-1][j]-a[i-1][j]*n[j]/Aij[i-1][j]\
                          -min(n[j]*a[i-1][j]/Aij[i-1][j],a[i-1][j]-n[j]*a[i-1][j]/Aij[i-1][j])
            if  Aij[i][j] <= n[j]:
                q[i][j] = Aij[i][j]
            else:
                q[i][j] = n[j]+min(n[j]*a[i][j]/Aij[i][j],a[i][j]-n[j]*a[i][j]/Aij[i][j])
    z1 = 0
    z2 = 0
    for j in range(12):
        z1 += m[j]*n[j]
        z2 += q.sum(axis=0)[j]/A[j]
    return [z1,z2/12]

def fun_2(n):
    # 定义功效函数，功效函数越大越好
    h1 = (fun_1(A)[0]-fun_1(n)[0])/fun_1(A)[0]     # 定义min学校购书费用的功效函数
    h2 = fun_1(n)[1]                               # 定义max学生满意度比例
    return -math.sqrt(h1*h2)

if __name__ == '__main__':
    bounds = tuple(zip([0]*12,[2000.,1400,600,3800,800,900,500,1000,600,500,400,100]))   # 边界条件
    n0 = A/100                # 定义初值条件，各个比例的的人数除100
    res = minimize(fun_2, n0, bounds=bounds)
    print("解为",res.x)
    print("功效函数值",-res.fun)
    print("学校购书的功效系数",(fun_1(A)[0] - fun_1(res.x)[0]) / fun_1(A)[0])
    print("学生满意度的功效系数",fun_1(res.x)[1])