import cv2 as cv
import numpy as np

def fonks(sayi):
    print(sayi)


cv.namedWindow("goruntu") # bu şekilde goruntu adında bir pencere oluşturdum
goruntu = np.zeros((450,495,3),np.uint8) # ben burada 8 bitlik imzasız bir görüntü ortaya çıkardım
cv.createTrackbar("mavi","goruntu",0,255,fonks)
cv.createTrackbar("yesil","goruntu",0,255,fonks)
cv.createTrackbar("kirmizi","goruntu",0,255,fonks)

while True:
    cv.imshow("goruntu",goruntu)
    mavi=cv.getTrackbarPos("mavi","goruntu")
    yesil = cv.getTrackbarPos("yesil", "goruntu")
    kirmizi = cv.getTrackbarPos("kirmizi", "goruntu")

    goruntu[:]=[mavi,yesil,kirmizi]
    cv.waitKey(1)