# coding=utf-8 
# @Time :2018/12/27 10:53

"""Modifying a dictionary while iterating over it"""

x = {0: None}

for i in x:
    del x[i]
    x[i + 1] = None
    print(i)

"""
Python不支持对字典进行迭代的同时修改它.因为字典的初始最小值是8, 扩容会导致散列表地址发生变化而中断循环

在不同的Python实现中删除键的处理方式以及调整大小的时间可能会有所不同.
(译: 就是说什么时候扩容在不同版本中可能是不同的, 在3.6及3.7的版本中到5就会自动扩容了.
以后也有可能再次发生变化. 顺带一提,后面两次扩容会扩展为32和256. 8->32->256)
"""

"""Stubborn del operator/坚强的 del"""


class SomeClass:
    def __del__(self):
        print("Deleted!")


x = SomeClass()
y = x

del x  # print None
del y  # print Deleted!

x1 = SomeClass
y1 = x1
del x1
print(y1)  # 检查一下y是否存在-->是存在的

del y1
globals()

"""
del x 并不会立刻调用 x.__del__().
每当遇到 del x, Python 会将 x 的引用数减1, 当 x 的引用数减到0时就会调用 x.__del__().

在第二个例子中, y1.__del__() 之所以未被调用, 是因为前一条语句 (>>> y1) 对同一对象创建了另一个引用, 
从而防止在执行 del y1 后对象的引用数变为0.
调用 globals 导致引用被销毁, 因此我们可以看到 "Deleted!" 终于被输出了.
"""
