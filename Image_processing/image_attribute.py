# coding=utf-8 
# @Time :2018/11/11 19:41
import cv2
import numpy as np

img = cv2.imread("peng_nosmile.png", cv2.IMREAD_UNCHANGED)


# print(img.shape)
# print(img.size)
# print(img.dtype)
# cv2.imshow("Demo", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def region_of_interest():
    # 定义200*100矩阵，3对应BGR
    face = np.ones((200, 100, 3))
    face = img[200:400, 200:300]
    # 显示ROI区域
    face = img[100:300, 150:350]
    img[0:200, 0:200] = face
    cv2.imshow("face", img)
    cv2.imshow("B", b)
    cv2.imshow("G", g)
    cv2.imshow("R", r)
    # 等待显示
    cv2.waitKey(0)
    cv2.destroyAllWindows()


b, g, r = cv2.split(img)
m = cv2.merge([r, g, b])
cv2.imshow("Merge", m)
cv2.waitKey(0)
cv2.destroyAllWindows()