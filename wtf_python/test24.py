# coding=utf-8 
# @Time :2019/1/24 10:09

"""Catching the Exceptions/捕获异常"""

some_list = [1, 2, 3]
try:
    print(some_list[4])
except (IndexError, ValueError):
    print("Caught!")

try:
    # 这里会抛出异常 ``ValueError``
    some_list.remove(4)
except (IndexError, ValueError):
    print("Caught again!")

try:
    some_list.remove(4)
except (IndexError, ValueError) as e:
    print("Caught!!")
    print(e)

# ===============================================


"""The out of scope variable/外部作用域变量"""

a = 1


def some_func():
    return a


"""当你在作用域中对变量进行赋值时, 变量会变成该作用域内的局部变量. 
因此 a 会变成 another_func 函数作用域中的局部变量, 但它在函数
作用域中并没有被初始化, 所以会引发错误."""


# def another_func():
#     a += 1
#     return a

# 想要在 another_func 中修改外部作用域变量 a 的话, 可以使用 global 关键字.
def another_func():
    global a
    a += 1
    return a
