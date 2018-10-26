# coding=utf-8


import pandas as pd
import re
import matplotlib.pyplot as plt


def atoi(s):
    s = s[::-1]
    num = 0
    for i, v in enumerate(s):
        for j in range(0, 10):
            if v == str(j):
                num += j * (10 ** i)
    return num


df = pd.read_csv('lagou.csv', encoding='utf-8')
# 数据清洗,剔除实习岗位
df.drop(df[df['职位名称'].str.contains('实习')].index, inplace=True)
# print(df.describe())
# 由于CSV文件内的数据是字符串形式,先用正则表达式将字符串转化为列表,再取区间的均值
pattern = 'd+'
df['work_year'] = df['工作经验'].str.findall(pattern)
# 数据处理后的工作年限
avg_work_year = []
# 工作年限
for i in df['work_year']:
    # 如果工作经验为'不限'或'应届毕业生',那么匹配值为空,工作年限为0
    if len(i) == 0:
        avg_work_year.append(0)
        # 如果匹配值为一个数值,那么返回该数值
    elif len(i) == 1:
        avg_work_year.append(int(''.join(i)))
        # 如果匹配值为一个区间,那么取平均值
    else:
        num_list = [int(j) for j in i]
        avg_year = sum(num_list) / 2
        avg_work_year.append(avg_year)
df['工作经验'] = avg_work_year

# 将字符串转化为列表,再取区间的前25%，比较贴近现实
sa1 = []
sa2 = []
sa3 = []
sa4 = []
avg_salary = []
t = df['工资']
t2 = t.tolist()
for i in range(len(t2)):
    k1 = re.findall(r"(.+?)k-", t2[i])
    k2 = re.findall(r"-(.+?)k", t2[i])
    sa1.append(k1)
    sa2.append(k2)

for i in range(len(sa1)):
    sa1[i] = ''.join(sa1[i])
    sa2[i] = ''.join(sa2[i])
for i in range(len(sa1)):
    t1 = atoi(sa1[i])
    t2 = atoi(sa2[i])
    sa3.append(t1)
    sa4.append(t2)
    t3 = t2 - t1
    avg_salary.append(t3)

# 月薪

df['月工资'] = avg_salary

# 将学历不限的职位要求认定为最低学历:大专
df['学历要求'] = df['学历要求'].replace('不限', '大专')

# 绘制频率直方图并保存
plt.hist(df['月工资'])
plt.xlabel(u'工资 (千元)', fontproperties='SimHei')
plt.ylabel(u'频数', fontproperties='SimHei')
plt.title(u"工资直方图", fontproperties='SimHei')
plt.savefig('薪资.jpg')
# plt.show()
