"""
编写一个numpy 程序来计算数组a 中各个数的出现次数.
"""
import numpy as np
from collections import  Counter
a = np.array([1,1,2,3,3,4,5,6])
print(Counter(a))