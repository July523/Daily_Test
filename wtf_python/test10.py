# coding=utf-8 
# @Time :2018/12/16 20:41
"""

is not ... is not is (not ...)/is not ... 不是 is (not ...)

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""

a1 = 'something' is not None
a2 = 'something' is (not None)

print(a1)
print(a2)

"""
is not 是个单独的二元运算符, 与分别使用 is 和 not 不同.
如果操作符两侧的变量指向同一个对象, 则 is not 的结果为 False, 
否则结果为 True.
"""