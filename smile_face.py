import cv2

img = cv2.imread('E:\\pycharm\\coding\\facial\\pei_smile.png', 1)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#将图片转化成灰度

face_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
face_cascade.load("E:\\pycharm\\coding\\facial\haarcascade_eye.xml")

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.namedWindow('img',0)
cv2.resizeWindow('img',800,800)
cv2.imshow('img', img)
cv2.waitKey()
