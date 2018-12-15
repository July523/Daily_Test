# coding=utf-8 
# @Time :2018/12/15 13:53
"""
For what?/为什么?

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""

some_string = "wtf"
some_dict = {}
for i, some_dict[i] in enumerate(some_string):
    pass

print(some_dict)

"""
Python 语法 中对 for 的定义是:
for_stmt: 'for' exprlist 'in' testlist ':' suite ['else' ':' suite]
其中 exprlist 指分配目标. 这意味着对可迭代对象中的每一项都
会执行类似 {exprlist} = {next_value} 的操作.

在每一次的迭代中, enumerate(some_string) 函数就生成一个
新值 i (计数器增加) 并从 some_string 中获取一个字符. 然后
将字典 some_dict 键 i (刚刚分配的) 的值设为该字符.
"""