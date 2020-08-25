"""
编写一个numpy 程序找出0 − 100 里所有3, 13, 23 的倍数, 并输出(不能使用循环).
"""
import numpy as np
a = np.arange(0,101)
print(a[(a%3==0) | (a%13==0) | (a%23==0)])
