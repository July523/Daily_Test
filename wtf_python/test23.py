# coding=utf-8 
# @Time :2019/1/23 11:03

""" Beware of default mutable arguments!/当心默认的可变参数!"""


def some_func(default_arg=[]):
    default_arg.append("some_string")
    return default_arg


# print(some_func())
# print(some_func())
# print(some_func([]))
# print(some_func())

"""Python中函数的默认可变参数并不是每次调用该函数时都会被初始化. 
相反, 它们会使用最近分配的值作为默认值. 当我们明确的将 [] 作为参
数传递给 some_func 的时候, 就不会使用 default_arg 的默认值, 
所以函数会返回我们所期望的结果."""

print(some_func.__defaults__)  # 这里会显示函数的默认参数的值
print(some_func())
print(some_func.__defaults__)


""" Same operands, different story!/同人不同命!"""

a = [1, 2, 3, 4]
b = a
a = a + [5, 6, 7, 8]

print(a)
print(b)

a = [1, 2, 3, 4]
b = a
a += [5, 6, 7, 8]

print(a)
print(b)

"""表达式 a = a + [5,6,7,8] 会生成一个新列表, 
并让 a 引用这个新列表, 同时保持 b 不变.
表达式 a += [5,6,7,8] 实际上是使用的是 "extend" 函数,
 所以 a 和 b 仍然指向已被修改的同一列表."""