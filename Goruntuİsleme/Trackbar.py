import cv2 as cv
import numpy as np

siyah=np.zeros((480,640,3),np.uint8)
cv.namedWindow("pencere")

def fonk(x):
    print(x)

cv.createTrackbar("sezer","pencere",0,255,fonk)
while True:
    ali=cv.getTrackbarPos("sezer","pencere")
    cv.imshow("pencere",siyah)
    cv.waitKey(1)