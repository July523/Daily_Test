# coding=utf-8 
# @Time :2019/1/24 11:08

"""Be careful with chained operations/小心链式操作"""

m1 = (False == False) in [False]  # False -> 可以理解
m2 = False == (False in [False])  # False -> 可以理解
m3 = False == False in [False]  # True ->  为毛？

print(m1, m2, m3)

m4 = True is False == False
m5 = False is False is False

print(m4, m5)

m6 = 1 > 0 < 1
m7 = (1 > 0) < 1
m8 = 1 > (0 < 1)

print(m6, m7, m8)

"""形式上, 如果 a, b, c, ..., y, z 是表达式, 
而 op1, op2, ..., opN 是比较运算符, 那么除了
每个表达式最多只出现一次以外 a op1 b op2 c ... y opN z 
就等于 a op1 b and b op2 c and ... y opN z."""

