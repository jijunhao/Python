"""
实现冒泡排序，要求输入任意一组无序数据，通过调用你所编写的函数，可以将数据变为有序
（冒泡排序的工作原理为重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。）
"""
def Bubble_sort(data):
    while 1:
        state = 0          # 是否已经排序结束
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                state = 1
        if not state:
            break
    return data

if __name__ == '__main__':
    data = [9, 3, 8, 7, 6, 5, 1, 2]
    print(Bubble_sort(data))