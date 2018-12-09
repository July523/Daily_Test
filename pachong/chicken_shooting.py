# coding=utf-8 
# @Time :2018/12/8 20:27

"""
serial_number：         游戏场次编号
knockout_number：  本场淘汰人数
assist_number：        助攻数
save_number：          救起队友人数
precision：                 射击精度
hit_the_target：         命中
exact_strike：             精准打击
marching_course：     行进历程（m）
material_collection：  材料已收集
material-using：         使用材料
afford_damage：        承受伤害
cause_damage：         玩家伤害
building-damage：     建筑伤害
total_score：               总分
total_experience：      总经验
teams_number：        参赛情况（1人为Solo，两人为Double，4人为team，3人参赛自动填充为4人）
match_time：             游戏时间
competitor_name：   该条记录的所有人

具体细节参考：
https://mp.weixin.qq.com/s?__biz=MjM5MjAwODM4MA
==&mid=2650710107&idx=1&sn=4e179691392664f1cfaf0
bca7c3c072c&chksm=bea6d18889d1589e3399757347e2cb
102f9f249e543238a6f506fda47b208db570240c145230
&mpshare=1&scene=23&srcid=1209SMq0x4ctcKI5LQ2nwhF9#rd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 数据的简单处理
Fortnite_data = pd.read_csv('Fortnite_data.csv')
# 　print(Fortnite_data.head())

# 查看数据类型和数据有无缺失
# print(Fortnite_data.info())

# 查看一下有无重复数据
# print(Fortnite_data[Fortnite_data.duplicated()])

# 查看数据的描述统计
# m = Fortnite_data.describe()
# print(m)

# 发现有一个一场淘汰15人的数据，可能有误，单独输出该条数据进行查看：
# k = Fortnite_data[Fortnite_data['knockout_number'] == 15]
# print(k)

# 接下来开始清理数据
# 复制一个备用df
Fortnite_clean = Fortnite_data.copy()
# 所有的连字符都用下划线表示
Fortnite_clean.columns = [c.replace('-', '_') for c in Fortnite_clean.columns]
Fortnite_clean.columns = [c.replace(' ', '_') for c in Fortnite_clean.columns]
# 大写转化成小写
Fortnite_clean.columns = [c.replace('T', 't') for c in Fortnite_clean.columns]

# 最后一列是提供数据的人，并不是竞争者姓名
Fortnite_clean.rename(columns={'competitor_name': 'data_sources'}, inplace=True)

# team-number并不应该是整型（int），因为不应该用数字表示，而是一个分类变量
# 将team-number中的数值1,2,4转换为对应的队伍人数名称
Fortnite_clean['teams_number'] = \
    Fortnite_clean['teams_number'].map({1: 'Solo', 2: 'Double', 4: 'Team'})

# 将总分和总经验中的NaN全部替换成0
Fortnite_clean['total_score'].fillna(0, inplace=True)
Fortnite_clean['total_experience'].fillna(0, inplace=True)

# 用.astype将这两列转化成整数形式
Fortnite_clean.total_score = Fortnite_clean.total_score.astype(int)
Fortnite_clean.total_experience = Fortnite_clean.total_experience.astype(int)

# 将整数转化成字符串
Fortnite_clean.serial_number = Fortnite_clean.serial_number.astype(str)
# 补上前面少的0
Fortnite_clean.serial_number = Fortnite_clean.serial_number.str.pad(4, side='left', fillchar='0')

# 列出年月日列和小时列
Fortnite_clean['match_day'] = pd.to_datetime(Fortnite_clean['match_time'])
Fortnite_clean['match_hour'] = pd.to_datetime(Fortnite_clean['match_time'])
# 将这两列转化成为想要的形式
Fortnite_clean['match_hour'] = Fortnite_clean['match_hour'].dt.time
Fortnite_clean['match_day'] = Fortnite_clean['match_day'].dt.date
# 删除多余的match_time列
Fortnite_clean = Fortnite_clean.drop('match_time', axis=1)

# 接下来对数据进行一个简单的分析
# 选出获得第一名的数据
one_place = Fortnite_clean[Fortnite_clean['grade'] == 1]

# 筛选出造成伤害高于606的数据
damage_high = Fortnite_clean[Fortnite_clean['cause_damage'] >= 606]
damage_high_mean = Fortnite_clean[Fortnite_clean['cause_damage'] >= 606].grade.mean()

damage_afford_high_mean = Fortnite_clean[Fortnite_clean['afford_damage'] >= 451].grade.mean()
damage_build_high_mean = Fortnite_clean[Fortnite_clean['building_damage'] >= 20000].grade.mean()

# 接下来研究排名第（吃）一（鸡）的最相关条件是什么？
Fortnite_one = Fortnite_clean[Fortnite_clean['grade'] <= 5]
# 来筛除掉肯定不太相关的数据
Fortnite_one.drop(['data_sources', 'match_hour', 'match_day', 'teams_number', 'total_experience', 'total_score',
                   'marching_course', 'save_number', 'assist_number', 'afford_damage',
                   'serial_number', 'building_damage'], axis=1, inplace=True)
Fortnite_one.grade.value_counts()
Fortnite_one['grade'] = Fortnite_one['grade'].map({1: 100, 2: 80, 3: 60, 4: 40, 5: 20})

list1 = ['knockout_number', 'precision', 'hit_the_target', 'exact_strike', 'material_collection',
         'material_using', 'cause_damage', 'building_damage', 'grade']

dfData = Fortnite_one.corr()
plt.subplots(figsize=(8, 8))  # 设置画面大小
sns.heatmap(dfData, annot=True, vmax=1, square=True, cmap="Blues")
plt.show()
