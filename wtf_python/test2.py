# coding=utf-8 
# @Time :2018/12/14 19:58

"""
Time for some hash brownies!/是时候来点蛋糕了!

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""


def No1_test2():
    some_dict = {5.5: "Ruby", 5.0: "JavaScript", 5: "Python"}
    print(some_dict[5.0])

    # Python字典通过检查键值是否相等和比较哈希值来确定两个键是否相同.
    print(5 == 5.0)
    print(hash(5) == hash(5.0))


No1_test2()
