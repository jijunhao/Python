"""
实现用户输入用户名和密码，当用户名为 seven 且密码为 123 时，显示登陆成功，
否则登陆失败，失败时允许重复输入三次
"""
def login_in():
    count = 0
    while count<3:
        user_name = input("请输入用户名: ")
        user_password = input("请输入密码: ")
        if user_name == 'seven' and user_password == '123':
            print('登录成功')
            break
        else:
            print('登录失败,请重新登录')
        count = count + 1
    if count == 3:
        print('您已经失败三次，账号已锁定。')

if __name__ == '__main__':
    login_in()
