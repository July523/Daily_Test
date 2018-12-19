# coding=utf-8 
# @Time :2018/12/18 21:29
"""
Class attributes and instance attributes/类属性和实例属性

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""


class A:
    x = 1


class B(A):
    pass


class C(A):
    pass


# 类变量和实例变量在内部是通过类对象的字典来处理
# (译: 就是 __dict__ 属性). 如果在当前类的字典中找不到的话
# 就去它的父类中寻找.


print(A.x, B.x, C.x)
B.x = 2
print(A.x, B.x, C.x)
A.x = 3
print(A.x, B.x, C.x)

a = A()
print(a.x, A.x)
a.x += 1
print(a.x, A.x)


class SomeClass:
    some_var = 15
    some_list = [5]
    another_list = [5]

    def __init__(self, m):
        self.some_var = m + 1
        self.some_list = self.some_list + [m]
        self.another_list += [m]


some_obj = SomeClass(420)
print(some_obj.some_list)
print(some_obj.another_list)

another_obj = SomeClass(111)
print(another_obj.some_list)
print(another_obj.another_list)
print(another_obj.another_list is SomeClass.another_list)
print(another_obj.another_list is some_obj.another_list)
print(some_obj.another_list)

# += 运算符会在原地修改可变对象, 而不是创建新对象. 因此, 修改一个实例的属性会影响其他实例和类属性.


"""
yielding None/生成 None
"""
some_iterable = ('a', 'b')


def some_func(val):
    return "something"


print([n for n in some_iterable])
print([(yield x) for x in some_iterable])
print(list([(yield x) for x in some_iterable]))
print(list((yield x) for x in some_iterable))
print(list(some_func((yield x)) for x in some_iterable))