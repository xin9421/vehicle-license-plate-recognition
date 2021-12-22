'''
Description: 查看生成的矩形
Author: Lirenjie
Date: 2021-12-21 21:22:08
LastEditors: Lirenjie
LastEditTime: 2021-12-22 15:55:23
'''
import cv2
import numpy as np
from numpy.linalg import norm
import sys
import os
import json

import turtle as t
import time

img = cv2.imread("C:\\Users\\lirenjie\\Desktop\\cAA662F.jpg")
oldimg = cv2.GaussianBlur(img, (3, 3), 0)  # 图片分辨率调整
pic_hight, pic_width = (576, 704)


box = [[114, 295], [115, 259], [208, 262], [207, 298]]

t.penup()
t.goto(box[0])

t.pendown()
t.goto(box[1])
t.goto(box[2])
t.goto(box[3])
t.goto(box[0])

t.down()
# time.sleep(3)


heigth_point = right_point = [0, 0]
left_point = low_point = [1000, 1000]
for point in box:
    if left_point[0] > point[0]:
        left_point = point
    if low_point[1] > point[1]:
        low_point = point
    if heigth_point[1] < point[1]:
        heigth_point = point
    if right_point[0] < point[0]:
        right_point = point

# 比较得到长边的斜率
length1 = (left_point[0] - low_point[0]) ** 2 + (left_point[1] - low_point[1]) ** 2
length2 = (right_point[0] - low_point[0]) ** 2 + (right_point[1] - low_point[1]) ** 2
if length1 > length2:
    k = (left_point[1] - low_point[1]) / (left_point[0] - low_point[0])
else:
    k = (right_point[1] - low_point[1]) / (right_point[0] - low_point[0])
print('k', k)

if k < 0:  # 正角度
    new_right_point = [right_point[0], heigth_point[1]]
    pts2 = np.float32([left_point, heigth_point, new_right_point])  # 字符只是高度需要改变
    pts1 = np.float32([left_point, heigth_point, right_point])
    M = cv2.getAffineTransform(pts1, pts2)  # 仿射变换
    dst = cv2.warpAffine(oldimg, M, (pic_width, pic_hight))
    cv2.imshow("card", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # dst = cv2.warpAffine(oldimg, M, (pic_width, pic_hight))
    # cv2.imshow("card", dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # point_limit(new_right_point)
    # point_limit(heigth_point)
    # point_limit(left_point)
    # card_img = dst[
    #     int(left_point[1]) : int(heigth_point[1]),
    #     int(left_point[0]) : int(new_right_point[0]),
    # ]

    # print(card_img)

    # card_imgs.append(card_img)
    # cv2.imshow("card", card_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
elif k > 0:  # 负角度
    new_left_point = [left_point[0], heigth_point[1]]
    pts2 = np.float32([new_left_point, heigth_point, right_point])  # 字符只是高度需要改变
    pts1 = np.float32([left_point, heigth_point, right_point])
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(oldimg, M, (pic_width, pic_hight))
    cv2.imshow("card", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # dst = cv2.warpAffine(oldimg, M, (pic_width, pic_hight))
    # cv2.imshow("card", dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # point_limit(right_point)
    # point_limit(heigth_point)
    # point_limit(new_left_point)
    # card_img = dst[
    #     int(right_point[1]) : int(heigth_point[1]),
    #     int(new_left_point[0]) : int(right_point[0]),
    # ]

    # print(card_img)

    # card_imgs.append(card_img)
    # cv2.imshow("card", card_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

print(M)
