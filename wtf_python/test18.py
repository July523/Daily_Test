# coding=utf-8 
# @Time :2018/12/23 13:14

"""
具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84
"""

'''From filled to None in one instruction.../从有到无...'''

some_list = [1, 2, 3]
some_dict = {
    "key_1": 1,
    "key_2": 2,
    "key_3": 3
}

some_list = some_list.append(4)
some_dict = some_dict.update({"key_4": 4})

print(some_list)  # None
print(some_dict)  # None

'''
大多数修改序列/映射对象的方法
比如 list.append, dict.update, list.sort 等等. 
都是原地修改对象并返回 None. 这样做的理由是, 如果操作
可以原地完成, 就可以避免创建对象的副本来提高性能.
'''


'''Subclass relationships/子类关系'''

from collections import Hashable
print(issubclass(list, object))  # True
print(issubclass(object, Hashable))  # True
print(issubclass(list, Hashable))  # False

'''
Python 中的子类关系并不必须是传递的. 任何人都可以在元类中随意定义 __subclasscheck__.
当 issubclass(cls, Hashable) 被调用时, 它只是在 cls 中寻找 "__hash__" 方法或继承自"__hash__"的方法.
由于 object is 可散列的(hashable), 但是 list 是不可散列的, 所以它打破了这种传递关系.
'''