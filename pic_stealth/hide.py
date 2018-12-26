# coding=utf-8 
# @Time :2018/12/26 17:22

"""Python实现图像信息隐藏"""

import cv2
import numpy as np

source = cv2.imread('tree.jpg')
h, w = source.shape[:2]
message = 'Hello World!'
x, y = (180, 250)
color = [255, 255, 255]
cv2.putText(source, message, (x, y), cv2.QT_FONT_NORMAL, 3, color, thickness=5)
cv2.imwrite('new_tree.png', source)

source1 = cv2.imread('ship.jpg')
for i in range(h):
    for j in range(w):
        # 把整幅图的B通道全设置为偶数
        if source1[i, j, 0] % 2 == 1:
            source1[i, j, 0] -= 1
for i in range(h):
    for j in range(w):
        # 找出有文字的位置
        if list(source[i, j]) == color:
            source1[i, j, 0] += 1
cv2.imwrite('hide.png', source1)

img = cv2.imread('hide.png')
h, w = img.shape[:2]
# 新建一张图用来放解出来的信息
info = np.zeros((h, w, 3), np.uint8)
for i in range(h):
    for j in range(w):
        # 发现B通道为奇数则为信息的内容
        if img[i, j, 0] % 2 == 1:
            info[i, j, 0] = 255
            info[i, j, 1] = 255
            info[i, j, 2] = 255
cv2.imwrite('info.png', info)
