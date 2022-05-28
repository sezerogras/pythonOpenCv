import cv2 as cv

resim=cv.imread("select.jpg",0)
#griFormat=cv.cvtColor(resim,cv.COLOR_BGR2GRAY)
cv.imshow("orijinal",resim)
#cv.imshow("gri format",griFormat)
cv.waitKey(0)