# coding=utf-8 
# @Time :2018/12/14 20:35

"""
Deep down, we're all the same./本质上,我们都一样.

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""


class WTF:
    pass


print(WTF() == WTF())  # 两个不同的对象应该不相等)
print(WTF() is WTF())

print(hash(WTF()) == hash(WTF()))
print(id(WTF()) == id(WTF()))

"""
    当调用 id 函数时, Python 创建了一个 WTF 类的对象并传给 id 函数.
然后 id 函数获取其id值 (也就是内存地址), 然后丢弃该对象. 该对象就被销毁了.
    当我们连续两次进行这个操作时, Python会将相同的内存地址分配给第二个
对象. 因为 (在CPython中) id 函数使用对象的内存地址作为对象的id值, 
所以两个对象的id值是相同的.
    综上, 对象的id值仅仅在对象的生命周期内唯一. 在对象被销毁之后, 或被
创建之前, 其他对象可以具有相同的id值.
"""


class WTF_2(object):
    def __init__(self):
        print("I")

    def __del__(self):
        print("D")


# 对象销毁的顺序是造成所有不同之处的原因
print(WTF_2() == WTF_2())  # output: I I D D
print(id(WTF_2()) == id(WTF_2()))  # output: I D I D

