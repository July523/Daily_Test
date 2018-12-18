# coding=utf-8 
# @Time :2018/12/18 21:07

"""
What's wrong with booleans?/布尔你咋了?

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""

# 一个简单的例子, 统计下面可迭代对象中的布尔型值的个数和整型值的个数

mixed_list = [False, 1.0, "some_string", 3, True, [], False]
integers_found_so_far = 0
booleans_found_so_far = 0

for item in mixed_list:
    if isinstance(item, int):
        integers_found_so_far += 1
    elif isinstance(item, bool):
        booleans_found_so_far += 1

print(integers_found_so_far, booleans_found_so_far)

another_dict = {True: "JavaScript", 1: "Ruby", 1.0: "Python"}
print(another_dict[True])


some_bool = True
a = "good" * some_bool
some_bool = False
b = "bad" * some_bool

print(a, b)

# 因为布尔值是 int 的子类
print(isinstance(True, int))

# 所以 True 的整数值是 1, 而 False 的整数值是 0.
print(True == 1 == 1.0 and False == 0 == 0.0)