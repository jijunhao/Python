"""
定义一个学生类。
有下面的类属性：①姓名②年龄③成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法：
①获取学生的姓名：get_name() 返回类型:str
②获取学生的年龄：get_age() 返回类型:int
③返回3门科目中最高的分数。get_course() 返回类型:int
"""
class Student:

    def __init__(self,name,age,score):
     self.name=name
     self.age=age
     self.score = score

    def get_name(self):
        return (str(self.name))

    def get_age(self):
        return (int(self.age))

    def get_score(self):
        return int(max(self.score))

if __name__ == '__main__':
    student = Student("阿巴阿巴",21,[1,10,100])
    print(student.get_name(),student.get_age(),student.get_score())
