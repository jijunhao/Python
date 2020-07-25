"""
提示用户输入5个整数，依次存入到列表中,并且按照从大到小的顺序依次输出到终端上

"""

def sort_number(sum):
    print('请输入%d个整数: ' % sum)
    num_list = []
    for i in range(sum):
        num = int(input())
        num_list.append(num)
    num_list.sort(reverse=True)        # 降序排列
    for i in num_list:
        print(i)

if __name__ == '__main__':
    sort_number(5)