"""
编写一个numpy 程序来找出数组a 中等于1 的数的位置
"""
import numpy as np
a = np.array([1,1,2,3,3,4,5,6])
print(np.where(a==1))