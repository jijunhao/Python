import numpy as np
def istype(a):
    """
    判断模糊矩阵a的类型
    """
    a = np.array(a)
    s = np.eye(a.shape[0], a.shape[1])
    if (a >= s).all() and (a.T == a).all():
        return "模糊自反矩阵、模糊对称矩阵"
    elif (a >= s).all():
        return "模糊自反矩阵"
    elif (a.T == a).all():
        return "模糊对称矩阵"
    elif (hecheng(a, a) <= a).all():
        return "模糊传递矩阵"
    else:
        return "一般模糊矩阵"


def isequal(a, b):
    """
    判断模糊矩阵a,b是否相等
    """
    a, b = np.array(a), np.array(b)
    if (a == b).all():
        print("相等")
    else:
        print("不相等")


def islower(a, b):
    """
    判断模糊矩阵a是否小于等于模糊矩阵b
    """
    a, b = np.array(a), np.array(b)
    if (a <= b).all():
        return "小于等于"
    else:
        return "不是小于等于"


def bing(a, b):
    """
    求模糊矩阵a和模糊矩阵b的并
    """
    a, b = np.array(a), np.array(b)
    c = np.fmax(a, b)  # 元素级的最大值计算
    return c


def jiao(a, b):
    """
    求模糊矩阵a和模糊矩阵b的交
    """
    a, b = np.array(a), np.array(b)
    c = np.fmin(a, b)  # 元素级的最小值计算
    return c


def bu(a):
    """
    求模糊矩阵a的补
    """
    a = np.array(a)
    c = 1 - a  # 元素级的计算
    return c


def hecheng(a, b):
    """
    求模糊是矩阵a和模糊矩阵b的合成
    """
    a, b = np.array(a), np.array(b)
    if a.shape[1] == b.shape[0]:
        c = np.zeros_like(a.dot(b))
        for i in range(a.shape[0]):  # 遍历a的行元素
            for j in range(b.shape[1]):  # 遍历b的列元素
                empty = []
                for k in range(a.shape[1]):
                    empty.append(min(a[i, k], b[k, j]))  # 行列元素比小
                c[i, j] = max(empty)  # 比小结果取大
        return c
    else:
        print("输入矩阵不能做合成运算！\n请检查矩阵的维度！")


def bibao(a):
    """
    求模糊矩阵a的闭包
    """
    a = np.array(a)
    if a.shape[0] == a.shape[1]:
        c = a
        while True:
            m = c
            c = hecheng(hecheng(a, c), hecheng(a, c))
            if (c == m).all():
                return c
                break
            else:
                continue
    else:
        print("输入矩阵不能做闭包运算！\n请检查矩阵的维度！")

if __name__ == "__main__":
    r = [
        [1, 0.54, 0.62, 0.63, 0.24],
        [0.54, 1, 0.55, 0.7, 0.53],
        [0.62, 0.55, 1, 0.56, 0.37],
        [0.63, 0.7, 0.56, 1, 0.38],
        [0.24, 0.53, 0.37, 0.38, 1]
    ]
    print("模糊矩阵\n", np.array(r))
    print("模糊传递闭包\n", bibao(r))