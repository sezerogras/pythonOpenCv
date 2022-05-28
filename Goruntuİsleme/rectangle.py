# dikdörtgen çizdirelim

import cv2 as cv
oku = cv.imread("iha son .png")
pt1=(12,12)
cv.rectangle(oku,pt1,(155,300),(0,0,255),5)
cv.imshow("pencere",oku)
cv.waitKey(0)
