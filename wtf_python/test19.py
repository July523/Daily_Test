# coding=utf-8 
# @Time :2018/12/26 10:52

"""Teleportation/空间移动 *"""

import numpy as np


def energy_send(x):
    # 初始化一个numpy数组
    np.array([float(x)])


def energe_receive():
    # 返回一个空的numpy数组
    return np.empty((), dtype=np.float).tolist()


energy_send(123.456)
k = energe_receive()
print(k)

'''
注意在 energy_send 函数中创建的 numpy 数组并没有返回, 因此内存空间被释放并可以被重新分配.
numpy.empty() 直接返回下一段空闲内存，而不重新初始化. 而这个内存点恰好就是刚刚释放的那个
(通常情况下, 并不绝对).
'''