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
# ������ϴ,�޳�ʵϰ��λ
df.drop(df[df['ְλ����'].str.contains('ʵϰ')].index, inplace=True)
# print(df.describe())
# ����CSV�ļ��ڵ��������ַ�����ʽ,����������ʽ���ַ���ת��Ϊ�б�,��ȡ����ľ�ֵ
pattern = 'd+'
df['work_year'] = df['��������'].str.findall(pattern)
# ���ݴ����Ĺ�������
avg_work_year = []
# ��������
for i in df['work_year']:
    # �����������Ϊ'����'��'Ӧ���ҵ��',��ôƥ��ֵΪ��,��������Ϊ0
    if len(i) == 0:
        avg_work_year.append(0)
        # ���ƥ��ֵΪһ����ֵ,��ô���ظ���ֵ
    elif len(i) == 1:
        avg_work_year.append(int(''.join(i)))
        # ���ƥ��ֵΪһ������,��ôȡƽ��ֵ
    else:
        num_list = [int(j) for j in i]
        avg_year = sum(num_list) / 2
        avg_work_year.append(avg_year)
df['��������'] = avg_work_year

# ���ַ���ת��Ϊ�б�,��ȡ�����ǰ25%���Ƚ�������ʵ
sa1 = []
sa2 = []
sa3 = []
sa4 = []
avg_salary = []
t = df['����']
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

# ��н

df['�¹���'] = avg_salary

# ��ѧ�����޵�ְλҪ���϶�Ϊ���ѧ��:��ר
df['ѧ��Ҫ��'] = df['ѧ��Ҫ��'].replace('����', '��ר')


# ����Ƶ��ֱ��ͼ������
def draw_salary():
    plt.hist(df['�¹���'])
    plt.xlabel(u'���� (ǧԪ)', fontproperties='SimHei')
    plt.ylabel(u'Ƶ��', fontproperties='SimHei')
    plt.title(u"����ֱ��ͼ", fontproperties='SimHei')
    plt.savefig('н��.jpg')
    plt.show()


def education_requirements_histogram():
    dict = {}
    for value in df['ѧ��Ҫ��']:
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
    count = df['����'].value_counts()
    plt.pie(count, labels=count.keys(), labeldistance=1.4, autopct='%2.1f%%')
    plt.axis('equal')  # ʹ��ͼΪ��Բ��
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
    plt.savefig('pie_chart.jpg')
    plt.show()


# company_distribution_pie_chart()
def pictures_of_benefits():
    # ���ƴ���,��ְλ�����е��ַ�������
    text = ''
    for line in df['ְλ����']:
        text += line
        # ʹ��jiebaģ�齫�ַ����ָ�Ϊ�����б�
    cut_text = ' '.join(jieba.cut(text))
    color_mask = plt.imread('test.jpg')  # ���ñ���ͼ
    cloud = WordCloud(
        background_color='white',
        # �����Ĳ�������ָ������
        font_path='simHei.ttf',
        mask=color_mask,
        max_words=1000,
        max_font_size=100
    ).generate(cut_text)

    # �������ͼƬ
    cloud.to_file('word_cloud.jpg')
    plt.imshow(cloud)
    plt.axis('off')
    plt.show()


# pictures_of_benefits()
