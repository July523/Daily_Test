# coding=utf-8 
# @Time :2019/1/3 21:39

# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# ! python3
import cv2
import numpy as np
import pandas as pd

img1 = cv2.imread('Z1.jpg')
img2 = cv2.imread('Z2.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# ====使用numpy的数组矩阵合并concatenate======

image = np.concatenate((gray1, gray2))  # 纵向连接=np.vstack((gray1, gray2))
# 横向连接image = np.concatenate([gray1, gray2], axis=1)

# ====使用pandas数据集处理的连接concat========

df1 = pd.DataFrame(gray1)

df2 = pd.DataFrame(gray2)  # ndarray to dataframe
df = pd.concat([df1, df2])
# 纵向连接,横向连接=pd.concat([df1, df2], axis=1)

image = np.array(df)  # dataframe to ndarray

# =============

cv2.imshow('image', image)