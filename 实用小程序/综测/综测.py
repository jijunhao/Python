import numpy as np
score = []
degree1 = [1,4,5,4,3,3,1,5,2,3,3,3]
degree1_1 = [1,4,5,4,3,3,1,5,2,3,3,3]
degree2 = [3,3,4]
degree2_2 = [3,3,4]
print('必修，大二下挂科的输入真实成绩')
strset1 = ['大学体育3','概率论与数理统计Ⅰ','数据结构与算法Ⅰ',
          '数据库原理与技术','离散数学II','Python数据分析',
          '大学体育4','数值计算方法','统计学原理','数学建模',
          '最优化方法','数据科学导引']
strset2 = ['运筹学','数据采集与清洗','计算机网络原理']
for i in range(len(strset1)):
    score.append(float(input("请输入"+strset1[i]+'成绩：')))
    if i<6 and score[-1]<60 :
        degree1_1[i]=0
print('选修，没选输入无，数据采集输入等级')
for i in range(len(strset2)):
    string = input("请输入"+strset2[i]+'成绩：')
    if string == '无':
        degree2[i] = 0
        degree2_2[i]=0
        score.append(0)
    else:
        if i==1:
            if string=="优":
                score.append(90)
            elif string=="良":
                score.append(80)
            elif string == "中":
                score.append(70)
            elif string == "及格":
                score.append(60)
            else:
                score.append(50)
        else:
            score.append(float(string))
            if score[-1] < 60:
                degree1_1[i] = 0

strset = strset1+strset2
degree = degree1+degree2
degree_ = degree1_1+degree2_2

import numpy as np

for i in range(len(strset)):
    print(strset[i],'\t',degree[i],'\t',score[i])

print('总成绩',sum(np.array(score)*np.array(degree_)))
print('总学分',sum(degree))
print('平均',sum(np.array(score)*np.array(degree_))/sum(degree))