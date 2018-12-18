# coding=utf-8 
# @Time :2018/12/18 11:01

"""
Midnight time doesn't exist?/不存在的午夜?

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""

from datetime import datetime

midnight = datetime(2018, 1, 1, 0, 0)
midnight_time = midnight.time()

noon = datetime(2018, 1, 1, 12, 0)
noon_time = noon.time()

if midnight_time:
    print("Time at midnight is", midnight_time)

if noon_time:
    print("Time at noon is", noon_time)

'''
    在Python 3.5之前, 如果 datetime.time 对象存储的UTC的午夜时间
(译: 就是 00:00), 那么它的布尔值会被认为是 False. 当使用 if obj: 
语句来检查 obj 是否为 null 或者某些“空”值的时候, 很容易出错.
    Python3.6已经修复了这个问题
'''