# coding=utf-8 
# @Time :2018/12/18 10:53

"""
Half triple-quoted strings/三个引号

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""

print('Good''')
print("Night""")

# 下面的语句会抛出 `SyntaxError` 异常
# print('''Good')
# print("""Night")

# Python 提供隐式的字符串链接
'''
    允许多个相邻的字符串文本(用空格分隔)，可能使用不同的引用约定，它们的
含义与它们的连接相同。因此，"hello" 'world'等于"helloworld"。此特性
可用于减少所需反斜杠的数量，方便地在长行之间分割长字符串，甚至可以向字符串
的部分添加注释
'''

print("good" "python")

'''
    """ 在 Python中也是字符串定界符, Python 解释器在先遇到三个引号的
时候会尝试再寻找三个终止引号作为定界符, 如果不存在则会导致 SyntaxError 异常.
'''