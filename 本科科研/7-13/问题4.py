"""
在python3中，编写函数，实现接收一个字符串，分别统计大写字母，小写字母，数字，
其它字符的个数，并以元组的形式返回结果(利用函数判断，循环实现)。
"""

def classify(str):
    capital= 0
    little = 0
    digit = 0
    other = 0
    for i in str:
        if i >= 'A' and i <= 'Z':
            capital = capital + 1
        elif i >= 'a' and i <= 'z':
            little = little + 1
        elif i >= '0' and i <= '9':
            digit = digit + 1
        else:
            other = other + 1
    print((capital,little,digit,other))
if __name__ == '__main__':
    str = input("请输入一个字符串： ")
    classify(str)