import cv2 as cv
def tersineCevirme(matris) :
   return cv.bitwise_not(matris)

resim =cv.imread("linus.jpg")
ters= tersineCevirme(resim)
cv.imshow("resim",resim)
cv.imshow("ters hali",ters)
cv.imshow("ters halin tersi ",tersineCevirme(ters))
cv.waitKey(0)
