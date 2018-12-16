# coding=utf-8 
# @Time :2018/12/16 13:17

"""
is not what it is!/出人意料的is!

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""

a = 256
b = 256
print(a is b)

c = 257
d = 257
print(c is d)

print([] == [])
print([] is [])

print(id(257))
print(id(c))


"""
is 和 == 的区别

is 运算符检查两个运算对象是否引用自同一对象 (即, 它检查两个预算对象是否相同).
== 运算符比较两个运算对象的值是否相等.因此 is 代表引用相同, == 代表值相等.

    当你启动Python 的时候, -5 到 256 的数值就已经被分配好了. 这些数字
因为经常使用所以适合被提前准备好.
    当前的实现为-5到256之间的所有整数保留一个整数对象数组, 当你创建了一个该
范围内的整数时, 你只需要返回现有对象的引用. 
"""