import cv2 as cv

resim = cv.imread("ben.png",0) # yanına sıfır yazarak grii rengine dönüştürdüm
dondurme = cv.rotate(resim,cv.ROTATE_180)
dondurme2 = cv.rotate(resim,cv.ROTATE_90_COUNTERCLOCKWISE)
cv.imshow("180",dondurme)
cv.imshow("90",dondurme2)


cv.waitKey(0)