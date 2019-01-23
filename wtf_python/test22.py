# coding=utf-8 
# @Time :2019/1/23 10:52

"""Loop variables leaking out!/循环变量泄漏!"""

for x in range(7):
    if x == 6:
        print(x, ': for x inside loop')
print(x, ': x in global')

# output:
# 6 : for x inside loop
# 6 : x in global

# 这次我们先初始化x
x = -1
for x in range(7):
    if x == 6:
        print(x, ': for x inside loop')
print(x, ': x in global')

x = 1
print([x for x in range(5)])
print(x, ': x in global')

'''
在 Python 中, for 循环使用所在作用域并在结束后保留定义的循环变量. 
如果我们曾在全局命名空间中定义过循环变量. 在这种情况下, 它会重新绑定现有变量.
'''
