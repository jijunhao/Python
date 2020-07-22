"""
编写一个函数，调用函数返回四位不含0的随机数.
"""

import random
def random_number(figure):
    num = 0
    for i in range(1,figure+1):
        num = num*10 + random.randint(1,9)
    return num
if __name__ == '__main__':
    print(random_number(4))
