# coding=utf-8 
# @Time :2018/12/14 20:16
"""

Return return everywhere!/到处返回！
具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""


def No1_test3():
    try:
        return 'from_try'
    finally:
        return 'from_finally'
    # 当在 "try...finally" 语句的 try 中执行 return, break
    # 或 continue 后, finally 子句依然会执行.
    # 函数的返回值由最后执行的 return 语句决定.
    # 由于 finally 子句一定会执行
    # 所以 finally 子句中的 return 将始终是最后执行的语句.


print(No1_test3())
