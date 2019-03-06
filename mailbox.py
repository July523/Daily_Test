# coding=utf-8
# @Time: 3/6/2019 2:51 PM
"""
    用数字0-11代表12个邮箱的名字。
    situation1表示 dl1 <- dl2 <- dl3 的情况

    situation2表示 dl1 <- dl2 的情况
                      <-dl3
"""

import random


class Solution:
    arr = []
    for i in range(6):
        k = random.randrange(0, 12, 1)
        if k not in arr:
            arr.append(k)

    number = {}

    for i in range(12):
        key = i
        value = 'local'
        number[key] = value

    for i in range(len(arr)):
        key = arr[i]
        value = 'cloud'
        number[key] = value

    b1 = []
    while True:
        k = random.randrange(0, 12, 1)
        if k not in b1:
            b1.append(k)
        else:
            continue
        if len(b1) == 4:
            break
    b2 = []
    while True:
        k = random.randrange(0, 12, 1)
        if (k not in b2) and (k not in b1):
            b2.append(k)
        else:
            continue
        if len(b2) == 4:
            break

    b3 = []
    while True:
        k = random.randrange(0, 12, 1)
        if (k not in b2) and (k not in b1) and (k not in b3):
            b3.append(k)
        else:
            continue
        if len(b3) == 4:
            break

    dl1 = []
    for i in range(4):
        dl1.append(b1[i])
    dl2 = []
    for i in range(4):
        dl2.append(b2[i])
    dl3 = []
    for i in range(4):
        dl3.append(b3[i])

    def situation1(self, num: int):
        if num in self.dl1:
            return ["dl1", "dl2", "dl3", num, self.number[num]]
        elif num in self.dl2:
            return ["dl2", "dl3", num, self.number[num]]
        elif num in self.dl3:
            return ["dl3", num, self.number[num]]

    def situation2(self, num: int):
        if num in self.dl1:
            return ["dl1", "dl2", "dl3", num, self.number[num]]
        elif num in self.dl2:
            return ["dl2", num, self.number[num]]
        elif num in self.dl3:
            return ["dl3", num, self.number[num]]


print(Solution().situation1(0))
