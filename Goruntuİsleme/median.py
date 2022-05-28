# median filtresi yani gürültü azaltma
import cv2 as cv
resim = cv.imread("gurultu.jpg")
medyan = cv.medianBlur(resim,1)

cv.imshow("Resim",resim)
cv.imshow("Medyanlasmis hal ",medyan)


cv.waitKey(0)