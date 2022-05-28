import cv2 as cv

resim= cv.imread("iha son .png")
kopya=resim.copy()
cv.imshow("kopya",kopya)
cv.imshow("orijinal",resim)
cv.waitKey(0)