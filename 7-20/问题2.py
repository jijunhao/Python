"""
for循环打印99乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(j,i,i*j),end=' ')
    print("")