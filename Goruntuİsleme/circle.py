# daire cizdirelim.

import cv2 as cv

oku=cv.imread("iha son .png")
cv.circle(oku,(200,200),90,(125,150,12,200),-1)
cv.imshow("pencere",oku)
cv.waitKey(0)
