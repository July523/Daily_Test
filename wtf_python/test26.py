# coding=utf-8 
# @Time :2019/2/9 19:38

#  Inpinity/无限

"""英文拼写是有意的, 请不要为此提交补丁.
(译: 这里是为了突出 Python 中无限的定义与Pi有关,
所以将两个单词拼接了.)"""

infinity = float('infinity')
print(hash(infinity))

print(hash(float('-inf')))


# =========================================

# Mangling time!/修饰时间!

class Yo(object):
    def __init__(self):
        self.__honey = True
        self.bitch = True


print(Yo().bitch)
# print(Yo().__honey)
# AttributeError: 'Yo' object has no attribute '__honey'
print(Yo()._Yo__honey)


"""名字修饰 用于避免不同命名空间之间名称冲突.
   在 Python 中, 解释器会通过给类中以 __ (双下划线)开头且结尾最
多只有一个下划线的类成员名称加上_NameOfTheClass 来修饰(mangles)
名称.
   所以, 要访问 __honey 对象,我们需要加上 _Yo 以防止与其他类中
定义的相同名称的属性发生冲突."""
