"""
实现插入排序，要求输入任意一组无序数据，通过调用你所编写的函数，可以将数据变为有序
（插入排序的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入)
"""
def InsertSort(data):
    # 插入排序递增
    sort_data = [data[0]]          # 有序表
    for i in range(1, len(data)):
        state = 0                  # 是否为首位元素
        for j in range(len(sort_data)-1, -1, -1):
            if data[i] >= sort_data[j]:
                sort_data.insert(j + 1, data[i])
                state = 1
                break
        if  not state:
            sort_data.insert(0,data[i])

    return sort_data
if __name__ == '__main__':
    data = [9,3,8,7,6,5,1,2]
    print(InsertSort(data))



