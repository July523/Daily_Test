# coding=GBK
import jieba
import pandas as pd
import re
import matplotlib.pyplot as plt
import pylab as mpl
from wordcloud import WordCloud

mpl.rcParams['font.sans-serif'] = ['simHei']
mpl.rcParams['axes.unicode_minus'] = False


def atoi(s):
    s = s[::-1]
    num = 0
    for s, v in enumerate(s):
        for j in range(0, 10):
            if v == str(j):
                num += j * (10 ** s)
    return num


df = pd.read_csv('lagou.csv', encoding='gbk')
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
    t3 = (t2 + t1) / 2
    avg_salary.append(t3)

# 月薪

df['月工资'] = avg_salary

# 将学历不限的职位要求认定为最低学历:大专
df['学历要求'] = df['学历要求'].replace('不限', '大专')


# 绘制频率直方图并保存
def draw_salary():
    plt.hist(df['月工资'])
    plt.xlabel(u'工资 (千元)', fontproperties='SimHei')
    plt.ylabel(u'频数', fontproperties='SimHei')
    plt.title(u"工资直方图", fontproperties='SimHei')
    plt.savefig('薪资.jpg')
    plt.show()


def education_requirements_histogram():
    dict = {}
    for value in df['学历要求']:
        if value not in dict.keys():
            dict[value] = 0
        else:
            dict[value] += 1
    index = list(dict.keys())
    print(index)
    num = []
    for value in index:
        num.append(dict[value])
    print(num)
    plt.bar(x=index, height=num, width=0.5)
    plt.show()


# education_requirements_histogram()
# draw_salary()


def company_distribution_pie_chart():
    count = df['区域'].value_counts()
    plt.pie(count, labels=count.keys(), labeldistance=1.4, autopct='%2.1f%%')
    plt.axis('equal')  # 使饼图为正圆形
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
    plt.savefig('pie_chart.jpg')
    plt.show()


# company_distribution_pie_chart()
def pictures_of_benefits():
    # 绘制词云,将职位福利中的字符串汇总
    text = ''
    for line in df['职位福利']:
        text += line
        # 使用jieba模块将字符串分割为单词列表
    cut_text = ' '.join(jieba.cut(text))
    color_mask = plt.imread('test.jpg')  # 设置背景图
    cloud = WordCloud(
        background_color='white',
        # 对中文操作必须指明字体
        font_path='simHei.ttf',
        mask=color_mask,
        max_words=1000,
        max_font_size=100
    ).generate(cut_text)

    # 保存词云图片
    cloud.to_file('word_cloud.jpg')
    plt.imshow(cloud)
    plt.axis('off')
    plt.show()


# pictures_of_benefits()
