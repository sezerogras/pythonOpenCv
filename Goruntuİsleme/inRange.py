
# belirli piksellerde renk takibi işlemmi , maskeleme işlemi

import cv2 as cv
import numpy as np
resim=cv.imread("linus.jpg")

az =np.array([0,10,100])
cok=np.array([255,255,255])

istenen = cv.inRange(resim,az,cok)

sonuc = cv.bitwise_and(resim,resim,mask=istenen)
cv.imshow("orijinal",resim)
cv.imshow("inrange",istenen)
cv.imshow("sonuc",sonuc)
cv.waitKey(0)