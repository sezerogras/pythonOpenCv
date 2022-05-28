# doğru çizdirelim

import cv2 as cv

dogru = cv.imread("iha son .png")
cv.line(dogru,(21,21),(295,340),(55,152,255),6,None,None)
cv.imshow("dogru",dogru)
cv.waitKey(0)