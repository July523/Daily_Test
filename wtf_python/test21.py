# coding=utf-8 
# @Time :2018/12/30 15:47

"""Deleting a list item while iterating/迭代列表时删除元素"""

list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]

for idx, item in enumerate(list_1):
    del item

for idx, item in enumerate(list_2):
    list_2.remove(item)

for idx, item in enumerate(list_3[:]):
    list_3.remove(item)

for idx, item in enumerate(list_4):
    list_4.pop(idx)

print(list_1, list_2, list_3, list_4)

# 在迭代时修改对象是一个很愚蠢的主意
# 正确的做法是迭代对象的副本, list_3[:] 就是这么做的.

some_list = [1, 2, 3, 4]
print(id(some_list))
print(id(some_list[:]))  # 注意python为切片列表创建了新对象.

"""
del var_name 只是从本地或全局命名空间中删除了 var_name (这就是为什么 list_1 没有受到影响).
remove 会删除第一个匹配到的指定值, 而不是特定的索引, 如果找不到值则抛出 ValueError 异常.
pop 则会删除指定索引处的元素并返回它, 如果指定了无效的索引则抛出 IndexError 异常.
"""