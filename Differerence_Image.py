import cv2
import numpy as np

pic1 = cv2.imread('Anjing.png')
pic2 = cv2.imread('Anjing2.png')

gray_pic1 = cv2.cvtColor(pic1, cv2.COLOR_BGR2GRAY)
gray_pic2 = cv2.cvtColor(pic2, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(gray_pic1, gray_pic2)

eq_diff_pic = cv2.equalizeHist(diff)

cv2.imshow('Difference Picture', diff)
cv2.imshow('Histogram Equalization Difference Image', eq_diff_pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
