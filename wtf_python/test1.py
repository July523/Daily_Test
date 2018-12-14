# coding=utf-8
# @Time :2018/12/14 19:31

"""
Section: Strain your brain!/大脑运动!

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""


# No.1 Strings can be tricky sometimes/微妙的字符串


def No1():
    a = 'some_string'
    print(id(a))
    b = id("some" + "_" + "string")
    print(b)


# No1()

def No2():
    a = 'wtf'
    b = 'wtf'
    print(a is b)
    c = "wtf!"
    d = "wtf!"
    print(id(c))
    print(id(d))
    print(c is d)
    m, n = "wtf!", "wtf!"
    print(m is n)
    print('a' * 20 is 'aaaaaaaaaaaaaaaaaaaa')
    print('a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa')


# No2()

"""
    这些行为是由于 Cpython 在编译优化时, 某些情况下会尝试使用已经存在的
不可变对象而不是每次都创建一个新对象. 
    (这种行为被称作字符串的驻留[string interning])
    发生驻留之后, 许多变量可能指向内存中的相同字符串对象. (从而节省内存)
    
    在上面的代码中, 字符串是隐式驻留的. 何时发生隐式驻留则取决于具体的实
现. 这里有一些方法可以用来猜测字符串是否会被驻留:
    所有长度为 0 和长度为 1 的字符串都被驻留.
    字符串在编译时被实现 ('wtf' 将被驻留, 但是 ''.join(['w', 't', 'f'] 将不会被驻留)
    字符串中只包含字母，数字或下划线时将会驻留. 所以 'wtf!' 
由于包含 ! 而未被驻留. 可以在这里找到 CPython 对此规则的实现.
    
    当在同一行将 a 和 b 的值设置为 "wtf!" 的时候, Python 解释器会创建
一个新对象, 然后同时引用第二个变量. 如果你在不同的行上进行赋值操作, 它就不
会“知道”已经有一个 wtf！ 对象 (因为 "wtf!" 不是按照上面提到的方式被隐式驻
留的). 它是一种编译器优化, 特别适用于交互式环境.
    
    常量折叠(constant folding) 是 Python 中的一种 窥孔优化
(peephole optimization) 技术. 这意味着在编译时表达式 'a'*20 
会被替换为 'aaaaaaaaaaaaaaaaaaaa' 以减少运行时的时钟周期. 只有
长度小于 20 的字符串才会发生常量折叠. (为啥? 想象一下由于表达式 
'a'*10**10 而生成的 .pyc 文件的大小).
"""
