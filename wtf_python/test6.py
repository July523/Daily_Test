# coding=utf-8 
# @Time :2018/12/16 13:03

"""
Evaluation time discrepancy/执行时机差异

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""

array = [1, 8, 15]
g = (x for x in array if array.count(x) > 0)
array = [2, 8, 22]
print(list(g))

array_1 = [1, 2, 3, 4]
g1 = (x for x in array_1)
array_1 = [1, 2, 3, 4, 5]

array_2 = [1, 2, 3, 4]
g2 = (x for x in array_2)
array_2[:] = [1, 2, 3, 4, 5]

print(list(g1))
print(list(g2))

"""
    在生成器表达式中, in 子句在声明时执行, 而条件子句则是在运行时执行.

    所以在运行前, array 已经被重新赋值为 [2, 8, 22],因此对于之前的 
1, 8 和 15, 只有 count(8) 的结果是大于 0 的, 所以生成器只会生成 8.
    第二部分中 g1 和 g2 的输出差异则是由于变量 array_1 和 array_2 
被重新赋值的方式导致的.
    在第一种情况下, array_1 被绑定到新对象 [1,2,3,4,5], 因为 in 
子句是在声明时被执行的， 所以它仍然引用旧对象 [1,2,3,4](并没有被销毁).
    在第二种情况下, 对 array_2 的切片赋值将相同的旧对象 [1,2,3,4] 
原地更新为 [1,2,3,4,5]. 因此 g2 和 array_2 仍然引用同一个对象(这个
对象现在已经更新为 [1,2,3,4,5]).

"""
