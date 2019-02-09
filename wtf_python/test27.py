# coding=utf-8 
# @Time :2019/2/9 20:07

# += is faster/更快的 +=

# 用“”"+" 连接三个字符串
import timeit

a = timeit.timeit("s1 = s1 + s2 + s3", setup="s1 = ' ' * 100000; s2 = ' ' * 100000; s3 = ' ' * 100000", number=100)

b = timeit.timeit("s1 += s2 + s3", setup="s1 = ' ' * 100000; s2 = ' ' * 100000; s3 = ' ' * 100000", number=100)

print(a)
print(b)

"""连接两个以上的字符串时 += 比 + 更快, 因为在计算过程中第一个字符串 
(例如, s1 += s2 + s3 中的 s1) 不会被销毁.(译: 就是 += 执行的是追加操作，少了一个销毁新建的动作.)"""


