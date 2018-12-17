# coding=utf-8 
# @Time :2018/12/17 11:12

"""

Backslashes at the end of string/字符串末尾的反斜杠

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""

print("\\ C:\\")
print(r"\ C:")
# print(r"\ C:\") 这是一个错误的表示

# 在以 r 开头的原始字符串中, 反斜杠并没有特殊含义.
print(repr(r"wt\"f"))

'''
    解释器所做的只是简单的改变了反斜杠的行为, 因此会直接放行反斜杠
及后一个的字符. 这就是反斜杠在原始字符串末尾不起作用的原因.
'''