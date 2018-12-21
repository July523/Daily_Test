# coding=utf-8 
# @Time :2018/12/21 15:57

"""
The disappearing variable from outer scope/消失的外部变量

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84
"""

e = 7
try:
    raise Exception()
except Exception as e:
    pass

# print(e)  # NameError: name 'e' is not defined

# 当使用 as 为目标分配异常的时候, 将在except子句的末尾清除该异常.

""" except E as N:
        foo
    会被翻译为:
    
    except E as N:
    try:
        foo
    finally:
        del N
"""


# 子句在 Python 中并没有独立的作用域. 而对于有独立的内部作用域的函数来说情况就不一样了
def f(x):
    del (x)
    print(x)


x = 5
y = [5, 4, 3]
# print(f(x))
# print(f(y))
print(x)
print(y)

# 在 Python 2.x 中, Exception() 实例被赋值给了变量 e,
# 所以当你尝试打印结果的时候, 它的输出为空.（译: 正常的Exception实例打印出来就是空）