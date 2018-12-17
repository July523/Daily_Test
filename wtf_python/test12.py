# coding=utf-8 
# @Time :2018/12/17 11:24

"""
not knot!/别纠结!

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""

x = True
y = False

print(not x == y)

# print(x == not y) 这是一个错误的表达

'''
运算符的优先级会影响表达式的求值顺序, 而在 Python 中 == 运算符的优先级要高于 not 运算符.
所以 not x == y 相当于 not (x == y), 同时等价于 not (True == False), 最后的运算结果就是 True.
之所以 x == not y 会抛一个 SyntaxError 异常, 是因为它会被认为等价于 (x == not) y, 而不是你一开始期望的 x == (not y).
解释器期望 not 标记是 not in 操作符的一部分 (因为 == 和 not in 操作符具有相同的优先级), 
但是它在 not 标记后面找不到 in 标记, 所以会抛出 SyntaxError 异常.
'''