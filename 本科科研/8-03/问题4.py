"""
利用高斯消元法，求解方程组的解。
   方程组如下：
   6x1+15x2+55x3=152.6
   15x1+55x2+225x3=585.6
   55x1+225x2+979x3=2488.8
"""
import numpy as np
def gauss(a,b):
    # 高斯消元法
    m = a.shape[0]
    n = a.shape[1]
    # 消元过程
    for k in range(n-1):
        for i in range(k+1,n):
            l = a[i][k] / a[k][k]   # 计算消元比例
            for j in range(k+1,m):
                a[i][j] = a[i][j] - l * a[k][j]
            b[i] = b[i] - l * b[k]
    # 回代过程
    x = np.zeros(n)
    x[n-1] = b[n-1] / a[n-1][n- 1]
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            b[i] = b[i] - a[i][j] * x[j]
        x[i] = b[i] / a[i][i]
    return x

if __name__ == '__main__':
    A = np.array([[6., 15, 55],
                  [15, 55, 225],
                  [55, 225, 979]])
    b = np.array([152.6, 585.6, 2488.8])
    print(np.linalg.solve(A,b))
    print(gauss(A,b))
