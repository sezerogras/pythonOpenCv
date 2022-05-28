import cv2 as cv

resim = cv.imread("renk.jpg")
hsv=cv.cvtColor(resim,cv.COLOR_BGR2HSV)
cv.imshow("gercek",resim)
cv.imshow("HSV",hsv)
cv.waitKey(0)