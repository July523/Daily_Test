# coding=utf-8
import cv2


def read_pic():
    img = cv2.imread("test.jpg")

    cv2.imshow("Demo", img)
    # 等待显示
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 写入图像
    cv2.imwrite("test_yyy.jpg", img)


def pixel_processing_read():
    img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
    test = img[88, 142]
    print(test)
    img[88, 142] = [255, 255, 255]
    print(test)
    # 分别获取BGR通道像素
    blue = img[88, 142, 0]
    print(blue)
    green = img[88, 142, 1]
    print(green)
    red = img[88, 142, 2]
    print(red)

    cv2.imshow("Demo", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# pixel_processing_read()

def pixel_processing_change():
    img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
    # 该区域设置为白色
    img[100:200, 150:250] = [255, 255, 255]

    cv2.imshow("Demo", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


pixel_processing_change()
